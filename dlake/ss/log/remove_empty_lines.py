#!/usr/bin/env python3
"""
Created by AI Assistant
Date: 2026-01-21
"""

def remove_empty_lines(input_file, output_file=None):
    """
    Remove empty lines from a file.

    Args:
        input_file: Path to the input file
        output_file: Path to the output file (optional, overwrites input if not provided)
    """
    # Read the file and filter out empty lines
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line for line in f if line.strip()]

    # Determine output file
    if output_file is None:
        output_file = input_file

    # Write the cleaned content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"Removed empty lines from: {input_file}")
    print(f"Output saved to: {output_file}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python remove_empty_lines.py <input_file> [output_file]")
        print("Example: python remove_empty_lines.py dlake/ss/log/ss-log-2601.log.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    remove_empty_lines(input_file, output_file)
