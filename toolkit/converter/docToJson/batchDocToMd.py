#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch DOC to Markdown Converter
Scans a folder for DOC files and converts them to Markdown
"""

from pathlib import Path

try:
    import textract
except ImportError:
    print("Error: textract package is required.")
    print("Install with: pip install textract")
    print("Or on Ubuntu/Debian, you may also need: apt-get install antiword")
    exit(1)


def doc_to_markdown(doc_path: str) -> str:
    """Convert a DOC file to Markdown string."""
    # Extract text from DOC file using textract
    try:
        text = textract.process(doc_path).decode('utf-8')
    except Exception as e:
        raise Exception(f"Failed to extract text from {doc_path}: {str(e)}")

    # Convert plain text to basic markdown format
    markdown_lines = []

    for line in text.split('\n'):
        stripped_line = line.strip()
        if not stripped_line:
            markdown_lines.append("")
            continue

        # Detect potential headings (all caps or followed by multiple blank lines)
        if stripped_line.isupper() and len(stripped_line) < 80:
            markdown_lines.append(f"## {stripped_line}")
        else:
            markdown_lines.append(stripped_line)

    return "\n".join(markdown_lines)


def convert_folder(source_dir: str, target_dir: str) -> None:
    """
    Scan source folder for DOC files and convert them to Markdown.

    Args:
        source_dir: Directory containing DOC files
        target_dir: Directory to save Markdown files
    """
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    # Create target directory if it doesn't exist
    target_path.mkdir(parents=True, exist_ok=True)

    # Find all DOC files (old format .doc)
    doc_files = list(source_path.glob("*.doc"))

    if not doc_files:
        print(f"No DOC files found in {source_dir}")
        return

    print(f"Found {len(doc_files)} DOC file(s)")
    print("\nUsing textract library to extract text from .doc files...")

    # Convert each DOC file
    success_count = 0
    error_count = 0

    for doc_file in doc_files:
        try:
            print(f"\nConverting: {doc_file.name}")

            # Convert to markdown
            markdown_content = doc_to_markdown(str(doc_file))

            # Generate output filename (same name but .md extension)
            md_filename = doc_file.stem + ".md"
            md_path = target_path / md_filename

            # Write markdown file
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            print(f"  ✓ Saved to: {md_path}")
            success_count += 1

        except Exception as e:
            print(f"  ✗ Error converting {doc_file.name}: {str(e)}")
            error_count += 1

    print(f"\nConversion complete: {success_count} succeeded, {error_count} failed")


if __name__ == "__main__":
    SOURCE_DIR = "/workspace/zbackup/sources"
    TARGET_DIR = "/workspace/dlake/edu/english/pschool"

    convert_folder(SOURCE_DIR, TARGET_DIR)
