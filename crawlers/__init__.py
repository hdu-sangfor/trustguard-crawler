"""Crawlers for cybersecurity RAG corpus collection.

Each crawler targets a specific data source and outputs structured Markdown
to the doc/crawled/ directory.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CRAWLED_DIR = PROJECT_ROOT / "doc" / "crawled"
