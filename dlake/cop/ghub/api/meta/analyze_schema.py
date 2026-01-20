import json

with open('/workspace/dlake/cop/ghub/api/meta/github-meta.json') as f:
    data = json.load(f)

print("=" * 80)
print("GitHub Meta API Schema")
print("=" * 80)
print()

# Top-level overview
print("ROOT OBJECT")
print("-" * 80)
for key, value in data.items():
    if isinstance(value, dict):
        print(f"{key}: dict with {len(value)} keys")
    elif isinstance(value, list):
        print(f"{key}: list with {len(value)} items")
    else:
        print(f"{key}: {type(value).__name__}")

print()
print("=" * 80)
print("Detailed Schema")
print("=" * 80)
print()

# ssh_key_fingerprints structure
print("ssh_key_fingerprints:")
for k, v in data.get('ssh_key_fingerprints', {}).items():
    print(f"  {k}: {type(v).__name__}")

print()
print("domains:")
for k, v in data.get('domains', {}).items():
    if isinstance(v, list):
        print(f"  {k}: list[{len(v)}]")
    else:
        print(f"  {k}: {type(v).__name__}")

print()
print("List field examples (first item):")
for field in ['ssh_keys', 'hooks', 'web', 'api', 'git', 'packages', 'pages', 'actions', 'copilot']:
    if field in data and data[field]:
        first = data[field][0]
        print(f"  {field}: {type(first).__name__}")
