"""
Created by AI Assistant
Date: 2026-01-21

Restore original verifiedFlag values - only keep originally verified services
"""

import json

# Read the current file
with open('/workspace/dlake/life/commu/life-communication.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# List of services that were originally verified (from the file)
originally_verified = [
    "12345市民服务热线",
    "个人所得税",
    "消费者权益保护",
    "国家气象局",
    "中国工商银行(工行)",
    "中国农业银行(农行)",
    "中国建设银行(建行)",
    "中国银行(中行)",
    "交通银行(交行)",
    "中国邮政储蓄银行(邮储)",
    "招商银行",
    "中国移动",
    "中国联通",
    "中国电信",
    "中国广电",
    "支付宝",
    "腾讯财付通",
    "中国银联",
    "中国国际航空",
    "东方航空",
    "南方航空",
    "领事直通车"
]

# Reset all verifiedFlag to original state
for service in data['services']:
    if service['name'] in originally_verified:
        service['verifiedFlag'] = True
    else:
        # Remove verifiedFlag if it was added
        if 'verifiedFlag' in service:
            del service['verifiedFlag']

# Save the restored file
with open('/workspace/dlake/life/commu/life-communication.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Count statistics
with_verified = sum(1 for s in data['services'] if s.get('verifiedFlag') == True)
without_verified = sum(1 for s in data['services'] if 'verifiedFlag' not in s)

print(f"Restored original state!")
print(f"Services with verifiedFlag (true): {with_verified}")
print(f"Services without verifiedFlag: {without_verified}")
print(f"Total: {len(data['services'])}")
