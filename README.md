# TrustGuard Crawler

面向网络安全领域的 RAG 语料采集与预处理工具。从多个权威数据源爬取、清洗并切分安全知识文档，生成可供 LLM 安全应用直接使用的检索就绪文本。

## 数据源

| 数据源 | 说明 | 格式 |
|---|---|---|
| NVD（美国国家漏洞数据库） | 含 CVSS 评分的最新 CVE | API → Markdown |
| MITRE CWE Top 25 2024 | 常见弱点枚举 | API → Markdown |
| MITRE CAPEC | 攻击模式分类 | 本地 → Markdown |
| MITRE ATT&CK | 对抗战术与技术 | STIX → Markdown |
| CISA KEV | 已知被利用漏洞目录 | Feed → Markdown |
| OWASP Top 10 | Web 应用安全风险 | Markdown |
| OWASP ASVS / WSTG | 验证与测试标准 | 本地 → Markdown |
| NIST CSF 2.0 / SP 800-53 | 安全框架 | 本地 → Markdown |
| ISO/IEC 27001:2022 | 信息安全管理体系标准 | 本地 → Markdown |
| 中国国家标准（GB） | 国家网络安全标准 | 本地 → Markdown |
| cvelistV5 | 完整 CVE 归档（1999–2026） | JSON → Markdown |
| 互联网搜索 | 基于关键词的安全资讯/文章 | DuckDuckGo API |

## 项目结构

```
trustguard-crawler/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── crawlers/                       # 数据采集脚本
│   ├── cwe_crawler.py              #   CWE Top 25 / CAPEC / OWASP
│   ├── nist_crawler.py             #   NIST CSF / SP 800-53 / ISO 27001
│   ├── china_standards_crawler.py  #   中国国标及法规
│   ├── live_crawler.py             #   NVD 最新 CVE / CISA KEV
│   ├── internet_crawler.py         #   DuckDuckGo 关键词搜索
│   └── consolidate.py              #   合并所有输出为 RAG 语料
│
├── scripts/                        # 预处理管线
│   ├── clean_owasp.py              #   清洗 OWASP Markdown
│   ├── clean_attck.py              #   转换 ATT&CK STIX → Markdown
│   ├── clean_cve.py                #   转换 CVE JSON → Markdown
│   └── splitter.py                 #   将清洗后文档切分为 RAG 块
│
├── doc/                            # 原始文档（按来源组织）
│   ├── crawled/                    #   爬虫输出（项目生成）
│   ├── owasp/                      #   OWASP Top 10（2017/2021/2025）
│   ├── cve/                        #   cvelistV5 归档
│   └── attck/                      #   MITRE ATT&CK STIX 数据
│
├── data-sample/                    # CVE 验证数据集样本
│
├── clean/                          # 清洗后的 Markdown 输出（gitignore）
└── chunks/                         # 切分后的文本块输出（gitignore）
```

## 快速开始

### 环境要求

- Python 3.9+
- Docker（用于 data-sample 中的 CVE 验证）

### 安装

```bash
pip install -r requirements.txt
```

### 采集安全数据

```bash
# CWE Top 25、CAPEC、OWASP 相关资料
python crawlers/cwe_crawler.py

# NIST 框架、NVD 最新 CVE
python crawlers/nist_crawler.py

# 中国国家标准与法规
python crawlers/china_standards_crawler.py

# NVD + CISA KEV 实时 CVE 数据
python crawlers/live_crawler.py

# 互联网关键词搜索
python crawlers/internet_crawler.py

# 合并所有爬虫输出
python crawlers/consolidate.py
```

### RAG 预处理

```bash
# 清洗 OWASP Markdown（去除前言、HTML 等）
python scripts/clean_owasp.py \
    --input doc/owasp/Top10-master/2017/en \
    --output clean/owasp/2017/en

# 转换 ATT&CK STIX 为 Markdown
python scripts/clean_attck.py

# 转换 CVE JSON 为 Markdown
python scripts/clean_cve.py \
    --input doc/cve/cvelistV5-main/cves/2026 \
    --output clean/cve/2026

# 将清洗后文档切分为检索块
python scripts/splitter.py \
    --input clean/owasp/2017/en \
    --output chunks/owasp/2017/en
```

所有脚本支持 `--help` 查看完整用法。

### 数据样本（CVE 验证）

`data-sample/` 目录包含 3 个项目共 8 个 CVE 的 Docker 化验证环境：

| 项目 | 语言 | CVE |
|---|---|---|
| caddy | Go | CVE-2026-27587、CVE-2026-27588、CVE-2026-30851 |
| cms（Kirby/Craft） | PHP | CVE-2025-30207、CVE-2025-31493、CVE-2025-35939 |
| saleor | Python | CVE-2026-22849、CVE-2026-24136 |

详见 `data-sample/README.md`。

## RAG 语料统计

| 指标 | 数值 |
|---|---|
| 总条目数 | 114 |
| 总字符数 | ~303K |
| 数据源 | 7 |
| 分类数 | 8 |

## 增量更新

- **每日**：运行 `live_crawler.py` 和 `internet_crawler.py` 获取最新 CVE 和资讯
- **每周**：运行 `cwe_crawler.py` 获取 CWE Top 25 更新
- **按需**：运行 `china_standards_crawler.py` 和 `nist_crawler.py` 更新框架内容
- **每次爬取后**：运行 `consolidate.py` 重建统一语料库

## 上游源仓库

`doc/` 目录包含来自以下公开仓库的数据：

- [OWASP Top 10](https://github.com/OWASP/Top10)
- [cvelistV5](https://github.com/CVEProject/cvelistV5)
- [ATT&CK STIX Data](https://github.com/mitre-attack/attack-stix-data)

如需完整的上游数据集，请直接从源仓库克隆。

## 许可证

MIT License — 详见 [LICENSE](LICENSE)。
