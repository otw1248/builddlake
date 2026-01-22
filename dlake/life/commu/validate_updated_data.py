#!/usr/bin/env python3
"""
Created by AI Assistant on 2026-01-22
验证生活服务数据的更新
"""

import json

# 读取更新后的文件
with open('/workspace/dlake/life/commu/life-communication.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 验证的关键条目
expected_updates = {
    "全国公共卫生热线": {
        "category": "公共服务",
        "phone": "12320",
        "verifiedFlag": True
    },
    "公共图书馆": {
        "category": "公共文化服务",
        "phone": "12345",
        "verifiedFlag": False
    },
    "自来水服务": {
        "category": "公用事业",
        "phone": "12319",
        "verifiedFlag": False
    },
    "天然气服务": {
        "category": "公用事业",
        "phone": "95158",
        "verifiedFlag": False
    },
    "中国石化": {
        "category": "能源零售",
        "phone": "95105888",
        "verifiedFlag": True
    },
    "中国石油": {
        "category": "能源零售",
        "phone": "95504",
        "verifiedFlag": True
    },
    "供暖服务": {
        "category": "公用事业",
        "phone": "12319",
        "verifiedFlag": False
    },
    "物业服务": {
        "category": "社区服务",
        "phone": "12345",
        "verifiedFlag": False
    },
    "携程旅行": {
        "category": "在线旅游",
        "phone": "400-820-6666",
        "verifiedFlag": True
    },
    "同程旅行": {
        "category": "在线旅游",
        "phone": "400-777-7777",
        "verifiedFlag": True
    }
}

# 验证类别列表
print("=== 类别列表验证 ===")
expected_new_categories = ["公共服务", "公共文化服务", "公用事业", "能源零售", "社区服务", "在线旅游"]
for cat in expected_new_categories:
    if cat in data['categoryList']:
        print(f"✓ 类别 '{cat}' 已添加")
    else:
        print(f"✗ 类别 '{cat}' 缺失")

# 验证具体条目
print("\n=== 条目更新验证 ===")
services_by_name = {s['name']: s for s in data['services']}

for name, expected in expected_updates.items():
    if name not in services_by_name:
        print(f"✗ 条目 '{name}' 不存在")
        continue

    service = services_by_name[name]
    all_match = True

    for key, expected_value in expected.items():
        actual_value = service.get(key)
        if actual_value != expected_value:
            print(f"✗ '{name}' 的 {key} 不匹配: 期望 {expected_value}, 实际 {actual_value}")
            all_match = False

    if all_match:
        print(f"✓ '{name}' 所有字段验证通过")

# 验证旧条目已被移除
removed_items = ["医院", "图书馆", "自来水", "天然气", "暖气", "物业公司", "携程", "同程"]
print("\n=== 旧条目移除验证 ===")
for name in removed_items:
    if name not in services_by_name:
        print(f"✓ 旧条目 '{name}' 已移除")
    else:
        print(f"⚠  旧条目 '{name}' 仍然存在（可能是不同条目）")

# 统计信息
print("\n=== 数据统计 ===")
print(f"总条目数: {len(data['services'])}")
print(f"类别数: {len(data['categoryList'])}")
print(f"最后验证日期: {data.get('lastVerified', 'N/A')}")

print("\n✅ 验证完成")
