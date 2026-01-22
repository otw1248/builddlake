#!/usr/bin/env python3
"""
Created by AI Assistant
Date: 2026-01-21
"""

def sort_and_deduplicate(input_file, output_file=None):
    """
    Sort file content and remove duplicate lines.

    Args:
        input_file: Path to the input file
        output_file: Path to the output file (optional, overwrites input if not provided)
    """
    # Read the file and filter out empty lines
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line for line in f if line.strip()]

    # Remove duplicates and sort
    unique_lines = sorted(set(lines), key=lambda x: x.strip())

    # Determine output file
    if output_file is None:
        output_file = input_file

    # Write the cleaned and sorted content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(unique_lines)

    print(f"Sorted and deduplicated: {input_file}")
    print(f"Original lines: {len(lines)}, Unique lines: {len(unique_lines)}")
    print(f"Output saved to: {output_file}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python sort_and_deduplicate.py <input_file> [output_file]")
        print("Example: python /workspace/dlake/ss/log/sort_and_deduplicate.py /workspace/dlake/ss/log/ss-log-2601.log.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    sort_and_deduplicate(input_file, output_file)
