# 网络安全语料爬取汇总

## 爬取时间: 2026-07-17 13:44:19

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
