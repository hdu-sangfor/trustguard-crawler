"""
Convert CVE JSON (cvelistV5 format) into structured Markdown.

Recursively walks a directory tree of CVE JSON files and exports each
valid CVE as a cleaned_*.md file, filtering out REJECTED/RESERVED entries.
"""

import argparse
import json
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts import CLEAN_DIR, DOC_DIR  # noqa: E402

logger = logging.getLogger(__name__)


def convert_single_cve(json_path: Path, output_dir: Path) -> bool:
    """Convert one CVE JSON file to Markdown.

    Args:
        json_path: Path to a single CVE JSON file.
        output_dir: Directory to write the output Markdown.

    Returns:
        True if the CVE was valid and exported, False otherwise.
    """
    try:
        with open(json_path, "r", encoding="utf-8") as fh:
            cve_data = json.load(fh)
    except (json.JSONDecodeError, OSError) as exc:
        logger.warning("Skipping %s: %s", json_path.name, exc)
        return False

    # Extract CVE ID
    cve_metadata = cve_data.get("cveMetadata", {})
    cve_id = cve_metadata.get("cveId")
    if not cve_id:
        return False

    # Extract CNA container data
    containers = cve_data.get("containers", {})
    cna = containers.get("cna", {})

    title = cna.get("title", "No title")

    # Extract English description
    descriptions = cna.get("descriptions", [])
    eng_desc = ""
    for desc in descriptions:
        lang = desc.get("lang", "")
        if lang == "en" or lang.startswith("en"):
            eng_desc = desc.get("value", "")
            break
    if not eng_desc and descriptions:
        eng_desc = descriptions[0].get("value", "")

    # Filter out uninteresting entries
    if not eng_desc or "REJECTED" in eng_desc or "RESERVED" in eng_desc:
        return False

    md_content = f"""# CVE ID: {cve_id}
## Title: {title}

### Description
{eng_desc.strip()}
"""

    fname = f"cleaned_{cve_id}.md"
    try:
        (output_dir / fname).write_text(md_content, encoding="utf-8")
        return True
    except OSError as exc:
        logger.error("Write failed for %s: %s", fname, exc)
        return False


def process_tree(input_dir: Path, output_dir: Path) -> tuple[int, int]:
    """Recursively walk a directory tree and convert all CVE JSON files.

    Args:
        input_dir: Root directory containing CVE JSON files (e.g. .../cves/2026).
        output_dir: Directory to write cleaned Markdown files.

    Returns:
        Tuple of (scanned_count, success_count).
    """
    if not input_dir.exists():
        logger.error("Input directory not found: %s", input_dir)
        return 0, 0

    output_dir.mkdir(parents=True, exist_ok=True)

    scanned = 0
    succeeded = 0
    for root, _dirs, files in input_dir.walk():
        for filename in files:
            if not filename.endswith(".json"):
                continue
            scanned += 1
            if convert_single_cve(root / filename, output_dir):
                succeeded += 1
            if scanned % 500 == 0:
                logger.info("  Scanned %d files, exported %d ...", scanned, succeeded)

    return scanned, succeeded


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert CVE JSON to Markdown")
    parser.add_argument(
        "--input",
        type=Path,
        default=DOC_DIR / "cve" / "cvelistV5-main" / "cves" / "2026",
        help="Root directory of CVE JSON files",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=CLEAN_DIR / "cve" / "2026",
        help="Output directory for cleaned Markdown",
    )
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(message)s",
    )

    logger.info("Scanning CVE JSON files in: %s", args.input)
    logger.info("=" * 50)

    scanned, succeeded = process_tree(args.input, args.output)

    logger.info("=" * 50)
    logger.info("Done. Scanned %d JSON files, exported %d CVEs → %s", scanned, succeeded, args.output)


if __name__ == "__main__":
    main()
