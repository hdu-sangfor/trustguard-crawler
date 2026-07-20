"""
数据整合脚本
将爬取的网络安全语料合并为一个统一的结构化 JSON 文件和汇总 Markdown，
便于后续数据清洗和 RAG 导入。

输入: crawled_data/ (所有爬虫输出)
输出:
  - consolidated/rag_corpus.json      (标准 JSON 格式，适合程序化处理)
  - consolidated/rag_corpus.md        (完整合并 Markdown)
  - consolidated/corpus_index.json    (语料索引，记录每条数据的元信息)
"""
import json
import os
import re
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
from datetime import datetime

# ==================== 配置区 ====================
CRAWLED_DIR = PROJECT_ROOT / "doc" / "crawled"
OUTPUT_DIR = CRAWLED_DIR / "consolidated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ==================== 语料条目结构 ====================
def create_corpus_entry(
    source: str,
    category: str,
    doc_id: str,
    title: str,
    content: str,
    metadata: dict = None
) -> dict:
    """创建标准语料条目"""
    return {
        "source": source,           # 数据来源, e.g. "MITRE CWE", "NVD", "NIST"
        "category": category,       # 分类, e.g. "vulnerability", "standard", "regulation"
        "doc_id": doc_id,          # 唯一标识符
        "title": title,            # 标题
        "content": content,        # 正文内容
        "char_count": len(content),
        "metadata": metadata or {},
        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def clean_text(text: str) -> str:
    """基本文本清洗"""
    if not text:
        return ""
    # 移除多余空白
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    return text.strip()


def parse_md_file(filepath: Path) -> dict:
    """解析 Markdown 文件，提取标题和内容"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 提取一级标题
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filepath.stem

        return {
            "title": title,
            "content": clean_text(content),
            "filepath": str(filepath),
        }
    except Exception as e:
        print(f"  ⚠️ 读取文件失败 {filepath}: {e}")
        return {"title": filepath.stem, "content": f"[读取失败: {e}]", "filepath": str(filepath)}


def collect_all_documents() -> list:
    """收集所有爬取的文档"""
    print("=" * 60)
    print("📂 收集所有爬取数据...")
    print("=" * 60)

    all_entries = []

    # 1. CWE Top 25
    cwe_dir = CRAWLED_DIR / "cwe" / "top25_2024"
    if cwe_dir.exists():
        print(f"\n  📁 CWE Top 25: {cwe_dir}")
        for md_file in sorted(cwe_dir.glob("cleaned_CWE-*.md")):
            parsed = parse_md_file(md_file)
            # 提取 CWE ID
            cwe_id_match = re.search(r'CWE-\d+', parsed["title"])
            cwe_id = cwe_id_match.group(0) if cwe_id_match else md_file.stem

            all_entries.append(create_corpus_entry(
                source="MITRE CWE",
                category="weakness",
                doc_id=cwe_id,
                title=parsed["title"],
                content=parsed["content"],
                metadata={"cwe_rank": "Top 25 2024", "file": parsed["filepath"]}
            ))
        print(f"    ✅ {len(list(cwe_dir.glob('cleaned_CWE-*.md')))} 个 CWE 条目")

    # 2. CWE Views
    views_dir = CRAWLED_DIR / "cwe" / "categories"
    if views_dir.exists():
        print(f"\n  📁 CWE Views: {views_dir}")
        for md_file in sorted(views_dir.glob("view_*.md")):
            parsed = parse_md_file(md_file)
            view_id_match = re.search(r'view_(\d+)', md_file.stem)
            view_id = view_id_match.group(1) if view_id_match else md_file.stem
            all_entries.append(create_corpus_entry(
                source="MITRE CWE",
                category="weakness_view",
                doc_id=f"CWE-View-{view_id}",
                title=parsed["title"],
                content=parsed["content"],
                metadata={"file": parsed["filepath"]}
            ))
        print(f"    ✅ {len(list(views_dir.glob('view_*.md')))} 个 CWE 视图")

    # 3. CAPEC
    capec_dir = CRAWLED_DIR / "cwe" / "capec"
    if capec_dir.exists():
        print(f"\n  📁 CAPEC: {capec_dir}")
        for md_file in sorted(capec_dir.glob("CAPEC_*.md")):
            parsed = parse_md_file(md_file)
            all_entries.append(create_corpus_entry(
                source="MITRE CAPEC",
                category="attack_pattern",
                doc_id=md_file.stem,
                title=parsed["title"],
                content=parsed["content"],
                metadata={"file": parsed["filepath"]}
            ))
        print(f"    ✅ {len(list(capec_dir.glob('CAPEC_*.md')))} 个 CAPEC 条目")

    # 4. OWASP (cwe dir)
    owasp_dir = CRAWLED_DIR / "cwe" / "owasp"
    if owasp_dir.exists():
        print(f"\n  📁 OWASP (CWE): {owasp_dir}")
        for md_file in sorted(owasp_dir.glob("OWASP_*.md")):
            parsed = parse_md_file(md_file)
            all_entries.append(create_corpus_entry(
                source="OWASP",
                category="security_standard",
                doc_id=md_file.stem,
                title=parsed["title"],
                content=parsed["content"],
                metadata={"file": parsed["filepath"]}
            ))
        print(f"    ✅ {len(list(owasp_dir.glob('OWASP_*.md')))} 个 OWASP 条目")

    # 5. NIST
    nist_dir = CRAWLED_DIR / "nist"
    if nist_dir.exists():
        print(f"\n  📁 NIST: {nist_dir}")
        for md_file in sorted(nist_dir.glob("*.md")):
            parsed = parse_md_file(md_file)
            all_entries.append(create_corpus_entry(
                source="NIST",
                category="security_framework",
                doc_id=md_file.stem,
                title=parsed["title"],
                content=parsed["content"],
                metadata={"file": parsed["filepath"]}
            ))
        # NVD recent
        nvd_dir = nist_dir / "nvd_recent"
        if nvd_dir.exists():
            for md_file in sorted(nvd_dir.glob("cleaned_CVE-*.md")):
                parsed = parse_md_file(md_file)
                cve_id_match = re.search(r'CVE-\d{4}-\d+', parsed["title"])
                cve_id = cve_id_match.group(0) if cve_id_match else md_file.stem
                all_entries.append(create_corpus_entry(
                    source="NVD",
                    category="vulnerability",
                    doc_id=cve_id,
                    title=parsed["title"],
                    content=parsed["content"],
                    metadata={"file": parsed["filepath"]}
                ))
        print(f"    ✅ {len(list(nist_dir.glob('*.md')) + list((nist_dir / 'nvd_recent').glob('cleaned_CVE-*.md')) if (nist_dir / 'nvd_recent').exists() else list(nist_dir.glob('*.md')))} 个 NIST/NVD 条目")

    # 6. China Standards
    china_dir = CRAWLED_DIR / "china_standards"
    if china_dir.exists():
        print(f"\n  📁 China Standards: {china_dir}")
        for md_file in sorted(china_dir.glob("*.md")):
            if md_file.name == "INDEX.md":
                continue
            parsed = parse_md_file(md_file)
            all_entries.append(create_corpus_entry(
                source="China Standards",
                category="regulation_and_standard",
                doc_id=md_file.stem,
                title=parsed["title"],
                content=parsed["content"],
                metadata={"file": parsed["filepath"]}
            ))
        print(f"    ✅ {len([f for f in china_dir.glob('*.md') if f.name != 'INDEX.md'])} 个中国标准条目")

    # 7. Live data
    live_dir = CRAWLED_DIR / "live"
    if live_dir.exists():
        print(f"\n  📁 Live Data: {live_dir}")
        live_md = live_dir / "markdown"
        if live_md.exists():
            for md_file in sorted(live_md.glob("*.md")):
                parsed = parse_md_file(md_file)
                # 判断分类
                if "CISA" in md_file.name or "KEV" in md_file.name:
                    cat = "known_exploited_vulnerability"
                    source = "CISA"
                elif "OWASP" in md_file.name:
                    cat = "security_standard"
                    source = "OWASP"
                elif "CVE" in md_file.name:
                    cat = "vulnerability"
                    source = "NVD"
                else:
                    cat = "other"
                    source = "Live"

                all_entries.append(create_corpus_entry(
                    source=source,
                    category=cat,
                    doc_id=md_file.stem,
                    title=parsed["title"],
                    content=parsed["content"],
                    metadata={"file": parsed["filepath"]}
                ))
        print(f"    ✅ {len(list(live_md.glob('*.md')) if live_md.exists() else [])} 个实时数据条目")

    return all_entries


def generate_consolidated_markdown(entries: list) -> str:
    """生成统一的合并 Markdown"""
    md = f"""# 网络安全与数据安全 RAG 语料库
## Unified Cybersecurity RAG Corpus

> **生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
> **总条目数**: {len(entries)}
> **总字符数**: {sum(e['char_count'] for e in entries):,}

---

## 目录

"""
    # 按分类组织目录
    from collections import defaultdict
    categories = defaultdict(list)
    for i, entry in enumerate(entries):
        categories[entry["category"]].append((i, entry))

    for cat, items in sorted(categories.items()):
        cat_name = {
            "weakness": "软件弱点 (CWE)",
            "weakness_view": "弱点分类视图 (CWE Views)",
            "attack_pattern": "攻击模式 (CAPEC)",
            "vulnerability": "漏洞实例 (CVE)",
            "known_exploited_vulnerability": "已知被利用漏洞 (CISA KEV)",
            "security_framework": "安全框架 (NIST/ISO)",
            "security_standard": "安全标准 (OWASP)",
            "regulation_and_standard": "法规与标准 (中国)",
            "other": "其他",
        }.get(cat, cat)
        md += f"- **{cat_name}** ({len(items)} 条)\n"
        for idx, entry in items:
            md += f"  - [{entry['doc_id']}](#{entry['doc_id'].lower().replace(':', '').replace(' ', '-')}) — {entry['title'][:80]}\n"

    md += "\n---\n\n"

    # 逐条输出
    for i, entry in enumerate(entries):
        md += f"""
{'='*60}
## {entry['doc_id']}
### {entry['title']}

**来源**: {entry['source']} | **分类**: {entry['category']} | **字符数**: {entry['char_count']}

{entry['content']}

---
"""
        # 每50条输出一次进度
        if (i + 1) % 50 == 0:
            print(f"  ⏳ 生成 Markdown: {i+1}/{len(entries)}...")

    return md


def generate_corpus_json(entries: list) -> dict:
    """生成标准 JSON 格式的语料库"""
    corpus = {
        "meta": {
            "name": "网络安全与数据安全 RAG 语料库",
            "version": "1.0",
            "generated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "total_entries": len(entries),
            "total_chars": sum(e['char_count'] for e in entries),
            "categories": {},
            "sources": {},
        },
        "entries": entries,
    }

    # 统计分类
    from collections import Counter
    cat_counter = Counter(e["category"] for e in entries)
    src_counter = Counter(e["source"] for e in entries)

    corpus["meta"]["categories"] = dict(cat_counter)
    corpus["meta"]["sources"] = dict(src_counter)

    return corpus


def generate_corpus_index(entries: list) -> list:
    """生成语料索引（轻量级，只含元数据不含正文）"""
    index = []
    for entry in entries:
        index.append({
            "doc_id": entry["doc_id"],
            "title": entry["title"],
            "source": entry["source"],
            "category": entry["category"],
            "char_count": entry["char_count"],
            "metadata": entry["metadata"],
        })
    return index


def main():
    print("=" * 60)
    print("🔄 开始整合网络安全 RAG 语料库")
    print("=" * 60)

    # 1. 收集所有文档
    entries = collect_all_documents()
    print(f"\n  📊 总计收集: {len(entries)} 条语料")

    if not entries:
        print("  ❌ 未找到任何语料数据!")
        return

    # 2. 生成语料索引 (JSON)
    print("\n" + "="*60)
    print("📋 生成语料索引...")
    print("="*60)
    index = generate_corpus_index(entries)
    with open(OUTPUT_DIR / "corpus_index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"  ✅ 索引已保存: corpus_index.json ({len(index)} 条)")

    # 3. 生成完整 JSON 语料库
    print("\n" + "="*60)
    print("📦 生成完整 JSON 语料库...")
    print("="*60)
    corpus = generate_corpus_json(entries)
    with open(OUTPUT_DIR / "rag_corpus.json", "w", encoding="utf-8") as f:
        json.dump(corpus, f, ensure_ascii=False, indent=2)
    print(f"  ✅ JSON 语料库已保存: rag_corpus.json")
    print(f"  📊 总条目: {corpus['meta']['total_entries']}")
    print(f"  📊 总字符: {corpus['meta']['total_chars']:,}")
    print(f"  📊 分类: {json.dumps(corpus['meta']['categories'], ensure_ascii=False)}")
    print(f"  📊 来源: {json.dumps(corpus['meta']['sources'], ensure_ascii=False)}")

    # 4. 生成合并 Markdown
    print("\n" + "="*60)
    print("📝 生成合并 Markdown...")
    print("="*60)
    md_content = generate_consolidated_markdown(entries)
    md_path = OUTPUT_DIR / "rag_corpus.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    file_size_mb = md_path.stat().st_size / (1024 * 1024)
    print(f"  ✅ Markdown 已保存: rag_corpus.md ({file_size_mb:.1f} MB)")

    # 5. 生成按分类拆分的子文件
    print("\n" + "="*60)
    print("📂 生成按分类拆分的子文件...")
    print("="*60)
    from collections import defaultdict
    by_category = defaultdict(list)
    for entry in entries:
        by_category[entry["category"]].append(entry)

    split_dir = OUTPUT_DIR / "by_category"
    split_dir.mkdir(parents=True, exist_ok=True)

    for cat, cat_entries in sorted(by_category.items()):
        cat_md = f"# {cat}\n\n"
        for entry in cat_entries:
            cat_md += f"## {entry['doc_id']}: {entry['title']}\n"
            cat_md += f"**来源**: {entry['source']}\n\n"
            cat_md += f"{entry['content']}\n\n---\n\n"

        cat_file = split_dir / f"{cat}.md"
        with open(cat_file, "w", encoding="utf-8") as f:
            f.write(cat_md)
        print(f"  ✅ {cat}.md ({len(cat_entries)} 条)")

    # 6. 生成最终汇总报告
    print("\n" + "="*60)
    print("📊 生成最终汇总报告...")
    report = f"""# 网络安全 RAG 语料库 — 数据整合报告

## 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 数据统计

| 指标 | 数值 |
|------|------|
| 总条目数 | {len(entries)} |
| 总字符数 | {sum(e['char_count'] for e in entries):,} |
| 平均每条目字符数 | {sum(e['char_count'] for e in entries) // max(len(entries), 1):,} |
| 数据来源数 | {len(set(e['source'] for e in entries))} |
| 分类数 | {len(set(e['category'] for e in entries))} |

## 分类分布

| 分类 | 条目数 | 占比 |
|------|-------|------|
"""
    from collections import Counter
    cat_counts = Counter(e["category"] for e in entries)
    for cat, count in cat_counts.most_common():
        pct = count / max(len(entries), 1) * 100
        report += f"| {cat} | {count} | {pct:.1f}% |\n"

    report += """

## 来源分布

| 来源 | 条目数 |
|------|-------|
"""
    src_counts = Counter(e["source"] for e in entries)
    for src, count in src_counts.most_common():
        report += f"| {src} | {count} |\n"

    report += f"""
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
"""
    with open(OUTPUT_DIR / "INTEGRATION_REPORT.md", "w", encoding="utf-8") as f:
        f.write(report)
    print(f"  ✅ 整合报告已保存: INTEGRATION_REPORT.md")

    print("\n" + "=" * 60)
    print("🎉 语料整合全部完成!")
    print(f"📂 输出目录: {OUTPUT_DIR}")
    print("=" * 60)
    print(f"""
输出文件:
  📦 rag_corpus.json       — 完整 JSON 语料库
  📝 rag_corpus.md         — 完整 Markdown 语料
  📋 corpus_index.json     — 轻量索引
  📂 by_category/          — 按分类拆分的子文件
  📊 INTEGRATION_REPORT.md — 整合报告
""")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ 整合过程出错: {e}")
        import traceback
        traceback.print_exc()
