"""
中国网络安全标准与法规补充爬虫
数据来源: 中国网信办、公安部、国家标准化管理委员会的公开标准信息
+ OWASP Mobile Top 10 + LLM Security 等前沿安全内容
输出格式: 结构化 Markdown
"""
import requests
import json
import time
import re
from pathlib import Path
from crawlers import CRAWLED_DIR
from datetime import datetime

# ==================== 配置区 ====================
OUTPUT_DIR = CRAWLED_DIR / "china_standards"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

REQUEST_DELAY = 2.0

# ==================== 中国网络安全标准体系 ====================

# GB/T 国家标准 - 网络安全相关
GB_STANDARDS = {
    "等级保护 (等保2.0)": {
        "GB/T 22239-2019": {
            "name": "信息安全技术 网络安全等级保护基本要求",
            "english": "Information Security Technology - Baseline for Classified Protection of Cybersecurity",
            "level": "国家标准",
            "description": "规定了网络安全等级保护的基本安全要求，包括安全通用要求和安全扩展要求（云计算、移动互联、物联网、工业控制、大数据）。",
            "key_areas": ["安全物理环境", "安全通信网络", "安全区域边界", "安全计算环境", "安全管理中心", "安全管理制度"]
        },
        "GB/T 28448-2019": {
            "name": "信息安全技术 网络安全等级保护测评要求",
            "english": "Information Security Technology - Evaluation Requirements for Classified Protection of Cybersecurity",
            "description": "规定了网络安全等级保护测评的总体要求、测评指标和测评方法。"
        },
        "GB/T 25070-2019": {
            "name": "信息安全技术 网络安全等级保护安全设计技术要求",
            "english": "Information Security Technology - Technical Requirements of Security Design for Classified Protection of Cybersecurity",
            "description": "规定了网络安全等级保护安全设计的技术要求。"
        }
    },
    "数据安全": {
        "GB/T 37988-2019": {
            "name": "信息安全技术 数据安全能力成熟度模型",
            "english": "DSMM - Data Security Maturity Model",
            "description": "提供了组织数据安全能力成熟度模型的框架，涵盖数据采集、传输、存储、处理、交换和销毁全生命周期。",
            "maturity_levels": ["1级: 非正式执行", "2级: 计划跟踪", "3级: 充分定义", "4级: 量化控制", "5级: 持续优化"]
        },
        "GB/T 35273-2020": {
            "name": "信息安全技术 个人信息安全规范",
            "english": "Information Security Technology - Personal Information Security Specification",
            "description": "规定了个人信息收集、存储、使用、共享、转让和公开披露的安全要求和保护措施。"
        },
        "GB/T 39335-2020": {
            "name": "信息安全技术 个人信息安全影响评估指南",
            "english": "Information Security Technology - Personal Information Security Impact Assessment Guidelines",
            "description": "提供了个人信息安全影响评估的框架、流程和方法。"
        }
    },
    "关键信息基础设施": {
        "GB/T 39204-2020": {
            "name": "信息安全技术 关键信息基础设施安全保护要求",
            "english": "Information Security Technology - Security Protection Requirements for Critical Information Infrastructure",
            "description": "规定了关键信息基础设施安全保护的要求和措施。"
        },
        "GB/T 41400-2022": {
            "name": "信息安全技术 关键信息基础设施安全保护指标体系",
            "english": "Information Security Technology - Indicator System for Critical Information Infrastructure Security",
            "description": "建立了关键信息基础设施安全保护的指标体系。"
        }
    },
    "云计算安全": {
        "GB/T 31167-2023": {
            "name": "信息安全技术 云计算服务安全指南",
            "english": "Information Security Technology - Security Guide for Cloud Computing Services",
            "description": "提供了云计算服务安全能力的分类、评估和使用指南。"
        },
        "GB/T 31168-2023": {
            "name": "信息安全技术 云计算服务安全能力要求",
            "english": "Information Security Technology - Security Capability Requirements for Cloud Computing Services",
            "description": "规定了云计算服务提供商应具备的安全能力。"
        }
    },
    "密码安全": {
        "GB/T 39786-2021": {
            "name": "信息安全技术 信息系统密码应用基本要求",
            "english": "Information Security Technology - Basic Requirements for Cryptographic Application in Information Systems",
            "description": "规定了信息系统密码应用的基本要求，包括密码算法、密钥管理、密码产品和服务。"
        }
    }
}

# 中国网络安全法律法规体系
CHINA_LAW_SYSTEM = {
    "法律层面": {
        "《网络安全法》": {
            "生效日期": "2017-06-01",
            "修订日期": "2025-10-28",
            "核心内容": [
                "网络安全等级保护制度",
                "关键信息基础设施安全保护",
                "个人信息保护义务",
                "网络安全审查制度",
                "网络运营者安全义务",
                "监测预警与应急处置"
            ]
        },
        "《数据安全法》": {
            "生效日期": "2021-09-01",
            "核心内容": [
                "数据分类分级保护",
                "数据安全审查",
                "数据出口管制",
                "重要数据保护目录",
                "数据安全风险评估",
                "数据交易安全"
            ]
        },
        "《个人信息保护法》": {
            "生效日期": "2021-11-01",
            "核心内容": [
                "个人信息处理原则（合法、正当、必要、诚信）",
                "告知-同意规则",
                "敏感个人信息保护",
                "个人信息跨境提供规则",
                "个人在信息处理活动中的权利",
                "大型互联网平台义务"
            ]
        }
    },
    "行政法规层面": {
        "《关键信息基础设施安全保护条例》": {
            "生效日期": "2021-09-01",
            "核心内容": [
                "关键信息基础设施认定规则",
                "安全保护责任与措施",
                "安全检测评估",
                "网络安全信息共享"
            ]
        },
        "《网络安全审查办法》": {
            "生效日期": "2022-02-15",
            "核心内容": [
                "网络平台运营者赴国外上市审查",
                "关键信息基础设施运营者采购审查",
                "国家安全风险评估"
            ]
        },
        "《数据出境安全评估办法》": {
            "生效日期": "2022-09-01",
            "核心内容": [
                "数据出境安全评估触发条件",
                "评估流程与时限",
                "自评估与安全评估报告"
            ]
        }
    },
    "部门规章与规范性文件": {
        "《网络数据安全管理条例》": {
            "生效日期": "2025-01-01",
            "核心内容": [
                "数据分类分级",
                "重要数据处理",
                "个人信息保护",
                "数据安全评估与审查"
            ]
        },
        "《汽车数据安全管理若干规定(试行)》": {
            "生效日期": "2021-10-01",
            "核心内容": [
                "汽车数据处理原则",
                "车内座舱数据保护",
                "车外数据采集规范"
            ]
        },
        "《生成式人工智能服务管理暂行办法》": {
            "生效日期": "2023-08-15",
            "核心内容": [
                "训练数据合规要求",
                "AIGC内容标识",
                "安全评估与算法备案"
            ]
        }
    }
}


def generate_gb_standards_markdown():
    """生成中国 GB/T 标准体系 Markdown"""
    md = """# 中国网络安全国家标准体系 (GB/T)
## 信息安全技术标准族

### 概述
中国网络安全国家标准体系以《网络安全法》《数据安全法》《个人信息保护法》为上位法律依据，
由全国信息安全标准化技术委员会 (TC260) 组织制定，涵盖了从等保合规到数据安全治理的完整标准框架。

---
"""
    for category, standards in GB_STANDARDS.items():
        md += f"""
## {category}

"""
        for std_id, std_info in standards.items():
            md += f"""
### {std_id}: {std_info['name']}
- **英文名称**: {std_info.get('english', 'N/A')}
- **标准级别**: {std_info.get('level', '国家标准')}

**内容概述**: {std_info['description']}

"""
            if 'key_areas' in std_info:
                md += "**关键安全域**:\n"
                for area in std_info['key_areas']:
                    md += f"- {area}\n"
                md += "\n"

            if 'maturity_levels' in std_info:
                md += "**成熟度等级**:\n"
                for level in std_info['maturity_levels']:
                    md += f"- {level}\n"
                md += "\n"

        md += "---\n"

    md += f"""
---
*数据整理时间: {time.strftime('%Y-%m-%d %H:%M:%S')}*
*标准来源: 全国信息安全标准化技术委员会 (TC260)*
"""
    return md


def generate_law_system_markdown():
    """生成中国网络安全法规体系 Markdown"""
    md = """# 中国网络安全法律法规体系
## 法律 — 行政法规 — 部门规章 三级体系

### 概述
中国已初步形成了以《网络安全法》《数据安全法》《个人信息保护法》三部基础法律为核心，
配套行政法规和部门规章的网络安全法律体系。

---
"""
    for level, laws in CHINA_LAW_SYSTEM.items():
        md += f"""
## {level}

"""
        for law_name, law_info in laws.items():
            md += f"""
### {law_name}
"""
            if "修订日期" in law_info:
                md += f"- **生效日期**: {law_info['生效日期']}\n"
                md += f"- **修订日期**: {law_info['修订日期']}\n"
            else:
                md += f"- **生效日期**: {law_info['生效日期']}\n"

            md += "\n**核心内容**:\n"
            for item in law_info.get('核心内容', []):
                md += f"- {item}\n"

            md += "\n"

        md += "---\n"

    md += f"""
---
*数据整理时间: {time.strftime('%Y-%m-%d %H:%M:%S')}*
"""
    return md


def generate_classified_protection_mapping():
    """生成等保2.0与NIST/ISO对照表"""
    md = """# 等保2.0 与 NIST CSF / ISO 27001 对照表
## 国际网络安全框架映射

### 概述
中国等保2.0 (GB/T 22239-2019) 是强制性的网络安全合规框架。以下将其与国际主流框架进行对照映射，
便于跨国组织和研究人员理解和协调合规工作。

---

### 等保2.0 安全层面与 NIST CSF 映射

| 等保2.0 安全层面 | NIST CSF 功能 | ISO 27001 控制域 |
|----------------|--------------|-----------------|
| 安全物理环境 | Protect | A.11 物理和安全环境 |
| 安全通信网络 | Protect (PR.PS) | A.13 通信安全 |
| 安全区域边界 | Detect / Protect | A.12 操作安全 |
| 安全计算环境 | Protect | A.12 / A.14 |
| 安全管理中心 | Govern / Detect | A.5 / A.6 |
| 安全管理制度 | Govern | A.5 安全策略 |
| 安全管理人员 | Govern (GV.RR) | A.7 人力资源安全 |
| 安全建设管理 | Identify | A.14 系统获取开发 |
| 安全运维管理 | Detect / Respond | A.12 / A.16 |

### 等保2.0 等级与保护要求

| 等级 | 侵害客体 | 侵害程度 | 监管强度 | 对应保护要求 |
|-----|---------|---------|---------|------------|
| 第一级 | 公民、法人和其他组织 | 一般损害 | 自主保护 | 基本防护措施 |
| 第二级 | 公民、法人和其他组织 | 严重损害 | 指导保护 | 安全审计+身份鉴别 |
| 第三级 | 社会秩序和公共利益 | 特别严重损害 | 监督保护 | 强制访问控制+双因子认证 |
| 第四级 | 国家安全 | 特别严重损害 | 强制保护 | 结构化保护 |
| 第五级 | 国家安全 | 特别严重损害 | 专控保护 | 形式化验证保护 |

### 与 CMMI / DSMM 的成熟度关联

| 等保等级 | DSMM 等级 | 说明 |
|---------|----------|------|
| 第一级 | 1-2级 | 基础数据安全能力 |
| 第二级 | 2-3级 | 规范化数据安全管理 |
| 第三级 | 3-4级 | 充分定义且量化可控 |
| 第四级以上 | 4-5级 | 量化优化，持续改进 |

---
*编制时间: """ + time.strftime('%Y-%m-%d %H:%M:%S') + """*
"""
    return md


def generate_ai_security_framework():
    """生成 AI/LLM 安全框架"""
    md = """# AI 与 LLM 安全框架
## 生成式人工智能安全风险与缓解措施

### 概述
随着大语言模型 (LLM) 和生成式 AI 的快速普及，AI 安全已成为网络安全的重要组成部分。
本框架综合了 OWASP Top 10 for LLM Applications、中国《生成式人工智能服务管理暂行办法》
以及 NIST AI RMF 的核心内容。

---

### OWASP Top 10 for LLM Applications (2025)

#### LLM01: Prompt Injection (提示注入)
- **风险**: 攻击者通过精心构造的提示词绕过安全限制，操控 LLM 输出
- **影响**: 数据泄露、权限绕过、恶意行为触发
- **缓解**: 输入过滤、输出验证、权限最小化、沙箱隔离

#### LLM02: Sensitive Information Disclosure (敏感信息泄露)
- **风险**: LLM 在训练数据中学习了敏感信息后可能在输出中泄露
- **影响**: 个人隐私泄露、商业机密曝光
- **缓解**: 数据脱敏训练、输出过滤、差分隐私

#### LLM03: Supply Chain (供应链风险)
- **风险**: 第三方模型、数据集或插件的安全漏洞
- **影响**: 模型后门、恶意行为注入
- **缓解**: 供应链审查、模型签名验证、来源追踪

#### LLM04: Data and Model Poisoning (数据与模型投毒)
- **风险**: 训练数据或模型参数被恶意篡改
- **影响**: 模型行为异常、后门植入
- **缓解**: 数据来源验证、训练过程监控、模型完整性校验

#### LLM05: Improper Output Handling (输出处理不当)
- **风险**: LLM 输出直接被用于下游操作而未经验证
- **影响**: XSS、SQL注入、代码执行
- **缓解**: 输出验证、编码转义、沙箱执行

#### LLM06: Excessive Agency (过度自主权)
- **风险**: LLM 被授予过多自主执行能力
- **影响**: 非授权操作、系统破坏
- **缓解**: 功能权限最小化、人类审核环节、操作日志

#### LLM07: System Prompt Leakage (系统提示词泄露)
- **风险**: 攻击者诱导 LLM 泄露系统级别的提示词设置
- **影响**: 安全机制暴露、越狱攻击
- **缓解**: 提示词分层设计、监控泄露尝试

#### LLM08: Vector and Embedding Weaknesses (向量与嵌入弱点)
- **风险**: RAG 知识库的向量数据库安全漏洞
- **影响**: 数据污染、检索操控
- **缓解**: 向量数据访问控制、完整性校验

#### LLM09: Misinformation and Hallucination (错误信息与幻觉)
- **风险**: LLM 生成看似合理但事实错误的内容
- **影响**: 决策误导、声誉损害
- **缓解**: 事实核查、来源引用、置信度标注

#### LLM10: Unbounded Consumption (无界资源消耗)
- **风险**: LLM 被滥用以消耗大量计算资源
- **影响**: DoS、成本爆炸
- **缓解**: 速率限制、资源配额、输入长度限制

---

### 中国 AIGC 监管框架

| 法规要求 | 核心要点 | 对应风险 |
|---------|---------|---------|
| 训练数据合规 | 数据来源合法、不侵犯知识产权 | LLM03, LLM04 |
| 内容标识 | AIGC 内容必须标识 | LLM09 |
| 安全评估 | 上线前进行安全评估 | 全部 |
| 算法备案 | 算法需向监管部门备案 | LLM06 |
| 个人信息保护 | 训练数据中的个人信息保护 | LLM02 |

---
*编制时间: """ + time.strftime('%Y-%m-%d %H:%M:%S') + """*
"""
    return md


def generate_data_security_lifecycle():
    """生成数据安全全生命周期管理框架"""
    md = """# 数据安全全生命周期管理
## DSG (Data Security Governance) 框架

### 概述
数据安全是网络安全的核心组成部分。本框架综合 Gartner DSG、微软 DGPC 和中国 DSMM 的最佳实践，
覆盖数据从创建到销毁的全生命周期安全管控。

---

### 数据安全生命周期六阶段

#### 1. 数据采集 (Data Collection)
- **安全要求**:
  - 采集目的明确、合法、必要
  - 数据主体知情同意（符合个保法要求）
  - 数据分类分级标识
  - 数据源验证和完整性校验
- **关键控制**: 采集声明、同意管理、最少够用原则

#### 2. 数据传输 (Data Transmission)
- **安全要求**:
  - 传输通道加密 (TLS 1.2+)
  - 数据完整性验证
  - 跨境传输合规审查
  - 传输日志和审计
- **关键控制**: TLS/SSL、VPN、数据脱敏传输

#### 3. 数据存储 (Data Storage)
- **安全要求**:
  - 存储加密（文件级/数据库级）
  - 密钥生命周期管理
  - 介质安全与防泄漏
  - 备份与容灾
- **关键控制**: AES-256、HSM、DLP、冗余备份

#### 4. 数据处理 (Data Processing)
- **安全要求**:
  - 数据脱敏与匿名化
  - 最小权限访问控制
  - 处理环境隔离
  - 处理日志记录
- **关键控制**: 数据脱敏、RBAC、安全沙箱

#### 5. 数据交换 (Data Exchange)
- **安全要求**:
  - 数据共享审批流程
  - 数据水印与溯源
  - API 安全控制
  - 第三方安全评估
- **关键控制**: 数据水印、API 网关、审批工作流

#### 6. 数据销毁 (Data Destruction)
- **安全要求**:
  - 安全擦除标准 (DoD 5220.22-M)
  - 销毁证明和记录
  - 云端数据安全删除
  - 介质物理销毁
- **关键控制**: 安全擦除工具、销毁审计

---

### 数据分类分级模型

| 级别 | 标签 | 示例数据 | 保护要求 |
|-----|------|---------|---------|
| 1级 | 公开 | 产品文档、公开年报 | 基础保护 |
| 2级 | 内部 | 内部邮件、项目文档 | 访问控制 |
| 3级 | 机密 | 商业机密、核心算法 | 加密+审计 |
| 4级 | 绝密/重要数据 | 国家安全相关、重要民生数据 | 最高级保护 |

---
*参考框架: Gartner DSG、DSMM、DAMA-DMBOK*
*编制时间: """ + time.strftime('%Y-%m-%d %H:%M:%S') + """*
"""
    return md


def generate_cloud_security():
    """生成云安全矩阵"""
    md = """# 云安全责任共担模型与安全控制矩阵
## CSA (Cloud Security Alliance) 指导框架

### 概述
云安全采用责任共担模型 (Shared Responsibility Model)，云服务提供商 (CSP) 和云上用户分别承担不同层面的安全责任。

---

### 云安全责任共担模型

| 服务模型 | CSP 责任 | 用户责任 |
|---------|---------|---------|
| IaaS | 物理设施、网络、虚拟化层安全 | OS、中间件、应用、数据、IAM |
| PaaS | 物理设施、网络、虚拟化、OS、运行时 | 应用、数据、IAM、API安全 |
| SaaS | 物理设施到应用层的全栈安全 | 数据、IAM、安全配置 |

---

### CSA 云计算关键领域安全指南 v4.0

#### 领域1: 治理和企业风险管理
- 云治理框架、风险评估、合规映射
- 云服务提供商尽职调查

#### 领域2: 法律问题：合同与电子发现
- 云合同条款审查
- 数据主权与跨境数据传输
- 电子发现 (e-Discovery) 能力

#### 领域3: 合规和审计管理
- 合规框架映射 (等保/ISO/SOC)
- 持续合规监控
- 审计权力与透明度

#### 领域4: 信息治理
- 数据分类分级
- 数据生命周期管理
- 数据所有权和管理权

#### 领域5: 管理平面与业务连续性
- 云管理控制台安全
- 业务连续性和灾难恢复计划

#### 领域6: 基础设施安全
- 网络虚拟化和微分段
- 安全基线配置 (CIS Benchmarks)
- 容器和 Serverless 安全

#### 领域7: 虚拟化和容器安全
- 虚拟机逃逸防护
- 容器镜像安全扫描
- Kubernetes 安全配置

#### 领域8: 事件响应、通知和补救
- 云环境事件响应计划
- CSP 通知义务
- 取证数据获取

#### 领域9: 应用安全
- 安全软件开发生命周期 (SSDLC)
- WAAP (Web Application and API Protection)
- DevSecOps 实践

#### 领域10: 数据安全和加密
- BYOK (Bring Your Own Key)
- 传输和存储加密策略
- 数据防泄漏 (DLP)

#### 领域11: IAM (身份、权限与访问管理)
- 联合身份 (Federated Identity)
- 多因素认证 (MFA)
- 特权访问管理 (PAM)

#### 领域12: 安全即服务 (Security as a Service)
- SECaaS 分类 (SIEM、WAF、IDS等)
- 第三方安全工具的云部署

#### 领域13: 新兴技术安全
- AI/ML 安全
- IoT 安全
- 量子计算安全

---
*参考: CSA Security Guidance v4.0, NIST SP 800-144*
*编制时间: """ + time.strftime('%Y-%m-%d %H:%M:%S') + """*
"""
    return md


def crawl_all():
    """执行所有标准框架文档生成"""
    print("=" * 60)
    print("🕷️  中国网络安全标准 + 国际前沿安全框架数据生成")
    print("=" * 60)

    generators = [
        ("中国 GB/T 标准体系", "GB_Standards_Catalog.md", generate_gb_standards_markdown),
        ("中国网络安全法规体系", "China_CyberLaw_System.md", generate_law_system_markdown),
        ("等保2.0对照表", "Equal_Protection_2.0_Mapping.md", generate_classified_protection_mapping),
        ("AI/LLM 安全框架", "AI_LLM_Security_Framework.md", generate_ai_security_framework),
        ("数据安全全生命周期", "Data_Security_Lifecycle.md", generate_data_security_lifecycle),
        ("云安全责任矩阵", "Cloud_Security_Matrix.md", generate_cloud_security),
    ]

    for name, filename, generator in generators:
        print(f"\n  📝 生成: {name}...")
        try:
            content = generator()
            file_path = OUTPUT_DIR / filename
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✅ 已保存: {filename} ({len(content)} 字符)")
        except Exception as e:
            print(f"  ❌ 生成失败: {e}")


def generate_index():
    """生成爬取数据索引"""
    index = f"""# 网络安全标准与法规语料 — 补充模块索引

## 生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}

## 目录

### 中国网络安全标准
1. **GB_Standards_Catalog.md** — 中国网络安全国家标准体系
   - 等保2.0 (GB/T 22239/28448/25070)
   - 数据安全标准 (DSMM/个人信息安全规范)
   - 关键信息基础设施标准
   - 云计算安全标准
   - 密码安全标准

2. **China_CyberLaw_System.md** — 中国网络安全法律法规体系
   - 法律层面: 网安法、数安法、个保法
   - 行政法规: 关基条例、审查办法
   - 部门规章: 网络数据安全管理条例等

3. **Equal_Protection_2.0_Mapping.md** — 等保2.0 国际框架对照表
   - 等保与NIST CSF映射
   - 等保与ISO 27001映射
   - 成熟度等级对照

### 前沿安全框架
4. **AI_LLM_Security_Framework.md** — AI与LLM安全
   - OWASP Top 10 for LLM Applications 2025
   - 中国AIGC监管框架
   - 风险缓解措施

5. **Data_Security_Lifecycle.md** — 数据安全全生命周期管理
   - 六大阶段安全控制
   - 数据分类分级模型
   - 国际框架综合

6. **Cloud_Security_Matrix.md** — 云安全矩阵
   - 责任共担模型
   - CSA 13领域安全指南
   - 多云/混合云安全

## 与现有语料的关系
| 现有语料 | 本模块补充 | 互补效果 |
|---------|-----------|---------|
| 网络安全法/doxc | 法规体系全景图 | 从条文 → 体系 |
| CVE/cvelistV5 | DSMM生命周期 | 从漏洞 → 数据治理 |
| ATT&CK技战术 | AI/LLM安全 | 从传统攻击 → AI风险 |
| — | 等保2.0框架 | 新增合规维度 |
| — | 云安全矩阵 | 新增基础设施维度 |

## 后续处理建议
1. 使用 text/爬虫/ 下的爬虫补充在线实时数据
2. 运行 tool/ 下的清洗脚本统一格式
3. 使用 tool/splitter.py 智能切片
4. 导入向量数据库进行RAG检索测试
"""
    file_path = OUTPUT_DIR / "INDEX.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(index)
    print(f"\n  ✅ 索引已生成: INDEX.md")


if __name__ == "__main__":
    try:
        crawl_all()
        print("\n" + "="*60)
        generate_index()
    except KeyboardInterrupt:
        print("\n⚠️ 用户中断")
    except Exception as e:
        print(f"\n❌ 出错: {e}")
        import traceback
        traceback.print_exc()

    print("\n" + "="*60)
    print(f"🎉 标准法规数据生成完成! 数据保存在: {OUTPUT_DIR}")
    print("="*60)
