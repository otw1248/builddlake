#!/usr/bin/env python3
"""
Created by AI Assistant on 2026-01-21
"""

import json
from pathlib import Path

def sort_services_by_category():
    # Read the JSON file
    json_file = Path("/workspace/dlake/life/commu/life-communication.json")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Get category order
    category_order = {cat: i for i, cat in enumerate(data['categoryList'])}
    
    # Sort services based on category order
    data['services'].sort(key=lambda x: category_order.get(x['category'], float('inf')))
    
    # Write back to JSON file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Services sorted successfully. Total services: {len(data['services'])}")

if __name__ == "__main__":
    sort_services_by_category()
