# 网络安全 RAG 语料采集 — 最终汇总报告

## 采集时间: 2026-07-24 12:09:37

## 采集统计

| 类别 | 文件数 | 格式 |
|------|-------|------|
| CISA KEV | 1 | Markdown |
| NVD Recent CVEs | 100 | Markdown |
| OWASP Top 10 | 1 | Markdown |

| **总计** | **102** | |

## 数据目录结构
```
crawled_data/
├── live/
│   ├── markdown/          # 102 个 Markdown 文件
│   │   ├── cleaned_CWE-*.md
│   │   ├── cleaned_CVE-*.md
│   │   ├── cleaned_CAPEC-*.md
│   │   ├── CISA_KEV_*.md
│   │   └── OWASP_Top10_*.md
│   └── json/              # 2 个 JSON 文件
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
*自动生成于: 2026-07-24 12:09:37*
