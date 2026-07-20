"""
Intelligent Markdown chunker for RAG corpus preparation.

Splits cleaned Markdown files into retrieval-friendly chunks:
- Splits on heading boundaries (##) to preserve semantic units.
- Short sections are kept whole; long sections use a rolling window.
"""

import argparse
import logging
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts import CHUNKS_DIR, CLEAN_DIR  # noqa: E402

logger = logging.getLogger(__name__)


def smart_markdown_splitter(
    text: str,
    chunk_size: int = 600,
    overlap: int = 50,
) -> list[str]:
    """Split Markdown text into fixed-size chunks on heading boundaries.

    Args:
        text: Input Markdown content.
        chunk_size: Maximum characters per chunk.
        overlap: Overlap between consecutive chunks from the same section.

    Returns:
        List of chunk strings.
    """
    # Split on ## headings (level-2+)
    sections = re.split(r"\n(?=## )", text)

    chunks: list[str] = []
    for section in sections:
        section = section.strip()
        if not section:
            continue
        if len(section) <= chunk_size:
            chunks.append(section)
        else:
            # Rolling window for long sections
            start = 0
            while start < len(section):
                end = start + chunk_size
                chunks.append(section[start:end])
                if end >= len(section):
                    break
                start += chunk_size - overlap

    return chunks


def process_folder(
    input_dir: Path,
    output_dir: Path,
    chunk_size: int = 600,
    overlap: int = 50,
) -> tuple[int, int]:
    """Batch-chunk all cleaned_*.md files in a directory.

    Args:
        input_dir: Directory containing cleaned_*.md files.
        output_dir: Root directory for chunk output.
        chunk_size: Characters per chunk.
        overlap: Rolling window overlap.

    Returns:
        Tuple of (files_processed, total_chunks).
    """
    if not input_dir.exists():
        logger.error("Input folder not found: %s", input_dir)
        return 0, 0

    output_dir.mkdir(parents=True, exist_ok=True)

    files_processed = 0
    total_chunks = 0

    for filepath in sorted(input_dir.iterdir()):
        if not filepath.name.startswith("cleaned_") or filepath.suffix != ".md":
            continue

        try:
            content = filepath.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            logger.error("Failed to read %s: %s", filepath.name, exc)
            continue

        chunks = smart_markdown_splitter(content, chunk_size, overlap)

        # Write each chunk into a subdirectory named after the source file
        base = filepath.stem.replace("cleaned_", "")  # strip prefix
        chunk_dir = output_dir / base
        chunk_dir.mkdir(parents=True, exist_ok=True)

        for idx, chunk in enumerate(chunks):
            chunk_path = chunk_dir / f"chunk_{idx + 1:03d}.txt"
            try:
                chunk_path.write_text(chunk, encoding="utf-8")
            except OSError as exc:
                logger.error("Write failed %s: %s", chunk_path, exc)

        logger.info("OK  %s  →  %d chunks  [%s/]", filepath.name, len(chunks), base)
        files_processed += 1
        total_chunks += len(chunks)

    return files_processed, total_chunks


def main() -> None:
    parser = argparse.ArgumentParser(description="Split cleaned Markdown into RAG chunks")
    parser.add_argument(
        "--input",
        type=Path,
        default=CLEAN_DIR / "owasp" / "2017" / "en",
        help="Directory containing cleaned_*.md files",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=CHUNKS_DIR / "owasp" / "2017" / "en",
        help="Output root directory for chunks",
    )
    parser.add_argument("--chunk-size", type=int, default=600, help="Max characters per chunk")
    parser.add_argument("--overlap", type=int, default=50, help="Rolling window overlap")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(message)s",
    )

    logger.info("Chunking files from: %s", args.input)
    logger.info("  chunk_size=%d  overlap=%d", args.chunk_size, args.overlap)
    logger.info("=" * 50)

    files, total = process_folder(args.input, args.output, args.chunk_size, args.overlap)

    logger.info("=" * 50)
    logger.info("Done. %d files → %d chunks in %s", files, total, args.output)


if __name__ == "__main__":
    main()
