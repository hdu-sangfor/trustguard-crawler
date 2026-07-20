"""
Clean OWASP Top 10 Markdown files.

Strips front matter, HTML tags, image links, and normalizes whitespace
from raw OWASP markdown documents into clean, structured Markdown
suitable for RAG ingestion.
"""

import argparse
import logging
import re
import sys
from pathlib import Path

# Allow running this script directly: python scripts/clean_owasp.py
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts import CLEAN_DIR, DOC_DIR  # noqa: E402

logger = logging.getLogger(__name__)


def clean_owasp_markdown(md_content: str) -> str:
    """Remove front matter, HTML, superfluous links and normalize whitespace.

    Args:
        md_content: Raw OWASP markdown content.

    Returns:
        Cleaned markdown text.
    """
    # 1. Remove Jekyll/Hugo front matter
    cleaned = re.sub(r"^---[\s\S]*?---", "", md_content)

    # 2. Remove inline HTML tags (keep text content)
    cleaned = re.sub(r"<[^>]+>", "", cleaned)

    # 3. Normalize obfuscated URLs
    cleaned = re.sub(r"hxxps?://", "https://", cleaned)
    cleaned = re.sub(r"\[\.\]", ".", cleaned)

    # 4. Collapse 3+ consecutive newlines into 2
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)

    # 5. Remove Markdown image links ![...](...)
    cleaned = re.sub(r"!\[.*?\]\(.*?\)", "", cleaned)

    # 6. Convert Markdown links [text](url) to plain text
    cleaned = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", cleaned)

    # 7. Strip table formatting separators
    cleaned = re.sub(r"\|[\s:-|]+\|", "", cleaned)

    return cleaned.strip()


def process_folder(input_dir: Path, output_dir: Path) -> int:
    """Batch-clean all markdown files in a directory.

    Args:
        input_dir: Directory containing raw .md files.
        output_dir: Directory to write cleaned_*.md files.

    Returns:
        Number of files successfully cleaned.
    """
    if not input_dir.exists():
        logger.error("Input folder not found: %s", input_dir)
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)

    success_count = 0
    for filepath in sorted(input_dir.iterdir()):
        if filepath.suffix not in (".md", ".markdown"):
            continue

        try:
            raw = filepath.read_text(encoding="utf-8")
            cleaned = clean_owasp_markdown(raw)
            out_path = output_dir / f"cleaned_{filepath.name}"
            out_path.write_text(cleaned, encoding="utf-8")
            logger.info("OK  %s  →  %s  (%d chars)", filepath.name, out_path.name, len(cleaned))
            success_count += 1
        except (OSError, UnicodeDecodeError) as exc:
            logger.error("Failed processing %s: %s", filepath.name, exc)

    return success_count


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean OWASP Top 10 Markdown files")
    parser.add_argument(
        "--input",
        type=Path,
        default=DOC_DIR / "owasp" / "Top10-master" / "2017" / "en",
        help="Input directory containing raw .md files",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=CLEAN_DIR / "owasp" / "2017" / "en",
        help="Output directory for cleaned files",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(message)s",
    )

    logger.info("Cleaning OWASP Markdown from: %s", args.input)
    logger.info("=" * 50)

    count = process_folder(args.input, args.output)

    logger.info("=" * 50)
    logger.info("Done. Cleaned %d files → %s", count, args.output)


if __name__ == "__main__":
    main()
