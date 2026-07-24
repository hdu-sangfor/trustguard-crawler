"""
互联网爬虫可视化界面
本地启动 Web 服务，浏览器操作爬虫配置、管理黑白名单、查看爬取结果。

启动:
  python crawlers/web_ui.py
  python crawlers/web_ui.py --port 8900 --host 0.0.0.0
"""
import argparse
import json
import os
import subprocess
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

try:
    from flask import Flask, request, jsonify, redirect, url_for
except ImportError:
    print("❌ Flask 未安装。请运行: pip install flask")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from crawlers import CRAWLED_DIR
from crawlers.internet_crawler import (
    OUTPUT_DIR, RESULTS_DIR, TRACKING_DIR,
    DEFAULT_CONFIG_PATH, CRAWLED_URLS_FILE, ERROR_URLS_FILE,
    BLACKLIST_FILE, WHITELIST_FILE,
    DEFAULT_CONFIG,
    ensure_dirs, init_tracking_files, init_config_file, load_config,
    load_crawled_urls, load_list_file,
)

app = Flask(__name__)

# ==================== 爬取状态管理 ====================
_crawl_status = {
    "running": False,
    "paused": False,
    "progress": "",
    "started_at": None,
    "total_fetched": 0,
    "total_extracted": 0,
    "site_saved": 0,
    "errors": [],
}
_crawl_proc = None  # subprocess 引用，用于终止
PAUSE_FILE = TRACKING_DIR / "pause.flag"


def _run_crawler(config_path=None, force=False):
    """在后台线程中运行爬虫"""
    global _crawl_status, _crawl_proc
    _crawl_status["running"] = True
    _crawl_status["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    _crawl_status["progress"] = "正在初始化..."
    _crawl_status["errors"] = []

    try:
        cmd = [sys.executable, "-u", str(PROJECT_ROOT / "crawlers" / "internet_crawler.py")]
        if config_path:
            cmd += ["--config", config_path]
        if force:
            cmd += ["--force"]

        env = os.environ.copy()
        env["PYTHONPATH"] = str(PROJECT_ROOT)
        env["PYTHONIOENCODING"] = "utf-8"
        env["PYTHONUNBUFFERED"] = "1"

        proc = subprocess.Popen(
            cmd, cwd=str(PROJECT_ROOT), env=env,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, encoding="utf-8", errors="replace",
        )

        _crawl_proc = proc
        _crawl_status["progress"] = "已启动爬虫进程，正在连接首个站点..."
        start = time.time()
        for line in proc.stdout:
            line = line.strip()
            if line:
                _crawl_status["progress"] = line
            # 如果长时间无输出，给个提示
            elapsed = time.time() - start
            if elapsed > 30 and _crawl_status["progress"] == "已启动爬虫进程，正在连接首个站点...":
                _crawl_status["progress"] = "网络连接较慢，正在等待站点响应...（可检查代理设置）"

        proc.wait()
        _crawl_status["progress"] = "✅ 爬取完成"
        _crawl_proc = None

    except Exception as e:
        _crawl_status["errors"].append(str(e))
        _crawl_status["progress"] = f"❌ 错误: {e}"
    finally:
        _crawl_status["running"] = False
        _crawl_status["paused"] = False
        _crawl_proc = None
        # 清理暂停标志
        if PAUSE_FILE.exists():
            PAUSE_FILE.unlink()


# ==================== 页面渲染 ====================
STYLE = """<style>
  :root { --bg:#0f172a; --card:#1e293b; --border:#334155; --text:#e2e8f0;
          --muted:#94a3b8; --accent:#38bdf8; --danger:#f87171; --success:#4ade80; --warn:#fbbf24; }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:system-ui,-apple-system,sans-serif; background:var(--bg); color:var(--text);
         min-height:100vh; display:flex; }
  nav { width:200px; background:var(--card); border-right:1px solid var(--border);
        padding:1rem; display:flex; flex-direction:column; gap:4px; flex-shrink:0; }
  nav a { color:var(--muted); text-decoration:none; padding:8px 12px; border-radius:6px;
          font-size:14px; transition:all .15s; }
  nav a:hover, nav a.active { color:var(--text); background:var(--border); }
  nav .brand { font-size:16px; font-weight:700; color:var(--accent); margin-bottom:12px; }
  main { flex:1; padding:2rem; overflow-y:auto; max-height:100vh; }
  h1 { font-size:22px; margin-bottom:16px; }
  h2 { font-size:18px; margin:20px 0 12px; color:var(--accent); }
  .card { background:var(--card); border:1px solid var(--border); border-radius:8px; padding:16px; margin-bottom:16px; }
  .stat-row { display:flex; gap:16px; flex-wrap:wrap; }
  .stat { background:var(--card); border:1px solid var(--border); border-radius:8px;
          padding:16px 24px; min-width:140px; text-align:center; }
  .stat .num { font-size:32px; font-weight:700; color:var(--accent); }
  .stat .label { font-size:12px; color:var(--muted); margin-top:4px; }
  table { width:100%; border-collapse:collapse; }
  th, td { padding:8px 12px; text-align:left; border-bottom:1px solid var(--border); font-size:14px; }
  th { color:var(--muted); font-weight:600; }
  button, .btn { background:var(--accent); color:#0f172a; border:none; padding:8px 20px;
                 border-radius:6px; cursor:pointer; font-weight:600; font-size:14px; }
  button:hover { opacity:.85; }
  button:disabled { opacity:.4; cursor:not-allowed; }
  button.danger { background:var(--danger); }
  button.outline { background:transparent; border:1px solid var(--border); color:var(--text); }
  input, textarea, select { background:var(--bg); border:1px solid var(--border); color:var(--text);
    padding:8px 12px; border-radius:6px; font-size:14px; width:100%; margin:4px 0 12px; }
  textarea { font-family:monospace; min-height:200px; resize:vertical; }
  label { font-size:13px; color:var(--muted); display:block; margin-top:8px; }
  .inline-label { display:inline; margin:0 8px; }
  .progress { background:var(--bg); border-radius:4px; padding:12px; margin:8px 0;
              font-family:monospace; font-size:13px; max-height:300px; overflow-y:auto; white-space:pre-wrap; }
  .flex-row { display:flex; gap:8px; align-items:center; }
  .mb { margin-bottom:12px; }
  .hint { color:var(--muted); font-size:12px; margin-bottom:8px; }
  a { color:var(--accent); text-decoration:none; }
  a:hover { text-decoration:underline; }
</style>"""

NAV_ITEMS = [
    ("/", "📊 仪表盘", "dashboard"),
    ("/config", "⚙️ 配置编辑", "config"),
    ("/sites", "📡 站点管理", "sites"),
    ("/blacklist", "🚫 黑名单", "blacklist"),
    ("/whitelist", "✅ 白名单", "whitelist"),
    ("/results", "📄 结果浏览", "results"),
    ("/errors", "⚠️ 失败日志", "errors"),
]


def render_page(title, content, active="dashboard"):
    """渲染完整 HTML 页面"""
    nav_html = '<div class="brand">🕷️ 爬虫控制台</div>'
    for url, label, key in NAV_ITEMS:
        cls = ' class="active"' if active == key else ""
        nav_html += f'<a href="{url}"{cls}>{label}</a>'

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — 爬虫控制台</title>
{STYLE}
</head>
<body>
<nav>{nav_html}</nav>
<main>{content}</main>
</body>
</html>"""


def html_escape(text):
    """简单的 HTML 转义"""
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;").replace("'", "&#39;"))


# ==================== 路由 ====================
@app.route("/")
def dashboard():
    ensure_dirs()
    crawled = load_crawled_urls()
    total_files = sum(1 for _ in RESULTS_DIR.glob("**/*.md")) if RESULTS_DIR.exists() else 0
    total_chars = 0
    if RESULTS_DIR.exists():
        for md_file in RESULTS_DIR.glob("**/*.md"):
            try:
                total_chars += len(md_file.read_text(encoding="utf-8"))
            except Exception:
                pass

    error_count = 0
    if ERROR_URLS_FILE.exists():
        try:
            content = ERROR_URLS_FILE.read_text(encoding="utf-8")
            error_count = len([l for l in content.splitlines() if l.strip() and not l.startswith("#")])
        except Exception:
            pass

    recent_rows = ""
    if RESULTS_DIR.exists():
        for d in sorted(RESULTS_DIR.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True)[:10]:
            if d.is_dir():
                fc = sum(1 for _ in d.glob("*.md"))
                mt = datetime.fromtimestamp(d.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
                recent_rows += f"<tr><td>{d.name}</td><td>{fc}</td><td>{mt}</td></tr>"

    crawl_running = _crawl_status["running"]
    crawl_paused = _crawl_status["paused"]

    if crawl_running:
        crawl_btn = '<button type="submit" disabled>⏳ 爬取中...</button>'
        force_btn = '<button type="submit" class="outline" disabled>🔄 强制重爬</button>'
        pause_label = '▶ 继续' if crawl_paused else '⏸️ 暂停'
        pause_btn = f'<form method="post" action="/toggle-pause" style="display:inline"><button type="submit" class="outline">{pause_label}</button></form>'
        stop_btn = '<form method="post" action="/stop-crawl" style="display:inline"><button type="submit" class="danger">⏹ 终止</button></form>'
    else:
        crawl_btn = '<button type="submit">▶ 启动爬取</button>'
        force_btn = '<button type="submit" class="outline">🔄 强制重爬</button>'
        pause_btn = ''
        stop_btn = ''

    progress_html = ""
    if crawl_running:
        progress_html = f"""<div class="progress" id="progress">{html_escape(_crawl_status['progress'])}</div>
<script>setInterval(function(){{fetch('/crawl-status').then(r=>r.json()).then(d=>{{document.getElementById('progress').textContent=d.progress;if(!d.running)location.reload();}});}},2000);</script>"""

    content = f"""<h1>📊 仪表盘</h1>
<div class="stat-row">
  <div class="stat"><div class="num">{total_files}</div><div class="label">已爬取文件</div></div>
  <div class="stat"><div class="num">{len(crawled)}</div><div class="label">已记录 URL</div></div>
  <div class="stat"><div class="num">{error_count}</div><div class="label">失败 URL</div></div>
  <div class="stat"><div class="num">{total_chars:,}</div><div class="label">总字符数</div></div>
</div>
<div class="card">
  <h2>爬取控制</h2>
  <div class="flex-row mb">
    <form method="post" action="/start-crawl" style="display:inline">{crawl_btn}</form>
    <form method="post" action="/start-crawl" style="display:inline"><input type="hidden" name="force" value="1">{force_btn}</form>
    {pause_btn}
    {stop_btn}
  </div>
  {progress_html}
</div>
<div class="card">
  <h2>最近爬取结果</h2>
  <table><tr><th>目录</th><th>文件数</th><th>最后修改</th></tr>{recent_rows}</table>
</div>"""
    return render_page("仪表盘", content, "dashboard")


@app.route("/start-crawl", methods=["POST"])
def start_crawl():
    if _crawl_status["running"]:
        return redirect(url_for("dashboard"))
    force = request.form.get("force") == "1"
    config_path = str(DEFAULT_CONFIG_PATH) if DEFAULT_CONFIG_PATH.exists() else None
    t = threading.Thread(target=_run_crawler, args=(config_path, force), daemon=True)
    t.start()
    time.sleep(1)
    return redirect(url_for("dashboard"))


@app.route("/stop-crawl", methods=["POST"])
def stop_crawl():
    global _crawl_proc, _crawl_status
    if _crawl_proc is not None:
        _crawl_proc.terminate()
        _crawl_proc = None
    _crawl_status["running"] = False
    _crawl_status["paused"] = False
    _crawl_status["progress"] = "⏹️ 用户手动停止"
    # 清理暂停标志
    if PAUSE_FILE.exists():
        PAUSE_FILE.unlink()
    return redirect(url_for("dashboard"))


@app.route("/toggle-pause", methods=["POST"])
def toggle_pause():
    global _crawl_status
    if not _crawl_status["running"]:
        return redirect(url_for("dashboard"))

    if _crawl_status["paused"]:
        # 恢复：删除暂停标志文件
        if PAUSE_FILE.exists():
            PAUSE_FILE.unlink()
        _crawl_status["paused"] = False
        _crawl_status["progress"] = "▶️ 已恢复爬取"
    else:
        # 暂停：创建暂停标志文件
        PAUSE_FILE.write_text("pause", encoding="utf-8")
        _crawl_status["paused"] = True
        _crawl_status["progress"] = "⏸️ 已暂停，等待当前请求完成后生效..."
    return redirect(url_for("dashboard"))


@app.route("/crawl-status")
def crawl_status():
    return jsonify({
        "running": _crawl_status["running"],
        "paused": _crawl_status["paused"],
        "progress": _crawl_status["progress"],
        "total_fetched": _crawl_status["total_fetched"],
        "total_extracted": _crawl_status["total_extracted"],
        "site_saved": _crawl_status["site_saved"],
    })


@app.route("/config")
def config_page():
    ensure_dirs()
    cfg = load_config(str(DEFAULT_CONFIG_PATH)) if DEFAULT_CONFIG_PATH.exists() else DEFAULT_CONFIG
    c = cfg["crawl"]
    ct = cfg["content"]
    rq = cfg["request"]

    kw_checked = "checked" if c["enable_keyword_search"] else ""
    site_checked = "checked" if c["enable_site_crawl"] else ""

    content = f"""<h1>⚙️ 配置编辑</h1>
<form method="post" action="/save-config">
  <div class="card">
    <h2>爬取参数</h2>
    <label>年份范围（逗号分隔）</label>
    <input name="years" value="{','.join(str(y) for y in c['years'])}">
    <label>每关键词最大结果数</label>
    <input name="max_results_per_keyword" type="number" value="{c['max_results_per_keyword']}">
    <label>每站最大页数</label>
    <input name="max_pages_per_site" type="number" value="{c['max_pages_per_site']}">
    <div class="flex-row mb">
      <label class="inline-label"><input type="checkbox" name="enable_keyword_search" {kw_checked}> 启用关键词搜索</label>
      <label class="inline-label"><input type="checkbox" name="enable_site_crawl" {site_checked}> 启用站点直爬</label>
    </div>
  </div>
  <div class="card">
    <h2>正文长度</h2>
    <label>最大字符数（0=不截断）</label>
    <input name="max_chars" type="number" value="{ct['max_chars']}">
    <label>最大文件字节数（兜底）</label>
    <input name="max_file_bytes" type="number" value="{ct['max_file_bytes']}">
  </div>
  <div class="card">
    <h2>请求参数</h2>
    <label>请求间隔（秒）</label>
    <input name="delay_seconds" type="number" step="0.5" value="{rq['delay_seconds']}">
    <label>抓取间隔（秒）</label>
    <input name="fetch_delay_seconds" type="number" step="0.5" value="{rq['fetch_delay_seconds']}">
    <label>超时（秒）</label>
    <input name="timeout_seconds" type="number" value="{rq['timeout_seconds']}">
    <label>最大重试次数</label>
    <input name="max_retries" type="number" value="{rq['max_retries']}">
  </div>
  <button type="submit">💾 保存配置</button>
</form>"""
    return render_page("配置编辑", content, "config")


@app.route("/save-config", methods=["POST"])
def save_config():
    ensure_dirs()
    cfg = load_config(str(DEFAULT_CONFIG_PATH)) if DEFAULT_CONFIG_PATH.exists() else dict(DEFAULT_CONFIG)
    cfg["crawl"]["years"] = [int(y.strip()) for y in request.form.get("years", "2025,2026").split(",") if y.strip()]
    cfg["crawl"]["max_results_per_keyword"] = int(request.form.get("max_results_per_keyword", 20))
    cfg["crawl"]["max_pages_per_site"] = int(request.form.get("max_pages_per_site", 15))
    cfg["crawl"]["enable_keyword_search"] = request.form.get("enable_keyword_search") == "on"
    cfg["crawl"]["enable_site_crawl"] = request.form.get("enable_site_crawl") == "on"
    cfg["content"]["max_chars"] = int(request.form.get("max_chars", 0))
    cfg["content"]["max_file_bytes"] = int(request.form.get("max_file_bytes", 100000))
    cfg["request"]["delay_seconds"] = float(request.form.get("delay_seconds", 3.0))
    cfg["request"]["fetch_delay_seconds"] = float(request.form.get("fetch_delay_seconds", 2.0))
    cfg["request"]["timeout_seconds"] = int(request.form.get("timeout_seconds", 25))
    cfg["request"]["max_retries"] = int(request.form.get("max_retries", 2))
    DEFAULT_CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DEFAULT_CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    return redirect(url_for("config_page"))


@app.route("/sites")
def sites_page():
    ensure_dirs()
    cfg = load_config(str(DEFAULT_CONFIG_PATH)) if DEFAULT_CONFIG_PATH.exists() else DEFAULT_CONFIG
    sites_json = json.dumps(cfg["sources"]["security_sites"], ensure_ascii=False, indent=2)
    cn_kw = "\n".join(cfg["sources"]["cn_keywords"])
    en_kw = "\n".join(cfg["sources"]["en_keywords"])
    ns = len(cfg["sources"]["security_sites"])
    nc = len(cfg["sources"]["cn_keywords"])
    ne = len(cfg["sources"]["en_keywords"])

    content = f"""<h1>📡 站点 & 关键词管理</h1>
<div class="card">
  <h2>安全站点 ({ns})</h2>
  <form method="post" action="/save-sites">
    <textarea name="sites_json" style="min-height:500px">{html_escape(sites_json)}</textarea>
    <p class="hint">JSON 数组，每项含 name 和 url 字段。直接编辑后保存。</p>
    <button type="submit">💾 保存站点列表</button>
  </form>
</div>
<div class="card">
  <h2>中文关键词 ({nc})</h2>
  <form method="post" action="/save-keywords">
    <input type="hidden" name="lang" value="cn">
    <textarea name="keywords" style="min-height:200px">{html_escape(cn_kw)}</textarea>
    <p class="hint">每行一个关键词</p>
    <button type="submit">💾 保存中文关键词</button>
  </form>
</div>
<div class="card">
  <h2>英文关键词 ({ne})</h2>
  <form method="post" action="/save-keywords">
    <input type="hidden" name="lang" value="en">
    <textarea name="keywords" style="min-height:200px">{html_escape(en_kw)}</textarea>
    <p class="hint">每行一个关键词</p>
    <button type="submit">💾 保存英文关键词</button>
  </form>
</div>"""
    return render_page("站点管理", content, "sites")


@app.route("/save-sites", methods=["POST"])
def save_sites():
    ensure_dirs()
    cfg = load_config(str(DEFAULT_CONFIG_PATH)) if DEFAULT_CONFIG_PATH.exists() else dict(DEFAULT_CONFIG)
    try:
        sites = json.loads(request.form.get("sites_json", "[]"))
        cfg["sources"]["security_sites"] = sites
        with open(DEFAULT_CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)
    except json.JSONDecodeError as e:
        return f"JSON 格式错误: {e}", 400
    return redirect(url_for("sites_page"))


@app.route("/save-keywords", methods=["POST"])
def save_keywords():
    ensure_dirs()
    cfg = load_config(str(DEFAULT_CONFIG_PATH)) if DEFAULT_CONFIG_PATH.exists() else dict(DEFAULT_CONFIG)
    lang = request.form.get("lang", "cn")
    keywords = [k.strip() for k in request.form.get("keywords", "").splitlines() if k.strip()]
    key = "cn_keywords" if lang == "cn" else "en_keywords"
    cfg["sources"][key] = keywords
    with open(DEFAULT_CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    return redirect(url_for("sites_page"))


@app.route("/blacklist")
def blacklist_page():
    ensure_dirs()
    init_tracking_files()
    raw = BLACKLIST_FILE.read_text(encoding="utf-8") if BLACKLIST_FILE.exists() else ""
    content = f"""<h1>🚫 黑名单</h1>
<p class="hint">每行一个域名或完整 URL，永不爬取。# 开头为注释。优先级：白名单 &gt; 黑名单 &gt; 硬编码规则。</p>
<form method="post" action="/save-blacklist">
  <textarea name="content" style="min-height:400px">{html_escape(raw)}</textarea>
  <button type="submit">💾 保存黑名单</button>
</form>"""
    return render_page("黑名单", content, "blacklist")


@app.route("/save-blacklist", methods=["POST"])
def save_blacklist():
    ensure_dirs()
    init_tracking_files()
    BLACKLIST_FILE.write_text(request.form.get("content", ""), encoding="utf-8")
    return redirect(url_for("blacklist_page"))


@app.route("/whitelist")
def whitelist_page():
    ensure_dirs()
    init_tracking_files()
    raw = WHITELIST_FILE.read_text(encoding="utf-8") if WHITELIST_FILE.exists() else ""
    content = f"""<h1>✅ 白名单</h1>
<p class="hint">每行一个域名或完整 URL，优先放行（即使命中黑名单也放行）。# 开头为注释。</p>
<form method="post" action="/save-whitelist">
  <textarea name="content" style="min-height:400px">{html_escape(raw)}</textarea>
  <button type="submit">💾 保存白名单</button>
</form>"""
    return render_page("白名单", content, "whitelist")


@app.route("/save-whitelist", methods=["POST"])
def save_whitelist():
    ensure_dirs()
    init_tracking_files()
    WHITELIST_FILE.write_text(request.form.get("content", ""), encoding="utf-8")
    return redirect(url_for("whitelist_page"))


@app.route("/results")
def results_page():
    ensure_dirs()
    rows = ""
    if RESULTS_DIR.exists():
        for d in sorted(RESULTS_DIR.iterdir()):
            if d.is_dir():
                md_count = sum(1 for _ in d.glob("*.md"))
                json_count = sum(1 for _ in d.glob("*.json"))
                rel = d.relative_to(RESULTS_DIR).as_posix()
                rows += f'<tr><td><a href="/results/{rel}">{d.name}</a></td><td>{md_count}</td><td>{json_count}</td></tr>'

    content = f"""<h1>📄 结果浏览</h1>
<div class="card">
  <h2>已爬取目录</h2>
  <table><tr><th>目录名</th><th>Markdown 文件数</th><th>JSON 文件数</th></tr>{rows}</table>
</div>"""
    return render_page("结果浏览", content, "results")


@app.route("/results/<path:relpath>")
def results_detail(relpath):
    d = RESULTS_DIR / relpath
    if not d.exists() or not d.is_dir():
        return "目录不存在", 404
    rows = ""
    for f in sorted(d.iterdir()):
        if f.is_file():
            size_kb = f"{f.stat().st_size / 1024:.1f}"
            if f.name.endswith('.md'):
                view_link = f'<a href="/view-file?path={f.absolute().as_posix()}">查看</a>'
            else:
                view_link = ""
            rows += f"<tr><td>{f.name}</td><td>{size_kb} KB</td><td>{view_link}</td></tr>"

    content = f"""<h1>📄 {d.name}</h1>
<div class="card">
  <table><tr><th>文件名</th><th>大小</th><th>操作</th></tr>{rows}</table>
</div>
<a href="/results">← 返回</a>"""
    return render_page(d.name, content, "results")


@app.route("/view-file")
def view_file():
    path = request.args.get("path", "")
    p = Path(path)
    if not p.exists() or not p.is_file():
        return "文件不存在", 404
    try:
        p.resolve().relative_to(RESULTS_DIR.resolve())
    except ValueError:
        return "无权访问", 403
    raw = p.read_text(encoding="utf-8")
    content = f"""<h1>{p.name}</h1>
<div class="card">
  <pre style="white-space:pre-wrap;font-family:monospace;font-size:13px;max-height:80vh;overflow-y:auto">{html_escape(raw)}</pre>
</div>
<a href="javascript:history.back()">← 返回</a>"""
    return render_page(p.name, content, "results")


@app.route("/errors")
def errors_page():
    ensure_dirs()
    init_tracking_files()
    raw = ERROR_URLS_FILE.read_text(encoding="utf-8") if ERROR_URLS_FILE.exists() else "（暂无失败记录）"
    content = f"""<h1>⚠️ 失败日志</h1>
<p class="hint">以下 URL 在爬取过程中失败。文件位置: {ERROR_URLS_FILE}</p>
<div class="card">
  <pre style="white-space:pre-wrap;font-family:monospace;font-size:13px;max-height:80vh;overflow-y:auto">{html_escape(raw)}</pre>
</div>"""
    return render_page("失败日志", content, "errors")


# ==================== 启动 ====================
def main():
    parser = argparse.ArgumentParser(description="互联网爬虫 Web 控制台")
    parser.add_argument("--port", type=int, default=8899)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()

    ensure_dirs()
    init_tracking_files()
    if not DEFAULT_CONFIG_PATH.exists():
        init_config_file()

    print(f"""
╔══════════════════════════════════════╗
║   🕷️  互联网爬虫 Web 控制台         ║
║                                      ║
║   浏览器打开: http://{args.host}:{args.port}  ║
║   按 Ctrl+C 停止                     ║
╚══════════════════════════════════════╝
""")
    app.run(host=args.host, port=args.port, debug=False)


if __name__ == "__main__":
    main()
