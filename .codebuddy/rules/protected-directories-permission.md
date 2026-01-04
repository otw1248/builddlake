# Protected Directories Permission Rule

## Rule Purpose
This rule protects specific directories from any write operations.

## Protected Directories
- `/workspace/zexamples`
- `/workspace/zarchive`

## Restrictions
- **DO NOT** create, modify, or delete any files in the protected directories
- **DO NOT** write to any files within these directories
- These directories should remain read-only at all times

## Action Required
If a task requires writing to any protected directory:
1. Inform the user that the directory is protected and cannot be modified
2. Ask the user for an alternative location or approach
3. Do not proceed with any write operations until explicitly confirmed by the user

## Enforcement
All write operations (create, modify, delete) targeting `/workspace/zexamples` or `/workspace/zarchive` are strictly prohibited and must be blocked.
