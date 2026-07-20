"""
Convert MITRE ATT&CK STIX JSON into structured Markdown.

Reads the enterprise-attack.json STIX bundle and exports each
attack-pattern as an independent Markdown file, filtering out
deprecated, revoked, and sub-technique entries.
"""

import argparse
import json
import logging
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts import CLEAN_DIR, DOC_DIR  # noqa: E402

logger = logging.getLogger(__name__)


def clean_description(text: str) -> str:
    """Strip residual HTML tags and normalize whitespace in a description.

    Args:
        text: Raw description string from STIX JSON.

    Returns:
        Cleaned plain-text description.
    """
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_techniques(json_path: Path, output_dir: Path) -> int:
    """Parse STIX JSON and write one .md file per attack-pattern.

    Args:
        json_path: Path to the STIX enterprise-attack.json.
        output_dir: Directory to write cleaned_*.md files.

    Returns:
        Number of techniques exported.
    """
    if not json_path.exists():
        logger.error("JSON file not found: %s", json_path)
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Loading %s ...", json_path)
    try:
        with open(json_path, "r", encoding="utf-8") as fh:
            stix_data = json.load(fh)
    except (json.JSONDecodeError, OSError) as exc:
        logger.error("Failed to load/parse JSON: %s", exc)
        return 0

    success_count = 0
    for obj in stix_data.get("objects", []):
        # Filter: only non-deprecated, non-revoked top-level attack-patterns
        if obj.get("type") != "attack-pattern":
            continue
        if obj.get("x_mitre_is_subtechnique"):
            continue
        if obj.get("deprecated") or obj.get("revoked"):
            continue

        tech_name = obj.get("name")
        raw_desc = obj.get("description", "")
        platforms = obj.get("x_mitre_platforms", [])

        # Extract ATT&CK ID (e.g. T1059)
        tech_id = "UnknownID"
        for ref in obj.get("external_references", []):
            if ref.get("source_name") == "mitre-attack":
                tech_id = ref.get("external_id", tech_id)
                break

        if not tech_name or not raw_desc:
            continue

        clean_desc = clean_description(raw_desc)
        md_content = f"""# Technique ID: {tech_id}
## Technique Name: {tech_name}

### Applicable Platforms
{', '.join(platforms) if platforms else 'General'}

### Description
{clean_desc}
"""

        fname = f"cleaned_{tech_id}.md"
        try:
            (output_dir / fname).write_text(md_content, encoding="utf-8")
            success_count += 1
        except OSError as exc:
            logger.error("Failed to write %s: %s", fname, exc)

    return success_count


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert ATT&CK STIX JSON to Markdown")
    parser.add_argument(
        "--input",
        type=Path,
        default=DOC_DIR / "attck" / "attack-stix-data-master" / "enterprise-attack" / "enterprise-attack.json",
        help="Path to enterprise-attack.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=CLEAN_DIR / "attck",
        help="Output directory for cleaned Markdown files",
    )
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(message)s",
    )

    logger.info("Extracting ATT&CK techniques from: %s", args.input)
    logger.info("=" * 50)

    count = extract_techniques(args.input, args.output)

    logger.info("=" * 50)
    logger.info("Done. Exported %d techniques → %s", count, args.output)


if __name__ == "__main__":
    main()
