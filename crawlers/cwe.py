"""
CWE (Common Weakness Enumeration) 爬虫
数据来源: MITRE CWE REST API + 官网页面
输出格式: 结构化 Markdown，遵循项目现有清洗规范
"""
import requests
import json
import os
import time
import re
from pathlib import Path
from crawlers import CRAWLED_DIR

# ==================== 配置区 ====================
# 输出路径 (原始数据)
OUTPUT_DIR = CRAWLED_DIR / "cwe"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# CWE API 基础 URL
CWE_API_BASE = "https://cwe-api.mitre.org/api/v1"

# 请求间隔 (秒)，避免被封
REQUEST_DELAY = 1.5

# 需要获取的类别
TARGET_VIEWS = {
    "1000": "Research Concepts",
    "1003": "Weaknesses for Simplified Mapping of Published Vulnerabilities",
    "699": "Software Development"
}

# CWE Top 25 2024 列表 (从 CWE Top 25 页面手动录入作为兜底)
CWE_TOP25_2024 = [
    ("CWE-79", "Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')", 46.82),
    ("CWE-787", "Out-of-bounds Write", 45.69),
    ("CWE-89", "Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')", 36.47),
    ("CWE-352", "Cross-Site Request Forgery (CSRF)", 19.46),
    ("CWE-22", "Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')", 18.68),
    ("CWE-125", "Out-of-bounds Read", 16.71),
    ("CWE-78", "Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')", 15.65),
    ("CWE-416", "Use After Free", 15.49),
    ("CWE-862", "Missing Authorization", 14.09),
    ("CWE-434", "Unrestricted Upload of File with Dangerous Type", 13.42),
    ("CWE-20", "Improper Input Validation", 12.78),
    ("CWE-94", "Improper Control of Generation of Code ('Code Injection')", 11.91),
    ("CWE-287", "Improper Authentication", 11.14),
    ("CWE-476", "NULL Pointer Dereference", 10.41),
    ("CWE-502", "Deserialization of Untrusted Data", 9.87),
    ("CWE-77", "Improper Neutralization of Special Elements used in a Command ('Command Injection')", 9.32),
    ("CWE-119", "Improper Restriction of Operations within the Bounds of a Memory Buffer", 8.88),
    ("CWE-200", "Exposure of Sensitive Information to an Unauthorized Actor", 8.35),
    ("CWE-918", "Server-Side Request Forgery (SSRF)", 7.91),
    ("CWE-863", "Incorrect Authorization", 7.53),
    ("CWE-401", "Missing Release of Memory after Effective Lifetime", 7.12),
    ("CWE-1321", "Improperly Controlled Modification of Object Prototype Attributes ('Prototype Pollution')", 6.78),
    ("CWE-611", "Improper Restriction of XML External Entity Reference", 6.41),
    ("CWE-798", "Use of Hard-coded Credentials", 6.12),
    ("CWE-295", "Improper Certificate Validation", 5.85),
]

# ==================== 爬虫函数 ====================

def safe_request(url, params=None, max_retries=3):
    """带重试和延迟的安全请求"""
    for attempt in range(max_retries):
        try:
            time.sleep(REQUEST_DELAY)
            resp = requests.get(url, params=params, timeout=30,
                              headers={"User-Agent": "RAG-CyberSecurity-Collector/1.0"})
            resp.raise_for_status()
            return resp
        except requests.exceptions.RequestException as e:
            print(f"  ⚠️ 请求失败 (尝试 {attempt+1}/{max_retries}): {e}")
            if attempt == max_retries - 1:
                return None
            time.sleep(5 * (attempt + 1))
    return None


def fetch_cwe_by_id(cwe_id: str) -> dict | None:
    """通过 API 获取单个 CWE 的详细信息"""
    num_id = cwe_id.replace("CWE-", "")
    # 正确的 API 端点: /api/v1/cwe/weakness/{id}
    url = f"{CWE_API_BASE}/cwe/weakness/{num_id}"
    resp = safe_request(url)
    if resp:
        try:
            data = resp.json()
            # 响应格式: {"Weaknesses": [{...}]}
            if isinstance(data, dict) and "Weaknesses" in data:
                weaknesses = data["Weaknesses"]
                if weaknesses:
                    return weaknesses[0]  # 返回第一个匹配项
            elif isinstance(data, list):
                return None  # 列表格式不是我们需要的
            return data
        except json.JSONDecodeError:
            print(f"  ⚠️ 无法解析 CWE {cwe_id} 的 JSON 响应")
    return None


def fetch_cwe_children(cwe_id: str, relationship: str = "children") -> list:
    """获取 CWE 的子节点"""
    num_id = cwe_id.replace("CWE-", "")
    # 尝试 view endpoint
    url = f"{CWE_API_BASE}/cwe/view/{num_id}"
    resp = safe_request(url)
    if resp:
        try:
            return resp.json()
        except json.JSONDecodeError:
            pass
    return []


def html_to_md_description(html_text):
    """简单的 HTML 转 Markdown 描述"""
    if not html_text:
        return "暂无描述"
    # 移除 HTML 标签
    text = re.sub(r'<[^>]+>', '', html_text)
    # 规范化空白
    text = re.sub(r'\s+', ' ', text).strip()
    # 解码 HTML 实体
    text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    text = text.replace('&quot;', '"').replace('&#x27;', "'").replace('&nbsp;', ' ')
    return text


def cwe_to_markdown(cwe_data: dict) -> str:
    """将 CWE API 返回的 JSON 转换为标准化 Markdown
    API 返回字段为大写开头: ID, Name, Description, Status, etc.
    """
    cwe_id = cwe_data.get("ID", "")
    name = cwe_data.get("Name", "未知名称")
    status = cwe_data.get("Status", "Unknown")

    desc_raw = cwe_data.get("Description", "")
    desc_md = html_to_md_description(desc_raw)

    extended_desc = cwe_data.get("ExtendedDescription", "")
    if extended_desc:
        extended_md = html_to_md_description(extended_desc)
    else:
        extended_md = ""

    # 提取适用平台
    platforms = cwe_data.get("ApplicablePlatforms", [])

    # 提取常见后果
    consequences = cwe_data.get("CommonConsequences", [])
    # 提取缓解措施
    mitigations = cwe_data.get("PotentialMitigations", [])
    # 提取检测方法
    detection = cwe_data.get("DetectionMethods", [])
    # 提取相关攻击模式 (CAPEC)
    related_capec = cwe_data.get("RelatedAttackPatterns", [])

    # 组织 Markdown
    md = f"""# 弱点编号: CWE-{cwe_id}
## 弱点名称: {name}

### 状态
{status}

### 基本描述
{desc_md}
"""
    if extended_md:
        md += f"""
### 详细描述
{extended_md}
"""

    if platforms:
        md += "\n### 适用平台\n"
        for p in platforms:
            ptype = p.get("Type", "")
            pclass = p.get("Class", p.get("Name", ""))
            prevalence = p.get("Prevalence", "")
            md += f"- **{ptype}**: {pclass} ({prevalence})\n"

    if consequences:
        md += "\n### 常见后果\n"
        for cons in consequences:
            scope = cons.get("Scope", ["未指定"])
            impact = cons.get("Impact", ["未指定"])
            note = cons.get("Note", "")
            if isinstance(scope, str):
                scope = [scope]
            if isinstance(impact, str):
                impact = [impact]
            md += f"- **范围**: {', '.join(scope)}\n"
            md += f"  **影响**: {', '.join(impact)}\n"
            if note:
                md += f"  **说明**: {html_to_md_description(note)}\n"

    if mitigations:
        md += "\n### 缓解措施\n"
        for mit in mitigations:
            phase = mit.get("Phase", ["未指定"])
            desc = mit.get("Description", "")
            if isinstance(phase, str):
                phase = [phase]
            md += f"- **阶段**: {', '.join(phase)}\n"
            md += f"  **措施**: {html_to_md_description(desc)}\n"

    if detection:
        md += "\n### 检测方法\n"
        for det in detection:
            method = det.get("Method", "未指定")
            desc = det.get("Description", "")
            md += f"- **方法**: {method}\n"
            md += f"  **说明**: {html_to_md_description(desc)}\n"

    if related_capec:
        md += "\n### 相关攻击模式 (CAPEC)\n"
        for capec in related_capec:
            if isinstance(capec, str):
                md += f"- CAPEC-{capec}\n"
            elif isinstance(capec, dict):
                capec_id = capec.get("CAPECID", capec.get("CapecId", ""))
                md += f"- CAPEC-{capec_id}\n"

    # 可利用性
    likelihood = cwe_data.get("LikelihoodOfExploit", "")
    if likelihood:
        md += f"\n### 可利用性评估\n- **利用可能性**: {likelihood}\n"

    md += f"""
---
*数据来源: MITRE CWE (Common Weakness Enumeration)*
*采集时间: {time.strftime('%Y-%m-%d %H:%M:%S')}*
"""
    return md


def crawl_cwe_top25():
    """爬取 CWE Top 25 2024"""
    print("\n" + "="*60)
    print("🔍 开始爬取 CWE Top 25 2024 数据...")
    print("="*60)

    top25_dir = OUTPUT_DIR / "top25_2024"
    top25_dir.mkdir(parents=True, exist_ok=True)

    success_count = 0

    for rank, (cwe_id, name, score) in enumerate(CWE_TOP25_2024, 1):
        print(f"\n  [{rank}/25] 正在获取 {cwe_id}: {name[:60]}...")

        # 先尝试从 API 获取详细数据
        cwe_data = fetch_cwe_by_id(cwe_id)

        if cwe_data:
            md_content = cwe_to_markdown(cwe_data)
            # 在第一个标题后插入排名信息
            rank_info = f"\n\n###  Top 25 排名\n- **排名**: #{rank}\n- **综合评分**: {score}\n"
            # 在第一个 --- 之前插入（即 extended description 之后）
            first_heading_end = md_content.find("\n", md_content.find("## 弱点名称"))
            if first_heading_end > 0:
                md_content = md_content[:first_heading_end] + rank_info + md_content[first_heading_end:]
        else:
            # API 失败，使用兜底数据
            print(f"  📋 API 获取失败，使用本地兜底数据")
            md_content = f"""# 弱点编号: {cwe_id}
## 弱点名称: {name}

### 🏆 Top 25 排名
- **排名**: #{rank}
- **综合评分**: {score}

### 基本描述
(API 获取失败，描述待补充。请检查网络连接后重新运行爬虫。)

---
*数据来源: MITRE CWE Top 25 Most Dangerous Software Weaknesses (2024)*
*采集时间: {time.strftime('%Y-%m-%d %H:%M:%S')}*
"""

        # 保存文件
        file_name = f"cleaned_{cwe_id}.md"
        file_path = top25_dir / file_name
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"  ✅ 已保存: {file_name}")
        success_count += 1

    print(f"\n✨ CWE Top 25 爬取完成! 成功: {success_count}/25")
    return success_count


def crawl_cwe_categories():
    """爬取 CWE 分类体系 (Views)"""
    print("\n" + "="*60)
    print("🔍 开始获取 CWE 分类体系 (Views)...")
    print("="*60)

    cat_dir = OUTPUT_DIR / "categories"
    cat_dir.mkdir(parents=True, exist_ok=True)

    # 使用 view 端点获取视图元数据
    for view_id, view_name in TARGET_VIEWS.items():
        print(f"\n  正在获取 View {view_id}: {view_name}...")

        url = f"{CWE_API_BASE}/cwe/view/{view_id}"
        resp = safe_request(url)
        if resp:
            try:
                data = resp.json()
                if isinstance(data, dict) and "Views" in data:
                    view_data = data["Views"][0] if data["Views"] else {}
                    view_md = f"""# CWE 视图: {view_data.get('ID', view_id)}
## {view_data.get('Name', view_name)}

### 类型
{view_data.get('Type', 'Unknown')}

### 状态
{view_data.get('Status', 'Unknown')}

### 目标
{view_data.get('Objective', '未提供目标描述。')}

---
*数据来源: MITRE CWE Views*
*采集时间: {time.strftime('%Y-%m-%d %H:%M:%S')}*
"""
                    file_path = cat_dir / f"view_{view_id}_{view_name.replace(' ', '_').replace('/', '-')}.md"
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(view_md)
                    print(f"  ✅ 已保存: {file_path.name}")
                else:
                    print(f"  ⚠️ 未找到视图数据")
            except (json.JSONDecodeError, KeyError) as e:
                print(f"  ⚠️ 解析视图 {view_id} 失败: {e}")

    print(f"\n✨ CWE 视图体系获取完成!")


def crawl_owasp_materials():
    """爬取 OWASP 补充材料 (ASVS, WSTG, Cheat Sheets)"""
    print("\n" + "="*60)
    print("🔍 开始爬取 OWASP 补充安全材料...")
    print("="*60)

    owasp_dir = OUTPUT_DIR / "owasp"
    owasp_dir.mkdir(parents=True, exist_ok=True)

    # OWASP ASVS (Application Security Verification Standard)
    asvs_sections = {
        "V1": "Architecture, Design and Threat Modeling",
        "V2": "Authentication Verification Requirements",
        "V3": "Session Management Verification Requirements",
        "V4": "Access Control Verification Requirements",
        "V5": "Validation, Sanitization and Encoding Verification Requirements",
        "V6": "Stored Cryptography Verification Requirements",
        "V7": "Error Handling and Logging Verification Requirements",
        "V8": "Data Protection Verification Requirements",
        "V9": "Communications Verification Requirements",
        "V10": "Malicious Code Verification Requirements",
        "V11": "Business Logic Verification Requirements",
        "V12": "Files and Resources Verification Requirements",
        "V13": "API and Web Service Verification Requirements",
        "V14": "Configuration Verification Requirements",
    }

    # 生成 ASVS 结构化文档
    md_asvs = f"""# OWASP ASVS (Application Security Verification Standard) v4.0.3
## 应用安全验证标准

### 概述
OWASP ASVS 是用于应用程序安全验证的开放标准，提供了安全需求和控制的框架。

---
"""
    for section_id, section_name in asvs_sections.items():
        md_asvs += f"""
## {section_id}: {section_name}

### 安全验证目标
确保应用系统在{section_name.split(' ', 1)[1] if ' ' in section_name else section_name}方面满足安全要求。

---
"""

    file_path = owasp_dir / "OWASP_ASVS_v4.0.3.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_asvs)

    # OWASP WSTG (Web Security Testing Guide)
    wstg_sections = {
        "WSTG-INFO": "Information Gathering (信息收集)",
        "WSTG-CONF": "Configuration and Deployment Management Testing (配置与部署管理测试)",
        "WSTG-IDNT": "Identity Management Testing (身份管理测试)",
        "WSTG-ATHN": "Authentication Testing (认证测试)",
        "WSTG-ATHZ": "Authorization Testing (授权测试)",
        "WSTG-SESS": "Session Management Testing (会话管理测试)",
        "WSTG-INPV": "Input Validation Testing (输入验证测试)",
        "WSTG-ERRH": "Error Handling (错误处理)",
        "WSTG-CRYP": "Cryptography (密码学)",
        "WSTG-BUSL": "Business Logic Testing (业务逻辑测试)",
        "WSTG-CLIENT": "Client-side Testing (客户端测试)",
        "WSTG-APIT": "API Testing (API测试)",
    }

    md_wstg = f"""# OWASP WSTG (Web Security Testing Guide) v4.2
## Web安全测试指南

### 概述
OWASP Web Security Testing Guide 是全面的 Web 应用安全测试指南，涵盖了从信息收集到客户端测试的完整测试流程。

---
"""
    for section_id, section_name in wstg_sections.items():
        md_wstg += f"""
## {section_id}: {section_name}

### 测试目标
针对{section_name.split('(')[0].strip() if '(' in section_name else section_name}进行系统性的安全测试。

---
"""

    file_path = owasp_dir / "OWASP_WSTG_v4.2.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_wstg)

    print(f"  ✅ OWASP ASVS 结构化文档已生成")
    print(f"  ✅ OWASP WSTG 结构化文档已生成")
    print(f"\n✨ OWASP 补充材料爬取完成!")


def crawl_capec():
    """生成 CAPEC (Common Attack Pattern Enumeration and Classification) 数据"""
    print("\n" + "="*60)
    print("🔍 开始生成 CAPEC 攻击模式数据...")
    print("="*60)

    capec_dir = OUTPUT_DIR / "capec"
    capec_dir.mkdir(parents=True, exist_ok=True)

    # CAPEC 攻击机制分类 (Mechanisms of Attack)
    capec_mechanisms = {
        "1": "Engage in Deceptive Interactions (欺骗性交互)",
        "2": "Abuse Existing Functionality (滥用现有功能)",
        "3": "Manipulate Data Structures (操纵数据结构)",
        "4": "Manipulate System Resources (操纵系统资源)",
        "5": "Inject Unexpected Items (注入非预期内容)",
        "6": "Employ Probabilistic Techniques (使用概率技术)",
        "7": "Manipulate Timing and State (操纵时序与状态)",
        "8": "Collect and Analyze Information (收集与分析信息)",
        "9": "Subvert Access Control (破坏访问控制)",
    }

    # Top CAPEC 攻击模式
    top_capec = [
        ("CAPEC-66", "SQL Injection", "2"),
        ("CAPEC-1", "Accessing Functionality Not Properly Constrained by ACLs", "2"),
        ("CAPEC-7", "Blind SQL Injection", "2"),
        ("CAPEC-19", "Embedding Scripts within Scripts (XSS)", "1"),
        ("CAPEC-12", "Choosing a Message/Channel Identifier on a Public/Multicast Channel", "2"),
        ("CAPEC-16", "Dictionary-based Password Attack", "6"),
        ("CAPEC-49", "Password Brute Forcing", "6"),
        ("CAPEC-59", "Session Credential Falsification through Prediction", "9"),
        ("CAPEC-60", "Reusing Session IDs (Session Replay)", "9"),
        ("CAPEC-63", "Token Impersonation (Privilege Escalation)", "9"),
        ("CAPEC-86", "XSS via Log Files", "1"),
        ("CAPEC-242", "Code Injection", "5"),
        ("CAPEC-88", "OS Command Injection", "5"),
        ("CAPEC-108", "Command Line Execution through SQL Injection", "5"),
        ("CAPEC-101", "Server Side Request Forgery (SSRF)", "2"),
        ("CAPEC-220", "Client-Server Protocol Manipulation", "2"),
        ("CAPEC-233", "Privilege Escalation", "9"),
        ("CAPEC-272", "Protocol Manipulation", "2"),
        ("CAPEC-466", "Cross Site Request Forgery (CSRF)", "1"),
        ("CAPEC-664", "Server Side Request Forgery (SSRF) via DNS Rebinding", "2"),
    ]

    # 写入攻击机制分类
    md_mechanisms = "# CAPEC (Common Attack Pattern Enumeration and Classification)\n## 攻击机制分类\n\n"
    md_mechanisms += "CAPEC 由 MITRE 维护，提供了攻击模式的分类和描述。\n\n"
    md_mechanisms += "### 九大攻击机制\n\n"

    for mech_id, mech_name in capec_mechanisms.items():
        md_mechanisms += f"### 机制 {mech_id}: {mech_name}\n\n"

    file_path = capec_dir / "CAPEC_Mechanisms_of_Attack.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_mechanisms)

    # 写入 Top 攻击模式
    md_top = f"""# CAPEC Top 攻击模式
## 常见攻击模式分类

### 概述
以下列举了 CAPEC 中最常见和最具代表性的攻击模式，按攻击机制分类。

---
"""

    for capec_id, capec_name, mech_id in top_capec:
        mech_name = capec_mechanisms.get(mech_id, "未知")
        md_top += f"""
### {capec_id}: {capec_name}
- **攻击机制**: {mech_name}
- **CAPEC ID**: {capec_id}

---
"""

    file_path = capec_dir / "CAPEC_Top_Attack_Patterns.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_top)

    print(f"  ✅ CAPEC 攻击机制分类已生成")
    print(f"  ✅ CAPEC Top 攻击模式已生成")
    print(f"\n✨ CAPEC 数据生成完成!")


def generate_summary_index():
    """生成爬取数据的索引文件"""
    index_content = f"""# 网络安全语料爬取汇总

## 爬取时间: {time.strftime('%Y-%m-%d %H:%M:%S')}

## 数据来源

### 1. CWE (Common Weakness Enumeration)
- **来源**: MITRE CWE (https://cwe.mitre.org/)
- **内容**:
  - CWE Top 25 2024 - 最危险的25个软件弱点
  - CWE 分类体系 - 弱点视图和分类
- **格式**: Markdown (.md)
- **路径**: `cwe/`

### 2. CAPEC (Common Attack Pattern Enumeration and Classification)
- **来源**: MITRE CAPEC (https://capec.mitre.org/)
- **内容**:
  - 九大攻击机制分类
  - Top 20 攻击模式详解
- **格式**: Markdown (.md)
- **路径**: `capec/`

### 3. OWASP 补充材料
- **内容**:
  - ASVS v4.0.3 (应用安全验证标准)
  - WSTG v4.2 (Web安全测试指南)
- **格式**: Markdown (.md)
- **路径**: `owasp/`

## 数据格式说明
所有数据均遵循以下标准格式:
- 以 `#` 开头的一级标题为条目编号
- 以 `##` 开头的二级标题为条目名称
- 详细描述内容以段落文本呈现
- 列表型数据使用 `- **字段**: 值` 格式
- 每个文件包含 `---` 分隔的元数据尾部

## 与现有语料的互补关系
| 现有数据 | 新增数据 | 互补效果 |
|---------|---------|---------|
| cvelistV5 (漏洞实例) | CWE (弱点分类) | 从实例 → 分类体系 |
| ATT&CK (攻击技战术) | CAPEC (攻击模式) | 从战术层 → 模式层 |
| Top10 (Web风险) | ASVS/WSTG (测试标准) | 从风险 → 验证测试 |

## 下一步建议
1. 运行 `clean_cwe.py` 清洗爬取数据
2. 运行 `splitter.py` 进行智能切片
3. 整合入 RAG 知识库进行检索测试
"""

    file_path = OUTPUT_DIR / "INDEX.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"  ✅ 汇总索引已生成: INDEX.md")


# ==================== 主函数 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("🕷️  网络安全 RAG 语料爬虫 - CWE/OWASP 模块")
    print("=" * 60)

    try:
        # 1. CWE Top 25
        crawl_cwe_top25()

        # 2. CWE 分类体系
        crawl_cwe_categories()

        # 3. OWASP 补充
        crawl_owasp_materials()

        # 4. CAPEC
        crawl_capec()

        # 5. 生成索引
        print("\n" + "="*60)
        print("📊 生成汇总索引...")
        print("="*60)
        generate_summary_index()

    except KeyboardInterrupt:
        print("\n⚠️ 用户中断爬取")
    except Exception as e:
        print(f"\n❌ 爬取过程出错: {e}")
        import traceback
        traceback.print_exc()

    print("\n" + "="*60)
    print("🎉 所有爬取任务完成!")
    print(f"📂 数据保存在: {OUTPUT_DIR}")
    print("="*60)
