# 网络安全 RAG 语料库 — 数据整合报告

## 生成时间: 2026-07-24 12:10:10

## 数据统计

| 指标 | 数值 |
|------|------|
| 总条目数 | 184 |
| 总字符数 | 362,380 |
| 平均每条目字符数 | 1,969 |
| 数据来源数 | 7 |
| 分类数 | 8 |

## 分类分布

| 分类 | 条目数 | 占比 |
|------|-------|------|
| vulnerability | 140 | 76.1% |
| weakness | 25 | 13.6% |
| regulation_and_standard | 6 | 3.3% |
| security_framework | 4 | 2.2% |
| weakness_view | 3 | 1.6% |
| security_standard | 3 | 1.6% |
| attack_pattern | 2 | 1.1% |
| known_exploited_vulnerability | 1 | 0.5% |


## 来源分布

| 来源 | 条目数 |
|------|-------|
| NVD | 140 |
| MITRE CWE | 28 |
| China Standards | 6 |
| NIST | 4 |
| OWASP | 3 |
| MITRE CAPEC | 2 |
| CISA | 1 |

## 输出文件列表

| 文件 | 格式 | 用途 |
|------|------|------|
| `rag_corpus.json` | JSON | 程序化处理、数据清洗 |
| `rag_corpus.md` | Markdown | 人工阅读、全文检索 |
| `corpus_index.json` | JSON | 轻量索引、快速查找 |
| `by_category/*.md` | Markdown | 按分类独立处理 |

## 与现有语料的对接
该语料库可直接合并入上层 RAG 项目的 clean/ 目录，
按照 `tool/` 下的清洗脚本流程处理后导入向量数据库。

## 后续建议
1. 运行 `clean_*.py` 系列脚本对新语料进行深度清洗
2. 运行 `splitter.py` 进行智能切片 (chunk_size: 600-800)
3. 使用 embedding 模型生成向量
4. 导入向量数据库 (Milvus/FAISS/Chroma) 进行 RAG 检索测试
