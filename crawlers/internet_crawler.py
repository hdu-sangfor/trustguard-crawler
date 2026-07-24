"""
互联网关键词检索爬虫（配置驱动版）
对网络安全/数据安全相关的关键词进行搜索引擎检索，抓取结果页面正文，
输出为结构化 Markdown，供 RAG 语料库使用。

搜索后端: DuckDuckGo (免费，无需 API Key)
内容提取: trafilatura (优先) → BeautifulSoup (回退)

使用方式:
  # 配置文件驱动（默认）
  python crawlers/internet_crawler.py --config crawler_config.json

  # CLI 参数直接覆盖
  python crawlers/internet_crawler.py --years 2025,2026 --max-pages 20 --max-chars 0

  # 强制重爬（忽略去重记录）
  python crawlers/internet_crawler.py --force

  # 仅生成默认配置文件
  python crawlers/internet_crawler.py --init-config
"""
import argparse
import hashlib
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import requests

from crawlers import CRAWLED_DIR

# ==================== 搜索后端 ====================
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
        pass

# ==================== 内容提取 ====================
HAS_TRAFILATURA = False
try:
    import trafilatura
    HAS_TRAFILATURA = True
except ImportError:
    pass

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False


def _has_lxml():
    try:
        import lxml
        return True
    except ImportError:
        return False


# ==================== 默认配置 ====================
DEFAULT_CONFIG = {
    "_comment": "互联网爬虫配置 — 可直接编辑此文件，或通过 Web UI 修改",
    "crawl": {
        "years": [2025, 2026],
        "max_results_per_keyword": 20,
        "max_pages_per_site": 15,
        "enable_keyword_search": True,
        "enable_site_crawl": True,
    },
    "content": {
        "max_chars": 0,
        "max_file_bytes": 100000,
    },
    "request": {
        "delay_seconds": 3.0,
        "fetch_delay_seconds": 2.0,
        "timeout_seconds": 25,
        "max_retries": 2,
    },
    "duckduckgo": {
        "region": "wt-wt",
    },
    "sources": {
        "security_sites": [
            # ---- 国际安全新闻 / 博客 ----
            {"name": "The Hacker News", "url": "https://thehackernews.com/"},
            {"name": "Bleeping Computer", "url": "https://www.bleepingcomputer.com/"},
            {"name": "Krebs on Security", "url": "https://krebsonsecurity.com/"},
            {"name": "Schneier on Security", "url": "https://www.schneier.com/"},
            {"name": "Dark Reading", "url": "https://www.darkreading.com/"},
            {"name": "Threatpost", "url": "https://threatpost.com/"},
            {"name": "SecurityWeek", "url": "https://www.securityweek.com/"},
            {"name": "Infosecurity Magazine", "url": "https://www.infosecurity-magazine.com/"},
            {"name": "CSO Online", "url": "https://www.csoonline.com/"},
            {"name": "ZDNet Security", "url": "https://www.zdnet.com/topic/security/"},
            {"name": "Help Net Security", "url": "https://www.helpnetsecurity.com/"},
            {"name": "CyberScoop", "url": "https://cyberscoop.com/"},
            {"name": "The Record", "url": "https://therecord.media/"},
            {"name": "Ars Technica Security", "url": "https://arstechnica.com/security/"},
            {"name": "GBHackers", "url": "https://gbhackers.com/"},
            # ---- 中国安全社区 ----
            {"name": "FreeBuf", "url": "https://www.freebuf.com/"},
            {"name": "安全客", "url": "https://www.anquanke.com/"},
            {"name": "嘶吼", "url": "https://www.4hou.com/"},
            {"name": "SecWiki", "url": "https://www.sec-wiki.com/"},
            {"name": "吾爱破解", "url": "https://www.52pojie.cn/"},
            {"name": "腾讯安全应急响应中心", "url": "https://security.tencent.com/"},
            {"name": "阿里云安全公告", "url": "https://www.alibabacloud.com/help/zh/security-notices/"},
            {"name": "奇安信威胁情报中心", "url": "https://ti.qianxin.com/"},
            # ---- 漏洞数据库 / 公告 ----
            {"name": "Exploit-DB", "url": "https://www.exploit-db.com/"},
            {"name": "Packet Storm Security", "url": "https://packetstormsecurity.com/"},
            {"name": "OpenCVE", "url": "https://www.opencve.io/cve"},
            # ---- 政府 / 标准机构 ----
            {"name": "CISA News", "url": "https://www.cisa.gov/news-events/news"},
            {"name": "NIST CSRC News", "url": "https://csrc.nist.gov/news"},
            {"name": "NCSC UK", "url": "https://www.ncsc.gov.uk/news"},
            {"name": "ACSC AU", "url": "https://www.cyber.gov.au/about-us/advisories"},
            {"name": "ENISA", "url": "https://www.enisa.europa.eu/news"},
        ],
        "cn_keywords": [
            "2025 2026 重大网络安全漏洞 通报",
            "零日漏洞 最新 2025 2026",
            "勒索软件 攻击事件 2025 2026",
            "供应链攻击 案例 分析 2025 2026",
            "APT 高级持续性威胁 最新动态 2025 2026",
            "数据泄露 事件 2025 2026 处罚",
            "个人信息保护 合规 案例 2025 2026",
            "数据跨境传输 安全评估 最新规定",
            "数据分类分级 实施指南",
            "大模型安全 攻击 防御 2025 2026",
            "AI 生成内容 安全风险 2025 2026",
            "提示词注入 防护 方案",
            "深度伪造 检测 技术",
            "云安全 最佳实践 2025 2026",
            "零信任 架构 实施 方案",
            "软件供应链安全 SBOM 2025 2026",
            "开源软件 安全治理",
            "网络安全等级保护 2.0 测评 要求",
            "关基 保护 条例 实施 细则",
            "数据安全法 执法案例",
            "个人信息出境 标准合同 备案",
            "量子计算 对密码学 威胁",
            "物联网安全 漏洞 2025 2026",
            "车联网 数据安全 规定",
            "工业控制系统 安全 事件 2025 2026",
        ],
        "en_keywords": [
            "critical CVE vulnerability 2025 2026 exploitation",
            "ransomware attack 2025 2026 analysis",
            "zero-day vulnerability 2025 2026 disclosure",
            "data breach incident 2025 2026 report",
            "supply chain attack 2025 2026 case study",
            "APT group threat intelligence 2025 2026",
            "cloud security best practices 2025 2026",
            "zero trust architecture implementation guide",
            "LLM AI security vulnerability OWASP 2025 2026",
            "prompt injection defense techniques",
            "software supply chain security SBOM 2025 2026",
            "NIST CSF 2.0 implementation guide",
            "cybersecurity regulation compliance 2025 2026",
            "IoT security vulnerability 2025 2026",
            "quantum computing cryptography threat",
            "CISA known exploited vulnerability 2025 2026",
            "cyber insurance requirements 2025 2026",
            "API security best practices 2025 2026",
            "container kubernetes security 2025 2026",
            "identity access management trends 2025 2026",
        ],
    },
}

# ==================== 路径常量 ====================
OUTPUT_DIR = CRAWLED_DIR / "live" / "internet_search"
RESULTS_DIR = OUTPUT_DIR / "search_results"
TRACKING_DIR = OUTPUT_DIR / "tracking"

# 跟踪文件路径
CRAWLED_URLS_FILE = TRACKING_DIR / "crawled_urls.json"
ERROR_URLS_FILE = TRACKING_DIR / "error_urls.log"
BLACKLIST_FILE = TRACKING_DIR / "blacklist.txt"
WHITELIST_FILE = TRACKING_DIR / "whitelist.txt"
PAUSE_FILE = TRACKING_DIR / "pause.flag"

# 默认配置文件路径
DEFAULT_CONFIG_PATH = OUTPUT_DIR / "crawler_config.json"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


# ==================== 配置加载 ====================
def ensure_dirs():
    """确保所有必要目录存在"""
    for d in [OUTPUT_DIR, RESULTS_DIR, TRACKING_DIR]:
        d.mkdir(parents=True, exist_ok=True)


def init_tracking_files():
    """初始化跟踪文件（不存在则创建默认内容）"""
    # crawled_urls.json
    if not CRAWLED_URLS_FILE.exists():
        CRAWLED_URLS_FILE.write_text("{}", encoding="utf-8")

    # error_urls.log
    if not ERROR_URLS_FILE.exists():
        ERROR_URLS_FILE.write_text(
            f"# 爬取失败 URL 日志 | 创建于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"# 格式: [时间] URL | 错误原因\n\n",
            encoding="utf-8",
        )

    # blacklist.txt
    if not BLACKLIST_FILE.exists():
        BLACKLIST_FILE.write_text(
            "# 黑名单 — 永不爬取的域名或完整 URL（每行一条）\n"
            "# 支持 # 开头的注释行\n"
            "# 示例:\n"
            "#   spam-tracker.com\n"
            "#   https://bad-site.com/scam-page\n"
            "\n"
            "# === 广告 / 追踪 ===\n"
            "doubleclick.net\n"
            "googleadservices.com\n"
            "googlesyndication.com\n"
            "facebook.com/plugins\n"
            "\n"
            "# === 非安全相关大型平台 ===\n"
            "amazon.com\n"
            "ebay.com\n"
            "etsy.com\n"
            "walmart.com\n"
            "shopify.com\n"
            "alibaba.com\n"
            "aliexpress.com\n"
            "pinterest.com\n"
            "instagram.com\n"
            "tiktok.com\n"
            "twitter.com\n"
            "youtube.com\n",
            encoding="utf-8",
        )

    # whitelist.txt
    if not WHITELIST_FILE.exists():
        WHITELIST_FILE.write_text(
            "# 白名单 — 优先放行的域名或完整 URL（每行一条）\n"
            "# 白名单优先级最高，即使命中黑名单也放行\n"
            "# 支持 # 开头的注释行\n"
            "# 示例:\n"
            "#   krebsonsecurity.com\n"
            "#   portswigger.net/research\n"
            "\n"
            "# === 核心安全研究站点 ===\n"
            "thehackernews.com\n"
            "bleepingcomputer.com\n"
            "krebsonsecurity.com\n"
            "schneier.com\n"
            "darkreading.com\n"
            "threatpost.com\n"
            "securityweek.com\n"
            "portswigger.net\n"
            "googleprojectzero.blogspot.com\n"
            "cisa.gov\n"
            "nist.gov\n"
            "ncsc.gov.uk\n"
            "enisa.europa.eu\n"
            "\n"
            "# === 漏洞数据库 ===\n"
            "exploit-db.com\n"
            "cve.mitre.org\n"
            "nvd.nist.gov\n"
            "vuldb.com\n"
            "opencve.io\n"
            "packetstormsecurity.com\n"
            "\n"
            "# === 中国安全社区 ===\n"
            "freebuf.com\n"
            "anquanke.com\n"
            "4hou.com\n"
            "sec-wiki.com\n"
            "52pojie.cn\n"
            "security.tencent.com\n",
            encoding="utf-8",
        )


def init_config_file(path=None):
    """生成默认配置文件"""
    p = Path(path) if path else DEFAULT_CONFIG_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(DEFAULT_CONFIG, f, ensure_ascii=False, indent=2)
    print(f"  ✅ 默认配置文件已生成: {p}")
    return p


def load_config(config_path=None):
    """加载配置文件，不存在则自动生成默认"""
    if config_path:
        p = Path(config_path)
    else:
        p = DEFAULT_CONFIG_PATH

    if not p.exists():
        print(f"  ⚠️ 配置文件不存在，自动生成默认配置: {p}")
        init_config_file(p)

    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def merge_cli_args(config, args):
    """将 CLI 参数合并到配置中（CLI 优先级高于配置文件）"""
    if args.years:
        config["crawl"]["years"] = [int(y.strip()) for y in args.years.split(",")]
    if args.max_pages is not None:
        config["crawl"]["max_pages_per_site"] = args.max_pages
    if args.max_chars is not None:
        config["content"]["max_chars"] = args.max_chars
    if args.cn_keywords:
        config["sources"]["cn_keywords"] = [k.strip() for k in args.cn_keywords.split(",")]
    if args.en_keywords:
        config["sources"]["en_keywords"] = [k.strip() for k in args.en_keywords.split(",")]
    if args.skip_search:
        config["crawl"]["enable_keyword_search"] = False
    if args.skip_sites:
        config["crawl"]["enable_site_crawl"] = False
    return config


# ==================== 黑白名单 ====================
def load_list_file(filepath):
    """加载黑白名单文件，返回纯域名/URL 列表（跳过注释和空行）"""
    if not filepath.exists():
        return []
    lines = []
    for line in filepath.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            lines.append(stripped)
    return lines


def url_in_list(url, entries):
    """检查 URL 是否匹配列表中的任一条目（域名或完整 URL）"""
    url_lower = url.lower()
    for entry in entries:
        entry_lower = entry.lower()
        if entry_lower in url_lower:
            return True
    return False


def is_whitelisted(url):
    """白名单优先检查"""
    whitelist = load_list_file(WHITELIST_FILE)
    return url_in_list(url, whitelist)


def is_blacklisted(url):
    """黑名单检查"""
    blacklist = load_list_file(BLACKLIST_FILE)
    return url_in_list(url, blacklist)


def is_likely_irrelevant(url):
    """硬编码的无关域名兜底规则"""
    irrelevant = [
        "amazon.", "ebay.", "etsy.", "walmart.", "shopify.",
        "priceoye.", "daraz.", "alibaba.", "aliexpress.",
        "youtube.com/watch", "youtu.be/",
        "facebook.com", "instagram.com", "tiktok.com",
        "pinterest.", "twitter.com",
    ]
    url_lower = url.lower()
    for domain in irrelevant:
        if domain in url_lower:
            return True
    return False


def should_skip_url(url):
    """综合判断是否跳过 URL
    优先级: 白名单 > 黑名单 > 硬编码规则
    """
    if is_whitelisted(url):
        return False
    if is_blacklisted(url):
        return True
    if is_likely_irrelevant(url):
        return True
    return False


# ==================== URL 去重 ====================
def load_crawled_urls():
    """加载已爬取 URL 记录"""
    if not CRAWLED_URLS_FILE.exists():
        return {}
    try:
        return json.loads(CRAWLED_URLS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def is_url_crawled(url):
    """检查 URL 是否已爬取过"""
    crawled = load_crawled_urls()
    return url in crawled


def mark_url_crawled(url, title="", success=True, source=""):
    """标记 URL 为已爬取"""
    crawled = load_crawled_urls()
    crawled[url] = {
        "title": title[:200] if title else "",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "success": success,
        "source": source,
    }
    CRAWLED_URLS_FILE.write_text(
        json.dumps(crawled, ensure_ascii=False, indent=2), encoding="utf-8"
    )


# ==================== 失败日志 ====================
def log_error_url(url, reason=""):
    """记录爬取失败的 URL"""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {url} | {reason}\n"
    with open(ERROR_URLS_FILE, "a", encoding="utf-8") as f:
        f.write(line)


# ==================== 暂停控制 ====================
def check_pause():
    """检查暂停标志，如果存在则等待直到标志被移除"""
    while PAUSE_FILE.exists():
        print("  ⏸️  爬虫已暂停，等待继续...（删除 pause.flag 恢复）")
        time.sleep(2)
    # 检查是否已被终止（进程被外部 kill）
    # 这里不需要额外逻辑，因为 subprocess.kill() 会直接终止进程


# ==================== HTTP 请求 & 内容提取 ====================
def safe_get(url, timeout=25, max_retries=2, fetch_delay=2.0):
    """获取网页 HTML"""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }

    for attempt in range(max_retries):
        try:
            time.sleep(fetch_delay)
            resp = requests.get(
                url, headers=headers, timeout=timeout,
                allow_redirects=True,
            )
            if resp.status_code >= 400:
                if resp.status_code in (429, 503, 502):
                    wait = 10 * (attempt + 1)
                    print(f"    ⏳ HTTP {resp.status_code}, 等待 {wait}s...")
                    time.sleep(wait)
                    continue
                log_error_url(url, f"HTTP {resp.status_code}")
                return None

            ct = resp.headers.get("Content-Type", "")
            if "html" not in ct and "text" not in ct:
                log_error_url(url, f"非文本类型: {ct}")
                return None

            text = resp.text
            if len(text) < 500:
                if any(kw in text.lower() for kw in ["cloudflare", "challenge", "captcha", "cf-browser"]):
                    log_error_url(url, "反爬页面(Cloudflare/CAPTCHA)")
                    return None

            return text

        except requests.exceptions.Timeout:
            if attempt == max_retries - 1:
                log_error_url(url, "超时")
                return None
            time.sleep(5)
        except requests.exceptions.ConnectionError:
            if attempt == max_retries - 1:
                log_error_url(url, "连接失败")
                return None
            time.sleep(3)
        except Exception as e:
            if attempt == max_retries - 1:
                log_error_url(url, f"异常: {type(e).__name__}")
                return None
            time.sleep(3)
    return None


def extract_content(html, url=""):
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
    if HAS_BS4:
        try:
            soup = BeautifulSoup(html, "lxml" if _has_lxml() else "html.parser")
            for tag in soup(["script", "style", "nav", "footer", "header",
                             "aside", "noscript", "iframe", "form"]):
                tag.decompose()

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


def clean_text(text):
    """清洗提取的文本"""
    if not text:
        return ""
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    text = re.sub(r' {3,}', '  ', text)
    return text.strip()


def fetch_and_extract(url, config):
    """获取页面并提取正文"""
    req = config["request"]
    html = safe_get(
        url,
        timeout=req.get("timeout_seconds", 25),
        max_retries=req.get("max_retries", 2),
        fetch_delay=req.get("fetch_delay_seconds", 2.0),
    )
    if not html:
        return {"success": False, "content": "", "error": "无法获取页面"}

    content = extract_content(html, url)
    if content and len(content) > 100:
        content_cfg = config["content"]
        max_chars = content_cfg.get("max_chars", 0)
        max_bytes = content_cfg.get("max_file_bytes", 100000)

        # 只在 max_chars > 0 时才按字符截断
        if max_chars > 0 and len(content) > max_chars:
            content = content[:max_chars] + "\n\n[... 内容已截断 ...]"
        # 兜底：文件字节上限
        content_bytes = content.encode("utf-8")
        if len(content_bytes) > max_bytes:
            # 从 max_bytes 位置向前找到最近的完整字符边界
            truncated = content_bytes[:max_bytes].decode("utf-8", errors="ignore")
            content = truncated + "\n\n[... 文件过大，已截断 ...]"

        return {"success": True, "content": content, "error": None}
    else:
        return {"success": False, "content": "", "error": "无法提取有效正文"}


# ==================== 搜索 ====================
def search_duckduckgo(keyword, max_results=10, region="wt-wt"):
    """通过 DuckDuckGo 搜索关键词"""
    if not HAS_DDGS:
        print("    ❌ 搜索后端不可用（缺少 ddgs 包）")
        return []

    results = []
    ddgs_class = DDGS
    try:
        with ddgs_class() as ddgs:
            search_results = list(ddgs.text(keyword, max_results=max_results, region=region))
            for r in search_results:
                url = r.get("href", "")
                if should_skip_url(url):
                    continue
                results.append({
                    "title": r.get("title", ""),
                    "url": url,
                    "snippet": r.get("body", ""),
                })
    except Exception as e:
        print(f"    ⚠️ 搜索异常: {e}")

    return results


# ==================== 文件名 & Markdown 生成 ====================
def sanitize_filename(name):
    """生成安全的文件名"""
    name = re.sub(r'[\\/:*?"<>|]', '_', name)
    name = re.sub(r'\s+', '_', name)
    return name[:80]


def generate_markdown(result, keyword=""):
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
        md += """### 备注
页面正文抓取失败，以上搜索摘要可作为参考信息。

"""

    md += f"""---
*检索时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*搜索来源: DuckDuckGo*
"""
    return md


# ==================== 关键词搜索爬取 ====================
def crawl_keywords(keywords, lang, config):
    """爬取一组关键词的搜索结果"""
    max_results = config["crawl"]["max_results_per_keyword"]
    region = config["duckduckgo"].get("region", "wt-wt")
    fetch_delay = config["request"].get("fetch_delay_seconds", 2.0)
    force = config.get("_force", False)

    total_fetched = 0
    total_extracted = 0

    for ki, keyword in enumerate(keywords, 1):
        check_pause()

        print(f"\n{'='*60}")
        print(f"[{ki}/{len(keywords)}] [{lang}] 搜索: {keyword}")
        print(f"{'='*60}")

        search_results = search_duckduckgo(keyword, max_results, region)
        print(f"  📊 搜索结果: {len(search_results)} 条")

        if not search_results:
            continue

        kw_dirname = sanitize_filename(keyword)[:50]
        kw_dir = RESULTS_DIR / f"{lang}_{kw_dirname}"
        kw_dir.mkdir(parents=True, exist_ok=True)

        keyword_results = []
        for ri, result in enumerate(search_results):
            url = result.get("url", "")
            title = result.get("title", "无标题")[:100]
            print(f"\n  [{ri+1}/{len(search_results)}] {title}...")

            if not url:
                continue

            # 暂停检查
            check_pause()

            # 去重检查
            if not force and is_url_crawled(url):
                print(f"    ⏭️  已爬取过，跳过")
                continue

            extraction = fetch_and_extract(url, config)
            result["fetch_success"] = extraction["success"]
            result["full_content"] = extraction["content"]

            if extraction["success"]:
                total_extracted += 1
                print(f"    ✅ 正文提取成功 ({len(extraction['content'])} 字符)")
            else:
                print(f"    ⚠️ {extraction['error']}")

            total_fetched += 1
            mark_url_crawled(url, title, extraction["success"], f"search:{keyword}")

            # 生成 Markdown
            md_content = generate_markdown(result, keyword)
            url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
            file_name = f"{sanitize_filename(title)[:60]}_{url_hash}.md"
            (kw_dir / file_name).write_text(md_content, encoding="utf-8")

            keyword_results.append(result)

        # 保存关键词汇总 JSON
        summary = {
            "keyword": keyword,
            "language": lang,
            "searched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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
        (kw_dir / "_summary.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    return total_fetched, total_extracted


# ==================== 站点直爬 ====================
def crawl_security_site(site_cfg, config):
    """爬取单个安全站点"""
    name = site_cfg.get("name", "unknown")
    url = site_cfg.get("url", "")
    max_pages = config["crawl"]["max_pages_per_site"]
    force = config.get("_force", False)

    print(f"\n  站点: {name} ({url})")

    check_pause()

    html = safe_get(
        url,
        timeout=config["request"].get("timeout_seconds", 25),
        max_retries=config["request"].get("max_retries", 2),
        fetch_delay=config["request"].get("fetch_delay_seconds", 2.0),
    )
    if not html:
        print(f"    ⚠️ 无法获取页面")
        log_error_url(url, f"站点首页无法访问: {name}")
        return []

    if not HAS_BS4:
        print(f"    ⚠️ BeautifulSoup 未安装，无法解析页面")
        return []

    articles = []
    try:
        soup = BeautifulSoup(html, "lxml" if _has_lxml() else "html.parser")

        # 收集文章链接
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            text = a.get_text(strip=True)
            if text and len(text) > 10:
                from urllib.parse import urljoin
                abs_url = urljoin(url, href)
                if should_skip_url(abs_url):
                    continue
                links.append({"title": text[:120], "url": abs_url})

        # 去重
        seen = set()
        unique_links = []
        for link in links:
            if link["url"] not in seen:
                seen.add(link["url"])
                unique_links.append(link)
            if len(unique_links) >= max_pages * 2:  # 多取一些做候选
                break

        print(f"    发现 {len(unique_links)} 个链接，将抓取最多 {max_pages} 篇")

        crawled_count = 0
        for li, link in enumerate(unique_links):
            if crawled_count >= max_pages:
                break

            # 去重检查
            if not force and is_url_crawled(link["url"]):
                print(f"    [{li+1}] ⏭️ 已爬取: {link['title'][:50]}...")
                continue

            # 暂停检查
            check_pause()

            print(f"    [{li+1}] {link['title'][:60]}...")
            extraction = fetch_and_extract(link["url"], config)
            link["fetch_success"] = extraction["success"]
            link["full_content"] = extraction["content"]
            articles.append(link)
            crawled_count += 1

            mark_url_crawled(link["url"], link["title"], extraction["success"], f"site:{name}")

            if extraction["success"]:
                print(f"      ✅ 正文提取成功 ({len(extraction['content'])} 字符)")
            else:
                print(f"      ⚠️ {extraction['error']}")

    except Exception as e:
        print(f"    ⚠️ 解析失败: {e}")
        log_error_url(url, f"解析异常: {type(e).__name__}")

    return articles


def save_site_articles(articles, site_name, config):
    """保存站点爬取的文章"""
    content_cfg = config["content"]
    max_chars = content_cfg.get("max_chars", 0)
    max_bytes = content_cfg.get("max_file_bytes", 100000)

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

        # 应用长度限制
        if max_chars > 0 and len(content) > max_chars:
            content = content[:max_chars] + "\n\n[... 内容已截断 ...]"
        content_bytes = content.encode("utf-8")
        if len(content_bytes) > max_bytes:
            content = content_bytes[:max_bytes].decode("utf-8", errors="ignore")
            content += "\n\n[... 文件过大，已截断 ...]"

        md = f"""# {title}

### 来源信息
- **URL**: {url}
- **来源站点**: {site_name}
- **页面抓取**: 成功

### 页面正文
{content}

---
*爬取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*来源: 直接站点爬取*
"""
        url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
        file_name = f"{sanitize_filename(title)[:60]}_{url_hash}.md"
        (site_dir / file_name).write_text(md, encoding="utf-8")
        saved += 1

    # Summary
    summary = {
        "site": site_name,
        "crawled_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_found": len(articles),
        "saved": saved,
        "articles": [
            {"title": a.get("title"), "url": a.get("url")}
            for a in articles if a.get("fetch_success")
        ],
    }
    (site_dir / "_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return saved


# ==================== 索引生成 ====================
def generate_index():
    """生成互联网检索总索引"""
    all_summaries = []
    for summary_file in sorted(RESULTS_DIR.glob("*/_summary.json")):
        try:
            all_summaries.append(json.loads(summary_file.read_text(encoding="utf-8")))
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
            name = s.get("site", "")[:50]
            lang = "site"
            total = s.get("total_found", 0)
            fetched = s.get("saved", 0)
        else:
            name = s.get("keyword", "")[:50]
            lang = s.get("language", "unknown")
            total = s.get("total_results", 0)
            fetched = s.get("fetched_count", 0)
        index += f"| {i} | {'站点' if 'site' in s else '关键词'} | {name} | {lang} | {total} | {fetched} |\n"

    index += "\n\n## 跟踪文件\n\n"
    index += f"- 已爬取 URL 记录: `tracking/crawled_urls.json`\n"
    index += f"- 失败 URL 日志: `tracking/error_urls.log`\n"
    index += f"- 黑名单: `tracking/blacklist.txt`\n"
    index += f"- 白名单: `tracking/whitelist.txt`\n"

    (OUTPUT_DIR / "SEARCH_INDEX.md").write_text(index, encoding="utf-8")
    print(f"\n  ✅ 检索索引已保存: SEARCH_INDEX.md")


# ==================== 主流程 ====================
def main():
    parser = argparse.ArgumentParser(
        description="互联网关键词检索爬虫（配置驱动版）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python crawlers/internet_crawler.py --init-config
  python crawlers/internet_crawler.py --config my_config.json
  python crawlers/internet_crawler.py --years 2025,2026 --max-pages 20
  python crawlers/internet_crawler.py --force
        """,
    )
    parser.add_argument("--config", help="配置文件路径")
    parser.add_argument("--init-config", action="store_true", help="仅生成默认配置文件，不爬取")
    parser.add_argument("--force", action="store_true", help="忽略 URL 去重，全部重爬")
    parser.add_argument("--years", help="覆盖年份范围，逗号分隔，如 2025,2026")
    parser.add_argument("--max-pages", type=int, help="每站最大页数")
    parser.add_argument("--max-chars", type=int, help="正文最大字符数（0=不截断）")
    parser.add_argument("--cn-keywords", help="覆盖中文关键词，逗号分隔")
    parser.add_argument("--en-keywords", help="覆盖英文关键词，逗号分隔")
    parser.add_argument("--skip-search", action="store_true", help="跳过关键词搜索")
    parser.add_argument("--skip-sites", action="store_true", help="跳过站点直爬")
    args = parser.parse_args()

    # --init-config 模式
    if args.init_config:
        ensure_dirs()
        init_tracking_files()
        init_config_file(args.config)
        return

    # 加载配置
    ensure_dirs()
    init_tracking_files()
    config = load_config(args.config)
    config = merge_cli_args(config, args)
    config["_force"] = args.force

    crawl_cfg = config["crawl"]
    sources = config["sources"]

    print("=" * 60)
    print("🌐 互联网关键词检索爬虫（配置驱动版）")
    print("=" * 60)
    print(f"📂 输出目录: {OUTPUT_DIR}")
    print(f"📝 配置文件: {args.config or DEFAULT_CONFIG_PATH}")
    print(f"📅 年份范围: {crawl_cfg['years']}")
    print(f"📄 正文长度限制: {config['content']['max_chars']} 字符 (0=不截断)")
    print(f"🔤 中文关键词: {len(sources['cn_keywords'])} 个")
    print(f"🔤 英文关键词: {len(sources['en_keywords'])} 个")
    print(f"📡 安全站点: {len(sources['security_sites'])} 个")
    print(f"📊 每站最多: {crawl_cfg['max_pages_per_site']} 篇")
    print(f"🔄 强制重爬: {'是' if args.force else '否'}")
    print("=" * 60)

    if not HAS_DDGS and crawl_cfg["enable_keyword_search"]:
        print("\n⚠️ 搜索后端不可用，将跳过关键词检索。")
        print("   安装: pip install ddgs")
    if not HAS_TRAFILATURA:
        print("\n⚠️ trafilatura 未安装，正文提取将使用回退方案。")
    if not HAS_BS4:
        print("\n❌ BeautifulSoup 未安装，无法运行。")
        sys.exit(1)

    total_fetched = 0
    total_extracted = 0
    site_saved = 0

    try:
        # 第一阶段：关键词检索
        if crawl_cfg["enable_keyword_search"] and HAS_DDGS:
            # 中文关键词
            print("\n" + "=" * 60)
            print("🔍 第一阶段: 中文关键词检索")
            print("=" * 60)
            f1, e1 = crawl_keywords(sources["cn_keywords"], "zh", config)
            total_fetched += f1
            total_extracted += e1

            # 英文关键词
            print("\n" + "=" * 60)
            print("🔍 第二阶段: 英文关键词检索")
            print("=" * 60)
            f2, e2 = crawl_keywords(sources["en_keywords"], "en", config)
            total_fetched += f2
            total_extracted += e2

        # 第二阶段：站点直爬
        if crawl_cfg["enable_site_crawl"]:
            print("\n" + "=" * 60)
            print("📡 第三阶段: 安全站点直接爬取")
            print("=" * 60)
            for site_cfg in sources["security_sites"]:
                articles = crawl_security_site(site_cfg, config)
                saved = save_site_articles(articles, site_cfg["name"], config)
                site_saved += saved
                print(f"    💾 保存: {saved} 篇")

    except KeyboardInterrupt:
        print("\n⚠️ 用户中断, 已抓取的数据已保存。")

    # 生成索引
    print("\n" + "=" * 60)
    print("📊 生成检索索引...")
    print("=" * 60)
    generate_index()

    # 输出统计
    print("\n" + "=" * 60)
    print("🎉 互联网关键词检索完成!")
    print(f"📊 关键词检索 — 抓取: {total_fetched}, 成功: {total_extracted}")
    print(f"📊 站点直爬 — 保存: {site_saved} 篇")
    print(f"📂 数据保存在: {OUTPUT_DIR}")
    print(f"📋 去重记录: {CRAWLED_URLS_FILE}")
    print(f"📋 失败日志: {ERROR_URLS_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()
