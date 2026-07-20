"""
互联网关键词检索爬虫
对网络安全/数据安全相关的关键词进行搜索引擎检索，抓取结果页面正文，
输出为结构化 Markdown，供 RAG 语料库使用。

搜索后端: DuckDuckGo (免费，无需 API Key)
内容提取: trafilatura (优先) → BeautifulSoup (回退)
"""
import requests
import time
import re
import json
import hashlib
from pathlib import Path
from crawlers import CRAWLED_DIR
from datetime import datetime
from urllib.parse import urlparse, quote

# 搜索后端: 优先使用新版 ddgs，回退到旧版 duckduckgo_search
HAS_DDGS = False
DDGS = None
try:
    from ddgs import DDGS
    HAS_DDGS = True
except ImportError:
    try:
        from duckduckgo_search import DDGS
        HAS_DDGS = True
    except ImportError:
        print("⚠️ ddgs / duckduckgo-search 未安装，搜索功能不可用。")
        print("   请运行: pip install ddgs")

# 内容提取
try:
    import trafilatura
    HAS_TRAFILATURA = True
except ImportError:
    HAS_TRAFILATURA = False
    print("⚠️ trafilatura 未安装，正文提取将使用回退方案。")

from bs4 import BeautifulSoup

# ==================== 配置区 ====================
OUTPUT_DIR = CRAWLED_DIR / "live" / "internet_search"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 搜索结果保存目录
RESULTS_DIR = OUTPUT_DIR / "search_results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# 请求间隔
REQUEST_DELAY = 3.0
FETCH_DELAY = 2.0

# 每个关键词最多抓取的文章数
MAX_RESULTS_PER_KEYWORD = 10

# 每篇文章最大字符数 (截断)
MAX_CONTENT_CHARS = 8000

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

# ==================== 关键词库 ====================

# 中文关键词
CN_KEYWORDS = [
    # 漏洞与攻击
    "2026年 重大网络安全漏洞 通报",
    "零日漏洞 最新 2026",
    "勒索软件 攻击事件 2026",
    "供应链攻击 案例 分析",
    "APT 高级持续性威胁 最新动态",

    # 数据安全
    "数据泄露 事件 2026 处罚",
    "个人信息保护 合规 案例",
    "数据跨境传输 安全评估 最新规定",
    "数据分类分级 实施指南",
    "重要数据 目录 管理 实践",

    # AI安全
    "大模型安全 攻击 防御",
    "AI 生成内容 安全风险",
    "提示词注入 防护 方案",
    "深度伪造 检测 技术",

    # 云与基础设施
    "云安全 最佳实践 2026",
    "零信任 架构 实施 方案",
    "软件供应链安全 SBOM",
    "开源软件 安全治理",

    # 法规合规
    "网络安全等级保护 2.0 测评 要求",
    "关基 保护 条例 实施 细则",
    "数据安全法 执法案例",
    "个人信息出境 标准合同 备案",

    # 新兴威胁
    "量子计算 对密码学 威胁",
    "物联网安全 漏洞 2026",
    "车联网 数据安全 规定",
    "工业控制系统 安全 事件",
]

# 英文关键词
EN_KEYWORDS = [
    "critical CVE vulnerability 2026 exploitation",
    "ransomware attack 2026 analysis",
    "zero-day vulnerability 2026 disclosure",
    "data breach incident 2026 report",
    "supply chain attack 2026 case study",
    "APT group threat intelligence 2026",
    "cloud security best practices 2026",
    "zero trust architecture implementation guide",
    "LLM AI security vulnerability OWASP",
    "prompt injection defense techniques",
    "software supply chain security SBOM",
    "NIST CSF 2.0 implementation guide",
    "cybersecurity regulation compliance 2026",
    "IoT security vulnerability 2026",
    "quantum computing cryptography threat",
]


def safe_get(url: str, timeout: int = 25, max_retries: int = 2) -> str | None:
    """获取网页 HTML"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "no-cache",
    }

    for attempt in range(max_retries):
        try:
            time.sleep(FETCH_DELAY)
            resp = requests.get(url, headers=headers, timeout=timeout,
                              allow_redirects=True, verify=True)

            # 接受 2xx 和部分可处理的非 2xx
            if resp.status_code >= 400:
                # 403/429/503 等 — 重试
                if resp.status_code in (429, 503, 502):
                    wait = 10 * (attempt + 1)
                    print(f"    ⏳ HTTP {resp.status_code}, 等待 {wait}s...")
                    time.sleep(wait)
                    continue
                return None

            ct = resp.headers.get("Content-Type", "")
            if "html" not in ct and "text" not in ct:
                return None

            # 检查是否为反爬页面
            text = resp.text
            if len(text) < 500:
                # 太短可能是 JS 挑战页面
                if any(kw in text.lower() for kw in ["cloudflare", "challenge", "captcha", "cf-browser"]):
                    return None

            return text

        except requests.exceptions.Timeout:
            if attempt == max_retries - 1:
                return None
            time.sleep(5)
        except requests.exceptions.ConnectionError:
            if attempt == max_retries - 1:
                return None
            time.sleep(3)
        except Exception:
            if attempt == max_retries - 1:
                return None
            time.sleep(3)
    return None


def extract_content(html: str, url: str = "") -> str:
    """从 HTML 中提取正文内容"""
    if not html:
        return ""

    # 优先使用 trafilatura
    if HAS_TRAFILATURA:
        try:
            text = trafilatura.extract(
                html,
                include_comments=False,
                include_tables=True,
                no_fallback=False,
                favor_precision=True,
            )
            if text and len(text) > 200:
                return clean_text(text)
        except Exception:
            pass

    # 回退: BeautifulSoup
    try:
        soup = BeautifulSoup(html, "lxml" if _has_lxml() else "html.parser")

        # 移除无用标签
        for tag in soup(["script", "style", "nav", "footer", "header",
                         "aside", "noscript", "iframe", "form"]):
            tag.decompose()

        # 尝试找到主内容区
        main = (
            soup.find("article") or
            soup.find("main") or
            soup.find(attrs={"role": "main"}) or
            soup.find("div", class_=re.compile(r"content|article|post|entry", re.I)) or
            soup.find("body")
        )

        if main:
            text = main.get_text(separator="\n", strip=True)
            return clean_text(text)
    except Exception:
        pass

    return ""


def _has_lxml() -> bool:
    try:
        import lxml
        return True
    except ImportError:
        return False


def clean_text(text: str) -> str:
    """清洗提取的文本"""
    if not text:
        return ""
    # 合并过多的空行
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    # 去除过多的空格
    text = re.sub(r' {3,}', '  ', text)
    # 去除首尾空白
    text = text.strip()
    return text


def search_duckduckgo(keyword: str, max_results: int = 10, region: str = "wt-wt") -> list[dict]:
    """通过 DuckDuckGo 搜索关键词

    region 参数:
      - 'cn-zh' 中国中文
      - 'us-en' 美国英文
      - 'wt-wt' 全球 (默认)
    """
    if not HAS_DDGS or DDGS is None:
        print("    ❌ 搜索后端不可用")
        return []

    results = []
    try:
        with DDGS() as ddgs:
            search_results = list(ddgs.text(
                keyword,
                max_results=max_results,
                region=region,
            ))
            for r in search_results:
                url = r.get("href", "")
                # 过滤明显不相关的域名
                if _is_likely_irrelevant(url):
                    continue
                results.append({
                    "title": r.get("title", ""),
                    "url": url,
                    "snippet": r.get("body", ""),
                })
    except Exception as e:
        print(f"    ⚠️ 搜索异常: {e}")

    # 如果全球搜索无结果，尝试美国区域
    if not results and region != "us-en":
        try:
            with DDGS() as ddgs:
                search_results = list(ddgs.text(
                    keyword, max_results=max_results, region="us-en"
                ))
                for r in search_results:
                    url = r.get("href", "")
                    if _is_likely_irrelevant(url):
                        continue
                    results.append({
                        "title": r.get("title", ""),
                        "url": url,
                        "snippet": r.get("body", ""),
                    })
        except Exception:
            pass

    return results


def _is_likely_irrelevant(url: str) -> bool:
    """判断 URL 是否明显与安全主题无关"""
    irrelevant_domains = [
        "amazon.", "ebay.", "etsy.", "walmart.", "shopify.",
        "priceoye.", "daraz.", "alibaba.", "aliexpress.",
        "youtube.com/watch", "youtu.be/",
        "facebook.com", "instagram.com", "tiktok.com",
        "pinterest.", "twitter.com",
    ]
    url_lower = url.lower()
    for domain in irrelevant_domains:
        if domain in url_lower:
            return True
    return False


def crawl_security_sites(site_configs: list[dict]) -> list[dict]:
    """直接爬取已知的安全站点/博客

    当搜索引擎效果不佳时的补充方案。
    每个 site_config 包含: name, url, article_selector (CSS)
    """
    print("\n" + "="*60)
    print("📡 直接爬取安全资讯站点...")
    print("="*60)

    all_articles = []
    for cfg in site_configs:
        name = cfg.get("name", "unknown")
        url = cfg.get("url", "")
        print(f"\n  正在爬取: {name} ({url})")

        html = safe_get(url)
        if not html:
            print(f"    ⚠️ 无法获取页面")
            continue

        try:
            soup = BeautifulSoup(html, "lxml" if _has_lxml() else "html.parser")

            # 提取文章链接
            links = []
            for a in soup.find_all("a", href=True):
                href = a["href"]
                text = a.get_text(strip=True)
                if text and len(text) > 10:
                    # 转换为绝对 URL
                    from urllib.parse import urljoin
                    abs_url = urljoin(url, href)
                    links.append({"title": text[:120], "url": abs_url})

            # 去重并限制数量
            seen = set()
            unique_links = []
            for link in links:
                if link["url"] not in seen:
                    seen.add(link["url"])
                    unique_links.append(link)
                if len(unique_links) >= 10:
                    break

            print(f"    发现 {len(unique_links)} 个链接")

            for li, link in enumerate(unique_links[:5]):
                print(f"    [{li+1}] {link['title'][:60]}...")
                extraction = fetch_and_extract(link["url"])
                link["fetch_success"] = extraction["success"]
                link["full_content"] = extraction["content"]
                link["snippet"] = ""
                all_articles.append(link)

        except Exception as e:
            print(f"    ⚠️ 解析失败: {e}")

    return all_articles


# 已知的安全资讯站点（当搜索效果不佳时的直接爬取目标）
SECURITY_SITES = [
    {
        "name": "The Hacker News",
        "url": "https://thehackernews.com/",
    },
    {
        "name": "Bleeping Computer",
        "url": "https://www.bleepingcomputer.com/",
    },
    {
        "name": "Krebs on Security",
        "url": "https://krebsonsecurity.com/",
    },
    {
        "name": "Schneier on Security",
        "url": "https://www.schneier.com/",
    },
    {
        "name": "CISA News",
        "url": "https://www.cisa.gov/news-events/news",
    },
    {
        "name": "NIST CSRC News",
        "url": "https://csrc.nist.gov/news",
    },
    {
        "name": "SANS ISC",
        "url": "https://isc.sans.edu/",
    },
    {
        "name": "Dark Reading",
        "url": "https://www.darkreading.com/",
    },
    {
        "name": "Threatpost",
        "url": "https://threatpost.com/",
    },
    {
        "name": "FreeBuf (中文)",
        "url": "https://www.freebuf.com/",
    },
    {
        "name": "安全客 (中文)",
        "url": "https://www.anquanke.com/",
    },
    {
        "name": "嘶吼 (中文)",
        "url": "https://www.4hou.com/",
    },
]


def fetch_and_extract(url: str) -> dict:
    """获取页面并提取正文"""
    html = safe_get(url)
    if not html:
        return {"success": False, "content": "", "error": "无法获取页面"}

    content = extract_content(html, url)
    if content and len(content) > 100:
        if len(content) > MAX_CONTENT_CHARS:
            content = content[:MAX_CONTENT_CHARS] + "\n\n[... 内容已截断 ...]"
        return {"success": True, "content": content, "error": None}
    else:
        return {"success": False, "content": "", "error": "无法提取有效正文"}


def sanitize_filename(name: str) -> str:
    """生成安全的文件名"""
    name = re.sub(r'[\\/:*?"<>|]', '_', name)
    name = re.sub(r'\s+', '_', name)
    return name[:80]


def generate_markdown(result: dict, keyword: str) -> str:
    """生成结构化 Markdown"""
    title = result.get("title", "无标题")
    url = result.get("url", "")
    snippet = result.get("snippet", "")
    content = result.get("full_content", "")
    fetch_success = result.get("fetch_success", False)

    domain = urlparse(url).netloc if url else "unknown"

    md = f"""# {title}

### 来源信息
- **URL**: {url}
- **域名**: {domain}
- **检索关键词**: {keyword}
- **页面抓取**: {'成功' if fetch_success else '失败（仅保留摘要）'}

### 搜索摘要
{snippet if snippet else '（无摘要）'}

"""
    if fetch_success and content:
        md += f"""### 页面正文
{content}

"""
    elif not fetch_success:
        md += f"""### 备注
页面正文抓取失败，以上搜索摘要可作为参考信息。

"""

    md += f"""---
*检索时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*搜索来源: DuckDuckGo*
"""
    return md


def crawl_keywords(keywords: list[str], lang: str):
    """爬取一组关键词的搜索结果"""
    total_fetched = 0
    total_extracted = 0

    for ki, keyword in enumerate(keywords, 1):
        print(f"\n{'='*60}")
        print(f"[{ki}/{len(keywords)}] [{lang}] 搜索: {keyword}")
        print(f"{'='*60}")

        # 1. 搜索
        search_results = search_duckduckgo(
            keyword, MAX_RESULTS_PER_KEYWORD,
            region="cn-zh" if lang == "zh" else "us-en"
        )
        print(f"  📊 搜索结果: {len(search_results)} 条")

        if not search_results:
            print(f"  ⚠️ 无搜索结果，跳过")
            continue

        # 2. 为每个关键词创建子目录
        kw_dirname = sanitize_filename(keyword)[:50]
        kw_dir = RESULTS_DIR / f"{lang}_{kw_dirname}"
        kw_dir.mkdir(parents=True, exist_ok=True)

        # 3. 抓取每个结果
        keyword_results = []
        for ri, result in enumerate(search_results):
            url = result.get("url", "")
            title = result.get("title", "无标题")[:100]
            print(f"\n  [{ri+1}/{len(search_results)}] {title}...")

            if not url:
                print(f"    ⚠️ 无 URL，跳过")
                continue

            # 抓取页面正文
            extraction = fetch_and_extract(url)
            result["fetch_success"] = extraction["success"]
            result["full_content"] = extraction["content"]

            if extraction["success"]:
                total_extracted += 1
                print(f"    ✅ 正文提取成功 ({len(extraction['content'])} 字符)")
            else:
                print(f"    ⚠️ {extraction['error']}")

            total_fetched += 1

            # 生成 Markdown
            md_content = generate_markdown(result, keyword)
            # 用 URL hash 做文件名
            url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
            file_name = f"{sanitize_filename(title)[:60]}_{url_hash}.md"
            file_path = kw_dir / file_name

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(md_content)

            keyword_results.append(result)

        # 4. 保存关键词级别的汇总 JSON
        summary = {
            "keyword": keyword,
            "language": lang,
            "searched_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "total_results": len(search_results),
            "fetched_count": len([r for r in keyword_results if r.get("fetch_success")]),
            "results": [
                {
                    "title": r.get("title"),
                    "url": r.get("url"),
                    "snippet": r.get("snippet"),
                    "fetched": r.get("fetch_success", False),
                    "char_count": len(r.get("full_content", "")),
                }
                for r in keyword_results
            ],
        }
        with open(kw_dir / "_summary.json", "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

    return total_fetched, total_extracted


def generate_index():
    """生成互联网检索总索引"""
    all_summaries = []
    for summary_file in sorted(RESULTS_DIR.glob("*/_summary.json")):
        try:
            with open(summary_file, "r", encoding="utf-8") as f:
                all_summaries.append(json.load(f))
        except Exception:
            pass

    index = f"""# 互联网关键词检索汇总

## 检索时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 统计概览

| 指标 | 数值 |
|------|------|
| 结果集总数 | {len(all_summaries)} |

## 检索结果

| # | 类型 | 关键词/站点 | 语言 | 搜索结果 | 成功抓取 |
|---|------|-----------|------|---------|---------|
"""
    for i, s in enumerate(all_summaries, 1):
        if "site" in s:
            # 站点直爬结果
            name = s.get("site", "")[:50]
            lang = "site"
            total = s.get("total_found", 0)
            fetched = s.get("saved", 0)
        else:
            # 关键词检索结果
            name = s.get("keyword", "")[:50]
            lang = s.get("language", "unknown")
            total = s.get("total_results", 0)
            fetched = s.get("fetched_count", 0)
        index += f"| {i} | {'站点' if 'site' in s else '关键词'} | {name} | {lang} | {total} | {fetched} |\n"

    index += f"""

## 目录结构
```
internet/output/search_results/
"""
    for s in all_summaries:
        if "site" in s:
            name = sanitize_filename(s.get("site", "unknown"))[:50]
            index += f"├── site_{name}/\n"
        else:
            name = sanitize_filename(s.get("keyword", "unknown"))[:50]
            lang = s.get("language", "??")
            index += f"├── {lang}_{name}/\n"
    index += "```\n"

    with open(OUTPUT_DIR / "SEARCH_INDEX.md", "w", encoding="utf-8") as f:
        f.write(index)
    print(f"\n  ✅ 检索索引已保存: SEARCH_INDEX.md")


def save_site_articles(articles: list[dict], site_name: str):
    """保存直接爬取的站点文章"""
    site_dir = RESULTS_DIR / f"site_{sanitize_filename(site_name)}"
    site_dir.mkdir(parents=True, exist_ok=True)

    saved = 0
    for article in articles:
        title = article.get("title", "无标题")
        url = article.get("url", "")
        content = article.get("full_content", "")
        fetch_success = article.get("fetch_success", False)

        if not fetch_success or not content:
            continue

        md = f"""# {title}

### 来源信息
- **URL**: {url}
- **来源站点**: {site_name}
- **页面抓取**: 成功

### 页面正文
{content[:MAX_CONTENT_CHARS]}

---
*检索时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*来源: 直接站点爬取*
"""
        url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
        file_name = f"{sanitize_filename(title)[:60]}_{url_hash}.md"
        with open(site_dir / file_name, "w", encoding="utf-8") as f:
            f.write(md)
        saved += 1

    # Summary
    summary = {
        "site": site_name,
        "crawled_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "total_found": len(articles),
        "saved": saved,
        "articles": [
            {"title": a.get("title"), "url": a.get("url")}
            for a in articles if a.get("fetch_success")
        ],
    }
    with open(site_dir / "_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    return saved


def main():
    print("=" * 60)
    print("🌐 互联网关键词检索爬虫")
    print("=" * 60)
    print(f"📂 输出目录: {OUTPUT_DIR}")
    print(f"🔤 中文关键词: {len(CN_KEYWORDS)} 个")
    print(f"🔤 英文关键词: {len(EN_KEYWORDS)} 个")
    print(f"📡 安全站点直爬: {len(SECURITY_SITES)} 个")
    print(f"📊 每关键词最多抓取: {MAX_RESULTS_PER_KEYWORD} 篇文章")
    print(f"⚠️  预计耗时: "
          f"{(len(CN_KEYWORDS) + len(EN_KEYWORDS)) * 20 // 60} 分钟 "
          f"(关键词检索) + {len(SECURITY_SITES) * 2 // 60} 分钟 (站点直爬)")
    print("=" * 60)

    if not HAS_DDGS:
        print("\n⚠️ 搜索后端不可用，将仅使用站点直爬模式。")
        print("   如需关键词检索，请运行: pip install ddgs")

    total_fetched = 0
    total_extracted = 0

    try:
        # 第一阶段：关键词检索
        if HAS_DDGS and DDGS is not None:
            # 中文关键词
            print("\n" + "=" * 60)
            print("🔍 第一阶段: 中文关键词检索")
            print("=" * 60)
            f1, e1 = crawl_keywords(CN_KEYWORDS, "zh")
            total_fetched += f1
            total_extracted += e1

            # 英文关键词
            print("\n" + "=" * 60)
            print("🔍 第二阶段: 英文关键词检索")
            print("=" * 60)
            f2, e2 = crawl_keywords(EN_KEYWORDS, "en")
            total_fetched += f2
            total_extracted += e2
        else:
            print("\n  ⏭️  跳过关键词检索 (搜索后端不可用)")

        # 第三阶段：安全站点直接爬取
        print("\n" + "=" * 60)
        print("📡 第三阶段: 安全资讯站点直接爬取")
        print("=" * 60)
        site_saved = 0
        for site_cfg in SECURITY_SITES:
            site_name = site_cfg["name"]
            print(f"\n  站点: {site_name} ({site_cfg['url']})")
            articles = crawl_security_sites([site_cfg])
            saved = save_site_articles(articles, site_name)
            site_saved += saved
            print(f"    💾 保存: {saved} 篇文章")

    except KeyboardInterrupt:
        print("\n⚠️ 用户中断, 已抓取的数据已保存。")

    # 生成索引
    print("\n" + "=" * 60)
    print("📊 生成检索索引...")
    print("=" * 60)
    generate_index()

    print("\n" + "=" * 60)
    print("🎉 互联网关键词检索完成!")
    print(f"📊 关键词检索 — 抓取: {total_fetched}, 成功: {total_extracted}")
    print(f"📊 站点直爬 — 保存: {site_saved if 'site_saved' in dir() else 'N/A'} 篇")
    print(f"📂 数据保存在: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
