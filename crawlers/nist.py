"""
NIST CSF & NVD 爬虫
数据来源: NIST Cybersecurity Framework + NVD API + CISA Known Exploited Vulnerabilities
输出格式: 结构化 Markdown
"""
import requests
import json
import os
import time
import sys
from pathlib import Path
from crawlers import CRAWLED_DIR
from datetime import datetime, timedelta

# ==================== 配置区 ====================
OUTPUT_DIR = CRAWLED_DIR / "nist"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

REQUEST_DELAY = 2.0  # NVD API 限制: 每6秒最多1次(无API key), 有key可提升
NVD_API_KEY = ""  # 如有 NVD API Key 请填入, 可提升请求频率

# NVD API 基础 URL
NVD_API_BASE = "https://services.nvd.nist.gov/rest/json/cves/2.0"

# ==================== NIST CSF 核心内容 ====================

NIST_CSF_2_0 = {
    "title": "NIST Cybersecurity Framework (CSF) 2.0",
    "version": "2.0",
    "published": "2024-02-26",
    "organization": "National Institute of Standards and Technology (NIST)",
    "govern": {
        "name": "GOVERN (治理)",
        "id": "GV",
        "description": "建立和监控组织的网络安全风险管理策略、期望和政策。治理为安全活动提供方向，确保与组织使命和利益相关者需求一致。",
        "categories": {
            "GV.OC": {
                "name": "Organizational Context (组织环境)",
                "description": "理解组织的使命、利益相关者期望、法律监管要求和风险偏好，以指导网络安全风险管理。"
            },
            "GV.RM": {
                "name": "Risk Management Strategy (风险管理策略)",
                "description": "建立、沟通和监控组织的网络安全风险管理策略，包括角色、职责和问责制度。"
            },
            "GV.SC": {
                "name": "Cybersecurity Supply Chain Risk Management (供应链风险管理)",
                "description": "识别、评估和管理与第三方供应商、服务提供商和合作伙伴相关的网络安全风险。"
            },
            "GV.RR": {
                "name": "Roles, Responsibilities, and Authorities (角色职责与权限)",
                "description": "明确网络安全相关的角色、职责和权限，确保问责制和有效的决策。"
            },
            "GV.PO": {
                "name": "Policies, Processes, and Procedures (政策流程与程序)",
                "description": "建立、维护和传达网络安全政策、流程和程序，以支持风险管理策略的执行。"
            },
            "GV.OV": {
                "name": "Oversight (监督)",
                "description": "定期审查和评估网络安全风险管理活动，确保持续改进和与组织目标的协调。"
            }
        }
    },
    "identify": {
        "name": "IDENTIFY (识别)",
        "id": "ID",
        "description": "识别和记录组织当前的网络安全风险，包括资产、业务流程、供应商和相关威胁。",
        "categories": {
            "ID.AM": {
                "name": "Asset Management (资产管理)",
                "description": "识别和管理支持业务目标的数据、人员、设备、系统和设施，使其与网络安全风险重要性一致。"
            },
            "ID.RA": {
                "name": "Risk Assessment (风险评估)",
                "description": "理解组织运营、资产和个人的网络安全风险，包括威胁、漏洞、影响和可能性评估。"
            },
            "ID.IM": {
                "name": "Improvement (改进)",
                "description": "识别组织网络安全风险管理活动和结果的改进机会，推动持续优化。"
            }
        }
    },
    "protect": {
        "name": "PROTECT (保护)",
        "id": "PR",
        "description": "实施防护措施以防止潜在的网络安全事件，确保关键服务的韧性。",
        "categories": {
            "PR.AA": {
                "name": "Identity Management, Authentication and Access Control (身份管理与访问控制)",
                "description": "限制对物理和逻辑资产的访问，确保只有授权用户、服务、系统和设备可以访问。"
            },
            "PR.AT": {
                "name": "Awareness and Training (意识与培训)",
                "description": "为人员提供必要的网络安全意识和技能培训，使其能够履行职责并应对威胁。"
            },
            "PR.DS": {
                "name": "Data Security (数据安全)",
                "description": "确保信息在存储、传输和处理过程中的机密性、完整性和可用性 (CIA)。"
            },
            "PR.PS": {
                "name": "Platform Security (平台安全)",
                "description": "确保硬件、软件（固件、操作系统、应用）和服务的安全配置和管理。"
            },
            "PR.IR": {
                "name": "Technology Infrastructure Resilience (技术基础设施韧性)",
                "description": "设计和维护具有弹性的技术架构，确保系统能够承受和从攻击中恢复。"
            }
        }
    },
    "detect": {
        "name": "DETECT (检测)",
        "id": "DE",
        "description": "及时发现潜在的网络安全事件，通过持续监控和分析识别异常和攻击。",
        "categories": {
            "DE.CM": {
                "name": "Continuous Monitoring (持续监控)",
                "description": "持续监控网络、系统、应用和服务，发现异常的网络安全事件和其他潜在威胁。"
            },
            "DE.AE": {
                "name": "Adverse Event Analysis (异常事件分析)",
                "description": "分析检测到的异常和警报警示，识别潜在的网络安全事件，区分真实威胁和误报。"
            }
        }
    },
    "respond": {
        "name": "RESPOND (响应)",
        "id": "RS",
        "description": "对检测到的网络安全事件采取行动，控制和减轻事件影响。",
        "categories": {
            "RS.MA": {
                "name": "Incident Management (事件管理)",
                "description": "实施事件响应计划，协调响应活动，与内外利益相关者沟通，确保有效的事件处理。"
            },
            "RS.AN": {
                "name": "Incident Analysis (事件分析)",
                "description": "调查和取证，确定事件的范围、影响和根本原因，指导后续恢复和预防措施。"
            },
            "RS.MI": {
                "name": "Incident Response, Reporting, and Communication (事件报告与沟通)",
                "description": "按照法规和组织政策要求，及时报告网络安全事件并保持透明沟通。"
            }
        }
    },
    "recover": {
        "name": "RECOVER (恢复)",
        "id": "RC",
        "description": "从网络安全事件中恢复，恢复正常运营，并从中吸取经验教训。",
        "categories": {
            "RC.RP": {
                "name": "Incident Recovery Plan Execution (事件恢复计划执行)",
                "description": "执行恢复计划，确保系统、数据和服务的及时恢复，最小化停机时间。"
            },
            "RC.CO": {
                "name": "Incident Recovery Communication (事件恢复沟通)",
                "description": "与内部和外部利益相关者沟通恢复进度，协调恢复活动。"
            }
        }
    }
}

# NIST 800-53 控制家族
NIST_800_53_FAMILIES = {
    "AC": {
        "name": "Access Control (访问控制)",
        "description": "限制信息系统对授权用户、代表授权用户的进程或设备的访问，以及这些授权用户被允许执行的操作类型。"
    },
    "AT": {
        "name": "Awareness and Training (意识与培训)",
        "description": "确保管理人员和用户了解与他们的活动相关的安全风险，以及适用的政策、标准和程序。"
    },
    "AU": {
        "name": "Audit and Accountability (审计与问责)",
        "description": "创建、保护并保留信息系统审计记录，使其能够监控、分析、调查和报告非法的或非授权的系统活动。"
    },
    "CA": {
        "name": "Assessment, Authorization, and Monitoring (评估、授权与监控)",
        "description": "定期评估安全控制措施的有效性，并对信息系统进行授权。"
    },
    "CM": {
        "name": "Configuration Management (配置管理)",
        "description": "建立和维护信息系统和产品的基线配置，控制变更，并记录配置变更。"
    },
    "CP": {
        "name": "Contingency Planning (应急计划)",
        "description": "通过计划、程序和技术措施，确保信息系统在紧急情况下的持续运行。"
    },
    "IA": {
        "name": "Identification and Authentication (标识与认证)",
        "description": "识别用户、进程或设备，并验证其身份，然后才允许访问信息系统。"
    },
    "IR": {
        "name": "Incident Response (事件响应)",
        "description": "建立对信息安全事件的运营层面的响应能力，包括准备、检测、分析、遏制、恢复和用户响应活动。"
    },
    "MA": {
        "name": "Maintenance (维护)",
        "description": "对组织信息系统进行例行维护和修复，确保安全控制措施持续有效运行。"
    },
    "MP": {
        "name": "Media Protection (介质保护)",
        "description": "保护信息系统介质（纸质和数字），限制仅授权用户访问介质上的信息，并对介质进行安全销毁或净化。"
    },
    "PE": {
        "name": "Physical and Environmental Protection (物理与环境安全)",
        "description": "限制对信息系统、设备和相应操作环境的物理访问，保护免受物理和环境威胁。"
    },
    "PL": {
        "name": "Planning (规划)",
        "description": "制定、记录、更新和实施安全计划，描述系统安全需求和运维环境。"
    },
    "PM": {
        "name": "Program Management (项目管理)",
        "description": "在整个组织层面管理信息安全项目，为信息系统安全控制提供全组织视角。"
    },
    "PS": {
        "name": "Personnel Security (人员安全)",
        "description": "确保人员（包括第三方服务提供商）可靠可信，满足既定的安全标准和政策。"
    },
    "PT": {
        "name": "PII Processing and Transparency (个人信息处理与透明度)",
        "description": "确保组织以透明的方式处理 PII，并向个人提供有关 PII 处理活动的信息。"
    },
    "RA": {
        "name": "Risk Assessment (风险评估)",
        "description": "评估组织运营和资产的风险，包括威胁、漏洞、可能性和影响。"
    },
    "SA": {
        "name": "System and Services Acquisition (系统与服务获取)",
        "description": "在获取信息系统和服务时，确保安全需求被考虑并纳入合同和开发流程。"
    },
    "SC": {
        "name": "System and Communications Protection (系统与通信保护)",
        "description": "监控、控制和保护在信息系统内部和外部传输的通信。"
    },
    "SI": {
        "name": "System and Information Integrity (系统与信息完整性)",
        "description": "识别、报告并纠正信息和信息系统的缺陷，保护其免受恶意代码的攻击和未经授权的修改。"
    },
    "SR": {
        "name": "Supply Chain Risk Management (供应链风险管理)",
        "description": "管理信息系统、组件和服务的供应链风险，防止供应过程中的篡改、仿冒和恶意插入。"
    }
}


def generate_nist_csf_markdown():
    """生成 NIST CSF 2.0 结构化 Markdown"""
    csf = NIST_CSF_2_0

    md = f"""# {csf['title']}
## NIST 网络安全框架 v{csf['version']}

### 基本信息
- **发布机构**: {csf['organization']}
- **发布版本**: v{csf['version']}
- **发布日期**: {csf['published']}
- **框架类型**: 网络安全风险管理框架

### 概述
NIST 网络安全框架 (CSF) 2.0 是理解和降低网络安全风险的标准化指南框架。
它由六个核心功能 (Functions) 组成：治理 (Govern)、识别 (Identify)、保护 (Protect)、
检测 (Detect)、响应 (Respond) 和恢复 (Recover)，涵盖了网络安全风险管理的完整生命周期。

---
"""

    for func_key, func_data in [
        ("govern", csf["govern"]),
        ("identify", csf["identify"]),
        ("protect", csf["protect"]),
        ("detect", csf["detect"]),
        ("respond", csf["respond"]),
        ("recover", csf["recover"]),
    ]:
        md += f"""
## {func_data['name']} ({func_data['id']})

### 功能概述
{func_data['description']}

### 分类 (Categories)

"""
        for cat_key, cat_data in func_data["categories"].items():
            md += f"""#### {cat_key}: {cat_data['name']}
{cat_data['description']}

"""

        md += "---\n"

    md += f"""
---
*数据来源: NIST Cybersecurity Framework 2.0*
*发布日期: 2024-02-26*
*处理时间: {time.strftime('%Y-%m-%d %H:%M:%S')}*
"""
    return md


def generate_nist_800_53_markdown():
    """生成 NIST 800-53 控制家族结构化 Markdown"""
    md = """# NIST SP 800-53 Rev. 5
## 信息系统和组织的安全与隐私控制

### 概述
NIST Special Publication 800-53 Rev. 5 提供了全面的安全和隐私控制目录，
用于保护信息系统和组织运营，是美国联邦信息系统安全的基础标准。

### 控制家族总览
SP 800-53 包含 20 个控制家族，涵盖从访问控制到供应链风险管理的完整安全控制体系。

---

"""

    for family_id, family_data in NIST_800_53_FAMILIES.items():
        md += f"""
## {family_id}: {family_data['name']}

### 控制目标
{family_data['description']}

---

"""

    md += f"""
---
*数据来源: NIST Special Publication 800-53 Rev. 5*
*处理时间: {time.strftime('%Y-%m-%d %H:%M:%S')}*
"""
    return md


def generate_cisa_kev():
    """生成 CISA Known Exploited Vulnerabilities 数据"""
    md = """# CISA Known Exploited Vulnerabilities (KEV) 目录
## 已知被利用的漏洞目录

### 概述
CISA（美国网络安全和基础设施安全局）维护的已知被利用漏洞目录，
收录了在实际攻击中被证实有活跃利用的漏洞。这是漏洞优先级管理的重要参考。

### 关键特征
- 收录的漏洞均有证据表明在野外被活跃利用
- 联邦机构必须在指定时间内修复
- 可作为漏洞管理优先级排序的重要依据

### 主要漏洞类别

#### 1. 远程代码执行 (RCE)
- 允许攻击者通过网络远程执行任意代码
- 通常影响最大，修复优先级最高
- 示例：Log4Shell (CVE-2021-44228)、ProxyShell (CVE-2021-34473)

#### 2. 权限提升 (Privilege Escalation)
- 允许低权限用户获取更高权限
- 常与RCE漏洞组合使用
- 示例：Windows Print Spooler (CVE-2021-34527)

#### 3. 认证绕过 (Authentication Bypass)
- 绕过身份验证机制获取未授权访问
- 可导致数据泄露或系统控制
- 示例：CVE-2021-40539

#### 4. 信息泄露 (Information Disclosure)
- 导致敏感信息未经授权地暴露
- 可能成为进一步攻击的跳板
- 示例：ProxyLogon (CVE-2021-26855)

### 漏洞管理建议
1. **建立资产清单**: 了解环境中运行的所有软件和硬件
2. **自动化扫描**: 持续扫描KEV中的漏洞
3. **优先级排序**: 根据CVSS评分和利用活跃度确定修复顺序
4. **补丁管理**: 建立及时部署安全补丁的流程
5. **缓解措施**: 对无法立即修补的漏洞实施补偿控制

### 参考链接
- CISA KEV 目录: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA BOD 22-01: https://www.cisa.gov/binding-operational-directive-22-01

---
*数据来源: CISA Known Exploited Vulnerabilities Catalog*
*生成时间: """ + time.strftime('%Y-%m-%d %H:%M:%S') + """*
"""
    return md


def fetch_nvd_recent_cves(days_back=7, limit=20):
    """从 NVD API 获取最近的 CVE 数据"""
    print(f"  正在从 NVD API 获取最近 {days_back} 天的 CVE 数据...")

    # 构建查询: 最近N天发布的CVE
    pub_end_date = datetime.utcnow()
    pub_start_date = pub_end_date - timedelta(days=days_back)

    params = {
        "pubStartDate": pub_start_date.strftime("%Y-%m-%dT%H:%M:%S.000"),
        "pubEndDate": pub_end_date.strftime("%Y-%m-%dT%H:%M:%S.000"),
        "resultsPerPage": min(limit, 20),
    }

    headers = {"User-Agent": "RAG-CyberSecurity-Collector/1.0"}
    if NVD_API_KEY:
        headers["apiKey"] = NVD_API_KEY
        params["resultsPerPage"] = min(limit, 100)

    try:
        time.sleep(REQUEST_DELAY)
        resp = requests.get(NVD_API_BASE, params=params, headers=headers, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        vulnerabilities = data.get("vulnerabilities", [])
        print(f"  📊 获取到 {len(vulnerabilities)} 个近期 CVE")

        return vulnerabilities

    except Exception as e:
        print(f"  ⚠️ NVD API 请求失败: {e}")
        return []


def nvd_cve_to_markdown(vuln_data) -> str:
    """将 NVD JSON 格式转换为标准化 Markdown"""
    cve = vuln_data.get("cve", {})
    cve_id = cve.get("id", "未知")

    descriptions = cve.get("descriptions", [])
    desc_en = ""
    for d in descriptions:
        if d.get("lang") == "en":
            desc_en = d.get("value", "")
            break

    # CVSS 评分
    metrics = cve.get("metrics", {})
    cvss_v31 = metrics.get("cvssMetricV31", [{}])
    cvss_v30 = metrics.get("cvssMetricV30", [{}])
    cvss_v2 = metrics.get("cvssMetricV2", [{}])

    base_score = None
    severity = "未知"
    for cvss_list in [cvss_v31, cvss_v30, cvss_v2]:
        if cvss_list:
            cvss_data = cvss_list[0].get("cvssData", {})
            base_score = cvss_data.get("baseScore")
            severity = cvss_data.get("baseSeverity", "")
            if base_score:
                break

    # CWE
    weaknesses = cve.get("weaknesses", [])
    cwe_ids = []
    for w in weaknesses:
        for d in w.get("description", []):
            if d.get("value"):
                cwe_ids.append(d.get("value"))

    md = f"""# 漏洞编号: {cve_id}

### 漏洞描述
{desc_en.strip() if desc_en else '暂无描述'}

### 风险评估
- **CVSS 评分**: {base_score if base_score else '暂无评分'}
- **严重等级**: {severity}

### 关联弱点类型 (CWE)
{', '.join(cwe_ids) if cwe_ids else '未分类'}

---
*数据来源: NVD (National Vulnerability Database)*
*获取时间: {time.strftime('%Y-%m-%d %H:%M:%S')}*
"""
    return md


def crawl_nist():
    """主控函数: 爬取 NIST 相关数据"""
    print("\n" + "="*60)
    print("🔍 开始生成 NIST 网络安全标准框架数据...")
    print("="*60)

    nist_dir = OUTPUT_DIR

    # 1. NIST CSF 2.0
    print("\n  📝 生成 NIST CSF 2.0 框架文档...")
    csf_md = generate_nist_csf_markdown()
    with open(nist_dir / "NIST_CSF_2.0_Framework.md", "w", encoding="utf-8") as f:
        f.write(csf_md)
    print("  ✅ NIST CSF 2.0 已生成")

    # 2. NIST 800-53
    print("\n  📝 生成 NIST SP 800-53 控制文档...")
    sp80053_md = generate_nist_800_53_markdown()
    with open(nist_dir / "NIST_SP800-53_Rev5.md", "w", encoding="utf-8") as f:
        f.write(sp80053_md)
    print("  ✅ NIST SP 800-53 已生成")

    # 3. CISA KEV
    print("\n  📝 生成 CISA KEV 目录...")
    kev_md = generate_cisa_kev()
    with open(nist_dir / "CISA_KEV_Catalog.md", "w", encoding="utf-8") as f:
        f.write(kev_md)
    print("  ✅ CISA KEV 已生成")

    # 4. 尝试从 NVD API 获取近期 CVE
    print("\n  🔄 尝试获取 NVD 近期漏洞数据...")
    recent_cves = fetch_nvd_recent_cves(days_back=30, limit=50)

    if recent_cves:
        nvd_dir = nist_dir / "nvd_recent"
        nvd_dir.mkdir(parents=True, exist_ok=True)
        for vuln in recent_cves:
            cve_id = vuln.get("cve", {}).get("id", "unknown")
            md_content = nvd_cve_to_markdown(vuln)
            with open(nvd_dir / f"cleaned_{cve_id}.md", "w", encoding="utf-8") as f:
                f.write(md_content)
        print(f"  ✅ 已保存 {len(recent_cves)} 个近期 CVE")
    else:
        print("  ⚠️ 无法从 NVD 获取近期数据，仅生成了框架文档")

    print(f"\n✨ NIST 数据采集完成!")


# 生成 ISO 27001 对照框架
def generate_iso27001_framework():
    """生成 ISO 27001 标准框架"""
    iso_controls = {
        "A.5": "信息安全策略 (Information Security Policies)",
        "A.6": "信息安全组织 (Organization of Information Security)",
        "A.7": "人力资源安全 (Human Resource Security)",
        "A.8": "资产管理 (Asset Management)",
        "A.9": "访问控制 (Access Control)",
        "A.10": "密码学 (Cryptography)",
        "A.11": "物理和环境安全 (Physical and Environmental Security)",
        "A.12": "操作安全 (Operations Security)",
        "A.13": "通信安全 (Communications Security)",
        "A.14": "系统获取、开发和维护 (System Acquisition, Development and Maintenance)",
        "A.15": "供应商关系 (Supplier Relationships)",
        "A.16": "信息安全事件管理 (Information Security Incident Management)",
        "A.17": "业务连续性管理 (Business Continuity Management)",
        "A.18": "符合性 (Compliance)",
    }

    md = f"""# ISO/IEC 27001:2022
## 信息安全、网络安全和隐私保护 — 信息安全管理体系 — 要求

### 概述
ISO/IEC 27001 是国际标准化组织发布的信息安全管理体系 (ISMS) 标准。
它提供了建立、实施、维护和持续改进信息安全管理体系的框架。

### 标准控制域 (Annex A)

---
"""
    for control_id, control_name in iso_controls.items():
        md += f"""
## {control_id}: {control_name}

### 控制目标
确保在{control_name.split('(')[0].strip() if '(' in control_name else control_name}方面建立有效的信息安全管理措施。

---

"""

    md += f"""
### 与 NIST CSF 的互补关系
| ISO 27001 | NIST CSF | 说明 |
|-----------|----------|------|
| A.5 安全策略 | Govern | 政策治理 |
| A.8 资产管理 | Identify | 资产识别 |
| A.9 访问控制 | Protect | 保护控制 |
| A.12 操作安全 | Protect | 运营保护 |
| A.16 事件管理 | Respond | 事件响应 |
| A.17 业务连续性 | Recover | 恢复策略 |

---
*标准版本: ISO/IEC 27001:2022*
*生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}*
"""

    with open(OUTPUT_DIR / "ISO27001_2022_Framework.md", "w", encoding="utf-8") as f:
        f.write(md)
    print("  ✅ ISO 27001 框架已生成")


if __name__ == "__main__":
    print("=" * 60)
    print("🕷️  网络安全 RAG 语料爬虫 - NIST/标准模块")
    print("=" * 60)

    try:
        crawl_nist()
        print("\n" + "="*60)
        print("📝 生成 ISO 27001 框架...")
        generate_iso27001_framework()

    except KeyboardInterrupt:
        print("\n⚠️ 用户中断")
    except Exception as e:
        print(f"\n❌ 出错: {e}")
        import traceback
        traceback.print_exc()

    print("\n" + "="*60)
    print(f"🎉 NIST 数据采集完成! 数据保存在: {OUTPUT_DIR}")
    print("="*60)
