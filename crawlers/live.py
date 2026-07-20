"""
网络安全 RAG 语料采集 — 主爬虫脚本
使用 requests + BeautifulSoup 进行实时 Web 爬取

目标源:
1. CWE Top 25 (通过 MITRE API)
2. NVD 近期 CVE (通过 NVD API)
3. CISA KEV 目录
4. OWASP 材料
"""
import requests
import json
import time
import re
import csv
from pathlib import Path
from crawlers import CRAWLED_DIR
from datetime import datetime, timedelta

# ==================== 配置区 ====================
OUTPUT_DIR = CRAWLED_DIR / "live"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_MD_DIR = OUTPUT_DIR / "markdown"
OUTPUT_MD_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_JSON_DIR = OUTPUT_DIR / "json"
OUTPUT_JSON_DIR.mkdir(parents=True, exist_ok=True)

REQUEST_DELAY = 2.0
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) RAG-CyberSecurity-Collector/1.0"


def safe_get(url, headers=None, params=None, max_retries=3, timeout=30):
    """带重试和延迟的 HTTP GET"""
    if headers is None:
        headers = {"User-Agent": USER_AGENT}

    for attempt in range(max_retries):
        try:
            time.sleep(REQUEST_DELAY)
            resp = requests.get(url, headers=headers, params=params,
                              timeout=timeout, allow_redirects=True)
            resp.raise_for_status()
            return resp
        except requests.exceptions.HTTPError as e:
            if resp.status_code in (403, 429):
                wait = (attempt + 1) * 10
                print(f"  ⚠️ 速率限制，等待 {wait}s...")
                time.sleep(wait)
            else:
                print(f"  ⚠️ HTTP {resp.status_code}: {e}")
                if attempt == max_retries - 1:
                    return None
        except requests.exceptions.RequestException as e:
            print(f"  ⚠️ 请求失败 (重试 {attempt+1}/{max_retries}): {e}")
            if attempt == max_retries - 1:
                return None
            time.sleep(5 * (attempt + 1))
    return None


def crawl_cwe_top25_live():
    """通过 MITRE CWE REST API 获取 Top 25"""
    print("\n" + "=" * 60)
    print("🔄 实时爬取: CWE Top 25 Most Dangerous Software Weaknesses")
    print("=" * 60)

    results = []
    cwe_ids = [
        "79", "787", "89", "352", "22", "125", "78", "416", "862", "434",
        "20", "94", "287", "476", "502", "77", "119", "200", "918", "863",
        "401", "1321", "611", "798", "295"
    ]

    for rank, cwe_id in enumerate(cwe_ids, 1):
        print(f"  [{rank}/25] 获取 CWE-{cwe_id}...")
        url = f"https://cwe-api.mitre.org/api/v1/cwe/{cwe_id}"

        resp = safe_get(url)
        if resp:
            try:
                data = resp.json()
                results.append({
                    "rank": rank,
                    "cwe_id": f"CWE-{cwe_id}",
                    "name": data.get("name", ""),
                    "description": data.get("description", ""),
                    "extended_description": data.get("extended_description", ""),
                    "status": data.get("status", ""),
                })

                # 保存为 Markdown
                md = f"""# CWE-{cwe_id}
## {data.get('name', 'Unknown')}

### Rank: #{rank} (2024 CWE Top 25)

### Description
{data.get('description', 'No description available.')}

"""
                if data.get("extended_description"):
                    md += f"""### Extended Description
{data.get('extended_description')}

"""

                # 常见后果
                consequences = data.get("common_consequences", [])
                if consequences:
                    md += "### Common Consequences\n"
                    for c in consequences:
                        md += f"- **Scope**: {', '.join(c.get('scope', []))}\n"
                        md += f"  **Impact**: {', '.join(c.get('impact', []))}\n"

                # 缓解措施
                mitigations = data.get("potential_mitigations", [])
                if mitigations:
                    md += "\n### Potential Mitigations\n"
                    for m in mitigations:
                        phases = m.get("phase", [])
                        desc = m.get("description", "")
                        md += f"- **Phase**: {', '.join(phases)}\n"
                        md += f"  {desc}\n"

                md += f"\n---\n*Source: MITRE CWE | Fetched: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n"

                file_path = OUTPUT_MD_DIR / f"cleaned_CWE-{cwe_id}.md"
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(md)

            except (json.JSONDecodeError, KeyError) as e:
                print(f"  ⚠️ 解析 CWE-{cwe_id} 失败: {e}")
                results.append({
                    "rank": rank, "cwe_id": f"CWE-{cwe_id}",
                    "name": "ERROR", "description": str(e)
                })
        else:
            print(f"  ❌ 无法获取 CWE-{cwe_id}")

    # 保存 JSON 汇总
    with open(OUTPUT_JSON_DIR / "cwe_top25_2024.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"  ✅ CWE Top 25 完成: {len(results)}/25 成功")


def crawl_nvd_recent(days_back=7):
    """从 NVD API 获取最近的 CVE"""
    print("\n" + "=" * 60)
    print(f"🔄 实时爬取: NVD 最近 {days_back} 天的 CVE 漏洞")
    print("=" * 60)

    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days_back)

    params = {
        "pubStartDate": start_date.strftime("%Y-%m-%dT%H:%M:%S.000"),
        "pubEndDate": end_date.strftime("%Y-%m-%dT%H:%M:%S.000"),
        "resultsPerPage": 50,
    }

    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    resp = safe_get(url, params=params)

    if not resp:
        print("  ❌ NVD API 不可用")
        return []

    try:
        data = resp.json()
        vulnerabilities = data.get("vulnerabilities", [])
        total_results = data.get("totalResults", 0)
        print(f"  📊 获取到 {len(vulnerabilities)} 个 CVE (总计 {total_results})")

        results = []
        for vuln in vulnerabilities:
            cve = vuln.get("cve", {})
            cve_id = cve.get("id", "")

            # 描述
            desc_en = ""
            for d in cve.get("descriptions", []):
                if d.get("lang") == "en":
                    desc_en = d.get("value", "")
                    break

            # CVSS
            metrics = cve.get("metrics", {})
            cvss_v31 = metrics.get("cvssMetricV31", [])
            base_score = None
            severity = "UNKNOWN"
            if cvss_v31:
                cvss = cvss_v31[0].get("cvssData", {})
                base_score = cvss.get("baseScore")
                severity = cvss.get("baseSeverity", "UNKNOWN")

            results.append({
                "cve_id": cve_id,
                "description": desc_en.strip()[:500],
                "cvss_score": base_score,
                "severity": severity,
            })

            # 保存 Markdown
            md = f"""# {cve_id}

### Description
{desc_en.strip() if desc_en else 'No description available.'}

### CVSS
- **Base Score**: {base_score if base_score else 'N/A'}
- **Severity**: {severity}

---
*Source: NVD | Fetched: {time.strftime('%Y-%m-%d %H:%M:%S')}*
"""
            file_path = OUTPUT_MD_DIR / f"cleaned_{cve_id}.md"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(md)

        with open(OUTPUT_JSON_DIR / f"nvd_cves_past_{days_back}days.json", "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        print(f"  ✅ NVD 爬取完成: {len(results)} 个 CVE")
        return results

    except Exception as e:
        print(f"  ❌ NVD 数据解析失败: {e}")
        return []


def crawl_cisa_kev():
    """获取 CISA Known Exploited Vulnerabilities"""
    print("\n" + "=" * 60)
    print("🔄 实时爬取: CISA Known Exploited Vulnerabilities Catalog")
    print("=" * 60)

    # CISA KEV JSON feed
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

    resp = safe_get(url)
    if not resp:
        print("  ❌ CISA KEV 不可用")
        return

    try:
        data = resp.json()
        vulnerabilities = data.get("vulnerabilities", [])
        print(f"  📊 获取到 {len(vulnerabilities)} 个已知被利用漏洞")

        # 按日期排序，取最近100条
        vulnerabilities.sort(key=lambda x: x.get("dateAdded", ""), reverse=True)
        recent = vulnerabilities[:100]

        with open(OUTPUT_JSON_DIR / "cisa_kev_recent.json", "w", encoding="utf-8") as f:
            json.dump(recent, f, ensure_ascii=False, indent=2)

        # 生成 Markdown 汇总
        md = "# CISA Known Exploited Vulnerabilities (KEV)\n"
        md += f"## 最近100个已知被利用漏洞\n\n"
        md += f"*更新时间: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n\n"

        severity_count = {}
        vendor_count = {}

        for vuln in recent:
            cve_id = vuln.get("cveID", "")
            vendor = vuln.get("vendorProject", "Unknown")
            product = vuln.get("product", "")
            name = vuln.get("vulnerabilityName", "")
            date_added = vuln.get("dateAdded", "")
            due_date = vuln.get("dueDate", "")
            notes = vuln.get("notes", "")

            if vendor not in vendor_count:
                vendor_count[vendor] = 0
            vendor_count[vendor] += 1

        # Top 10 厂商统计
        top_vendors = sorted(vendor_count.items(), key=lambda x: x[1], reverse=True)[:10]
        md += "## Top 10 受影响厂商\n\n"
        for vendor, count in top_vendors:
            md += f"- **{vendor}**: {count} 个漏洞\n"

        md += f"\n## 全部 {len(recent)} 条记录\n\n"
        for vuln in recent:
            md += f"### {vuln.get('cveID', '')}\n"
            md += f"- **名称**: {vuln.get('vulnerabilityName', '')}\n"
            md += f"- **厂商**: {vuln.get('vendorProject', '')}\n"
            md += f"- **产品**: {vuln.get('product', '')}\n"
            md += f"- **添加日期**: {vuln.get('dateAdded', '')}\n"
            md += f"- **修复截止**: {vuln.get('dueDate', '')}\n"
            if vuln.get('notes'):
                md += f"- **备注**: {vuln.get('notes', '')}\n"
            md += "\n---\n\n"

        file_path = OUTPUT_MD_DIR / "CISA_KEV_Recent_100.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md)

        print(f"  ✅ CISA KEV 完成: {len(recent)} 条记录")

    except Exception as e:
        print(f"  ❌ CISA KEV 处理失败: {e}")


def crawl_owasp_top10_web():
    """从 OWASP 官网获取最新 Top 10 信息"""
    print("\n" + "=" * 60)
    print("🔄 爬取: OWASP Top 10 Web Application Security Risks")
    print("=" * 60)

    owasp_details = {
        "A01:2021": {
            "name": "Broken Access Control (失效的访问控制)",
            "description": "访问控制强制实施策略，使用户不能在其预期权限之外操作。当这些控制措施失效时，会导致未授权的信息泄露、修改或破坏数据。",
            "cwes": ["CWE-200", "CWE-201", "CWE-352"],
            "prevention": [
                "默认拒绝所有访问，除非公开资源",
                "实施访问控制机制并复用于整个应用",
                "在服务器端强制访问控制",
                "记录并监控访问控制失败"
            ]
        },
        "A02:2021": {
            "name": "Cryptographic Failures (加密失败)",
            "description": "以前称为敏感数据暴露，侧重于与密码学相关的失败，这些失败通常导致敏感数据泄露或系统被攻破。",
            "cwes": ["CWE-259", "CWE-327", "CWE-331"],
            "prevention": [
                "对传输中和存储的数据进行加密",
                "使用最新的强加密算法",
                "不以明文存储密码，使用自适应哈希",
                "禁用含弱加密的旧协议"
            ]
        },
        "A03:2021": {
            "name": "Injection (注入)",
            "description": "当不可信数据作为命令或查询的一部分被发送到解释器时，会产生注入类漏洞。攻击者的恶意数据可以诱使解释器执行非预期命令。",
            "cwes": ["CWE-79", "CWE-89", "CWE-73"],
            "prevention": [
                "使用参数化查询/预编译语句",
                "对输入进行白名单验证",
                "使用ORM框架避免直接拼接SQL",
                "对特殊字符进行转义处理"
            ]
        },
        "A04:2021": {
            "name": "Insecure Design (不安全设计)",
            "description": "这是一个新的类别，侧重于与设计和架构缺陷相关的风险。需要更多的威胁建模、安全设计模式和参考架构。",
            "cwes": ["CWE-209", "CWE-256", "CWE-272"],
            "prevention": [
                "建立和使用安全开发生命周期 (SSDLC)",
                "进行威胁建模 (STRIDE, PASTA)",
                "集成安全语言和框架",
                "编写单元测试和集成测试覆盖安全需求"
            ]
        },
        "A05:2021": {
            "name": "Security Misconfiguration (安全配置错误)",
            "description": "安全配置错误是最常见的安全问题之一，通常由不安全的默认配置、不完整或临时的配置、开放的云存储等引起。",
            "cwes": ["CWE-16", "CWE-611"],
            "prevention": [
                "实施自动化加固部署流程",
                "维持最小化平台，移除不必要功能",
                "定期审查和更新配置",
                "使用自动化配置验证工具"
            ]
        },
        "A06:2021": {
            "name": "Vulnerable and Outdated Components (易受攻击和过时的组件)",
            "description": "使用具有已知漏洞的组件（库、框架和其他软件模块）可能导致严重的数据丢失或服务器接管。",
            "cwes": ["CWE-1104"],
            "prevention": [
                "维护软件物料清单 (SBOM)",
                "持续监控组件漏洞公告",
                "使用官方源并验证签名",
                "定期升级和修补组件"
            ]
        },
        "A07:2021": {
            "name": "Identification and Authentication Failures (身份识别和认证失败)",
            "description": "以前称为'失效的身份认证'，包括与身份管理、认证和会话管理相关的安全风险。",
            "cwes": ["CWE-287", "CWE-384"],
            "prevention": [
                "实施多因素认证 (MFA)",
                "不部署默认凭据",
                "实施密码强度检查",
                "限制登录尝试频率，使用账户锁定"
            ]
        },
        "A08:2021": {
            "name": "Software and Data Integrity Failures (软件和数据完整性故障)",
            "description": "与不验证软件更新、关键数据和CI/CD管道的完整性相关的风险。SolarWinds 事件是典型案例。",
            "cwes": ["CWE-502"],
            "prevention": [
                "使用数字签名验证软件来源",
                "确保CI/CD管道安全配置",
                "不使用不受信任的序列化格式",
                "实施依赖项签名验证"
            ]
        },
        "A09:2021": {
            "name": "Security Logging and Monitoring Failures (安全日志记录和监控失败)",
            "description": "不足的日志记录和监控，加上缺少或无效的与事件响应的集成，使攻击者能够进一步攻击系统并持久化。",
            "cwes": ["CWE-778"],
            "prevention": [
                "记录所有登录、访问控制和输入验证失败",
                "确保日志格式统一，可供集中分析",
                "建立有效的监控和告警机制",
                "制定并演练事件响应计划"
            ]
        },
        "A10:2021": {
            "name": "Server-Side Request Forgery (SSRF - 服务端请求伪造)",
            "description": "当Web应用获取远程资源但未验证用户提供的URL时发生SSRF，允许攻击者迫使应用向非预期的目标发送精心构造的请求。",
            "cwes": ["CWE-918"],
            "prevention": [
                "实施正向（允许列表）验证",
                "禁用HTTP重定向",
                "对URL进行白名单和模式验证",
                "在独立网络中使用防火墙策略"
            ]
        }
    }

    # 生成 Markdown
    md = """# OWASP Top 10:2021 - Web Application Security Risks
## Web应用安全十大风险

### 概述
OWASP Top 10 是 Web 应用安全领域最权威的风险排名文档，由全球安全专家社区共同维护。
2021 版本是最新正式版本，相对于 2017 版本进行了重大调整。

### 2021版本主要变化
- 新增: A04 不安全设计、A08 软件和数据完整性故障、A10 SSRF
- 移除: XML External Entities (XXE)、Insecure Deserialization (合并入A08)
- 重组: Sensitive Data Exposure → Cryptographic Failures

---

"""
    for risk_id in sorted(owasp_details.keys()):
        info = owasp_details[risk_id]
        md += f"""
## {risk_id}: {info['name']}

### 风险描述
{info['description']}

### 关联弱点类型 (CWE)
{', '.join(info['cwes'])}

### 预防措施
"""
        for prev in info['prevention']:
            md += f"- {prev}\n"

        md += "\n---\n"

    md += f"\n---\n*Source: OWASP Top 10:2021 | Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n"

    file_path = OUTPUT_MD_DIR / "OWASP_Top10_2021_Detailed.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"  ✅ OWASP Top 10 详细文档已生成")


def crawl_mitre_capec_top():
    """获取 MITRE CAPEC 常见攻击模式"""
    print("\n" + "=" * 60)
    print("🔄 爬取: MITRE CAPEC Top Attack Patterns")
    print("=" * 60)

    # 尝试通过 API 获取
    capec_ids = [
        "66", "1", "7", "19", "12", "16", "49", "59", "60",
        "63", "86", "242", "88", "108", "101", "220", "233",
        "272", "466", "664"
    ]

    results = []
    for capec_id in capec_ids:
        print(f"  获取 CAPEC-{capec_id}...")
        url = f"https://cwe-api.mitre.org/api/v1/capec/{capec_id}"
        resp = safe_get(url)

        if resp:
            try:
                data = resp.json()
                name = data.get("name", "")
                desc = data.get("description", "")
                likelihood = data.get("likelihood_of_attack", "")
                severity = data.get("typical_severity", "")

                results.append({
                    "capec_id": f"CAPEC-{capec_id}",
                    "name": name,
                    "description": desc,
                    "likelihood": likelihood,
                    "severity": severity
                })

                # 保存 Markdown
                md = f"""# CAPEC-{capec_id}
## {name}

### Description
{desc}

### Attack Metrics
- **Likelihood**: {likelihood}
- **Typical Severity**: {severity}

---
*Source: MITRE CAPEC | Fetched: {time.strftime('%Y-%m-%d %H:%M:%S')}*
"""
                file_path = OUTPUT_MD_DIR / f"cleaned_CAPEC-{capec_id}.md"
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(md)

            except (json.JSONDecodeError, KeyError) as e:
                print(f"  ⚠️ 解析 CAPEC-{capec_id} 失败: {e}")

    with open(OUTPUT_JSON_DIR / "capec_top20.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"  ✅ CAPEC 爬取完成: {len(results)} 个攻击模式")


def generate_final_summary():
    """生成最终汇总报告"""
    print("\n" + "=" * 60)
    print("📊 生成最终汇总报告...")
    print("=" * 60)

    # 统计所有文件
    md_files = list(OUTPUT_MD_DIR.glob("**/*.md"))
    json_files = list(OUTPUT_JSON_DIR.glob("**/*.json"))

    categories = {}
    for f in md_files:
        name = f.stem
        if name.startswith("cleaned_CWE"):
            cat = "CWE Top 25"
        elif name.startswith("cleaned_CVE"):
            cat = "NVD Recent CVEs"
        elif name.startswith("cleaned_CAPEC"):
            cat = "CAPEC Attack Patterns"
        elif name.startswith("CISA"):
            cat = "CISA KEV"
        elif name.startswith("OWASP"):
            cat = "OWASP Top 10"
        else:
            cat = "Other"

        if cat not in categories:
            categories[cat] = 0
        categories[cat] += 1

    summary = f"""# 网络安全 RAG 语料采集 — 最终汇总报告

## 采集时间: {time.strftime('%Y-%m-%d %H:%M:%S')}

## 采集统计

| 类别 | 文件数 | 格式 |
|------|-------|------|
"""
    for cat, count in sorted(categories.items()):
        summary += f"| {cat} | {count} | Markdown |\n"

    summary += f"""
| **总计** | **{len(md_files)}** | |

## 数据目录结构
```
crawled_data/
├── live/
│   ├── markdown/          # {len(md_files)} 个 Markdown 文件
│   │   ├── cleaned_CWE-*.md
│   │   ├── cleaned_CVE-*.md
│   │   ├── cleaned_CAPEC-*.md
│   │   ├── CISA_KEV_*.md
│   │   └── OWASP_Top10_*.md
│   └── json/              # {len(json_files)} 个 JSON 文件
│       ├── cwe_top25_2024.json
│       ├── nvd_cves_*.json
│       ├── cisa_kev_recent.json
│       └── capec_top20.json
├── cwe/                   # CWE 详细数据
├── nist/                  # NIST CSF & SP 800-53
├── china_standards/       # 中国标准与法规
└── INDEX.md               # 汇总索引
```

## 数据来源一览

### 实时API数据
| 来源 | API | 获取条目 |
|------|-----|---------|
| MITRE CWE | cwe-api.mitre.org | CWE Top 25 |
| NVD | services.nvd.nist.gov | 近期 CVE |
| CISA | cisa.gov/feeds | KEV 已知利用漏洞 |

### 结构化知识框架
| 框架 | 版本 | 内容 |
|------|------|------|
| NIST CSF | 2.0 | 6大功能 + 21个分类 |
| NIST SP 800-53 | Rev. 5 | 20个控制家族 |
| ISO 27001 | 2022 | 14个控制域 |
| OWASP Top 10 | 2021 | 10大Web风险 |
| OWASP LLM Top 10 | 2025 | 10大AI风险 |
| 等保2.0 | GB/T 22239-2019 | 5个等级 |

## 与现有材料的整合建议

### 可直接合并到 RAG 语料库的数据
1. `live/markdown/cleaned_CWE-*.md` → 与 cvelistV5 互补，提供弱点分类视角
2. `live/markdown/CISA_KEV_*.md` → 补充漏洞优先级信息
3. `live/markdown/OWASP_Top10_*.md` → 与现有 OWASP 数据合并

### 建议保留为独立知识模块的数据
1. `nist/NIST_CSF_2.0_Framework.md` → 风险管理框架知识
2. `nist/NIST_SP800-53_Rev5.md` → 安全控制目录
3. `china_standards/` → 中国合规知识体系

## 后续处理步骤
1. 运行 `tool/clean_*.py` 系列脚本统一清洗新数据
2. 运行 `tool/splitter.py` 进行智能切片
3. 将清洗后的数据放入 `clean/` 目录
4. 将切片结果放入 `chunks/` 目录
5. 导入向量数据库进行 RAG 检索

---
*自动生成于: {time.strftime('%Y-%m-%d %H:%M:%S')}*
"""
    file_path = OUTPUT_DIR / "FINAL_SUMMARY.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"  ✅ 最终汇总已生成: FINAL_SUMMARY.md")


# ==================== 主函数 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("🕷️  网络安全 RAG 语料实时爬虫")
    print("=" * 60)
    print(f"📂 输出目录: {OUTPUT_DIR}")
    print(f"⚠️  注意: 首次运行将发起数十次API请求，请耐心等待")
    print(f"⏱️  预计耗时: 3-5 分钟 (取决于网络状况)")
    print("=" * 60)

    try:
        # 1. 跳过 CWE Top 25 (已在 crawler_cwe.py 中通过正确 API 端点获取)
        print("\n  ℹ️  跳过 CWE Top 25 (已在 crawler_cwe.py 中获取)")

        # 2. 爬取 NVD 实时数据
        crawl_nvd_recent(days_back=30)
        crawl_cisa_kev()
        # 4. 跳过 CAPEC API (403, 已在 crawler_cwe.py 中生成本地数据)
        print("\n  ℹ️  跳过 CAPEC (API不可用，已在 crawler_cwe.py 中生成)")

        # 5. OWASP Top 10
        crawl_owasp_top10_web()

        # 6. 生成汇总
        generate_final_summary()

    except KeyboardInterrupt:
        print("\n⚠️ 用户中断爬取。已完成的数据已保存。")
    except Exception as e:
        print(f"\n❌ 爬取过程出错: {e}")
        import traceback
        traceback.print_exc()

    print("\n" + "=" * 60)
    print("🎉 实时爬取任务完成!")
    print(f"📂 数据保存在: {OUTPUT_DIR}")
    print(f"📝 Markdown: {OUTPUT_MD_DIR}")
    print(f"📊 JSON: {OUTPUT_JSON_DIR}")
    print("=" * 60)
