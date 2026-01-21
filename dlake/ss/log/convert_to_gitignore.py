#!/usr/bin/env python3
"""
Created by AI Assistant
Date: 2026-01-21
"""

def convert_to_gitignore(input_file, output_file=None):
    """
    Convert a list of paths to a properly formatted .gitignore file.

    Args:
        input_file: Path to the input file
        output_file: Path to the output file (optional, defaults to .gitignore)
    """
    # Read the file and filter out empty lines
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line for line in f if line.strip()]

    # Process and normalize paths
    normalized = []
    for line in lines:
        path = line.strip()

        # Skip comments
        if path.startswith('#'):
            normalized.append(path)
            continue

        # Skip if already properly formatted
        if path.startswith('!'):
            # Negation pattern - keep as is but remove trailing whitespace
            normalized.append('!' + path[1:].rstrip())
            continue

        # Remove leading slash if it's a single pattern (not anchored to root)
        # In .gitignore, paths without leading slash match anywhere
        # Paths with leading slash only match from repository root
        if path.startswith('/'):
            # Keep leading slash for root-anchored patterns
            path = path.lstrip()
            # Check if it should be anchored or not
            # For files like .env, .git/config, etc., we usually want to match anywhere
            # For directories like /admin, we might want to anchor
            if '/' in path and not path.startswith('.'):
                # Contains directory separators and not a hidden file - keep anchored
                path = '/' + path
        else:
            path = path.lstrip()

        # Remove trailing slashes for files (keep for directories)
        if path.endswith('/') and '.' in path.rsplit('/', 1)[-1]:
            # It's a file with a trailing slash, remove it
            path = path.rstrip('/')

        # Normalize path separators
        path = path.replace('\\', '/')

        # Remove any duplicate consecutive slashes
        while '//' in path:
            path = path.replace('//', '/')

        # Remove trailing whitespace
        path = path.rstrip()

        if path:
            normalized.append(path)

    # Remove duplicates while preserving order
    seen = set()
    unique_lines = []
    for line in normalized:
        if line not in seen:
            seen.add(line)
            unique_lines.append(line)

    # Determine output file
    if output_file is None:
        output_file = '/workspace/.gitignore'

    # Write the .gitignore file
    with open(output_file, 'w', encoding='utf-8') as f:
        # Add header comment
        f.write("# Auto-generated gitignore file\n")
        f.write(f"# Created by AI Assistant on 2026-01-21\n")
        f.write(f"# Source: {input_file}\n")
        f.write("#\n\n")

        # Group patterns by category
        sections = {
            'System and Configuration': [],
            'Environment Files': [],
            'Git and VCS': [],
            'Database and Backups': [],
            'Logs and Temporary Files': [],
            'CI/CD and DevOps': [],
            'Security and Credentials': [],
            'Web and Framework Files': [],
            'Other': []
        }

        for line in unique_lines:
            if line.startswith('#'):
                continue

            # Categorize patterns
            path = line.lstrip('/')
            path_lower = path.lower()

            if any(x in path_lower for x in ['env', 'config', 'secret', 'credential', 'key', 'password']):
                if 'git' in path_lower or 'svn' in path_lower:
                    sections['Git and VCS'].append(line)
                elif 'db' in path_lower or 'database' in path_lower:
                    sections['Database and Backups'].append(line)
                elif 'backup' in path_lower or 'dump' in path_lower or 'sql' in path_lower:
                    sections['Database and Backups'].append(line)
                else:
                    sections['Environment Files'].append(line)
            elif any(x in path_lower for x in ['git', 'svn', 'hg']):
                sections['Git and VCS'].append(line)
            elif any(x in path_lower for x in ['log', 'tmp', 'cache', 'temp']):
                sections['Logs and Temporary Files'].append(line)
            elif any(x in path_lower for x in ['ci', 'cd', 'pipeline', 'workflow', 'jenkins', 'travis', 'circle']):
                sections['CI/CD and DevOps'].append(line)
            elif any(x in path_lower for x in ['admin', 'auth', 'token', 'vault', 'ssh', 'ssl', 'cert']):
                sections['Security and Credentials'].append(line)
            elif any(x in path_lower for x in ['package', 'node', 'composer', 'vendor', 'npm']):
                sections['Web and Framework Files'].append(line)
            elif any(x in path_lower for x in ['sql', 'backup', 'dump', 'db']):
                sections['Database and Backups'].append(line)
            elif any(x in path_lower for x in ['actuator', 'debug', 'profiler', 'api-docs', 'swagger']):
                sections['System and Configuration'].append(line)
            else:
                sections['Other'].append(line)

        # Write sections
        for section_name, patterns in sections.items():
            if patterns:
                f.write(f"# {section_name}\n")
                for pattern in sorted(patterns):
                    f.write(f"{pattern}\n")
                f.write("\n")

    print(f"Converted {input_file} to .gitignore format")
    print(f"Total patterns: {len(unique_lines)}")
    print(f"Output saved to: {output_file}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python convert_to_gitignore.py <input_file> [output_file]")
        print("Example: python convert_to_gitignore.py dlake/ss/log/ss-log-2601.log.txt")
        print("         python convert_to_gitignore.py dlake/ss/log/ss-log-2601.log.txt .gitignore")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    convert_to_gitignore(input_file, output_file)
