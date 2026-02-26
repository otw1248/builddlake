#!/usr/bin/env python3
"""
Created by AI Assistant
Date: 2026-02-26
Sort carPrefix.json by prefix and group same cities together
"""

import json
import re
from collections import defaultdict


def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data, filepath):
    """Save JSON file with proper formatting"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')  # Add trailing newline


def get_city_key(city):
    """Extract city name for grouping, remove parentheses content for sorting"""
    # Remove content in parentheses for grouping
    city_clean = re.sub(r'（[^）]*）', '', city)
    city_clean = re.sub(r'\([^)]*\)', '', city_clean)
    # Also remove "已取消", "增补", etc. for grouping
    city_clean = city_clean.replace('已取消', '').replace('增补', '').strip()
    return city_clean


def sort_data(data):
    """Sort the data by province/prefix and group same cities"""
    sorted_data = {}

    # Sort provinces by prefix (which is Chinese character or letter)
    # First group: Municipalities (京, 津, 沪, 渝)
    # Second: Provinces in alphabetical order of prefix
    # Third: Autonomous regions

    def get_province_sort_key(province_name, province_data):
        prefix = province_data.get('prefix', '')
        # Municipalities first
        if prefix in ['京', '津', '沪', '渝']:
            return (0, prefix, province_name)
        # Autonomous regions
        if '自治区' in province_name or '壮族' in province_name or '回族' in province_name or '维吾尔' in province_name:
            return (2, prefix, province_name)
        # Regular provinces
        return (1, prefix, province_name)

    # Sort provinces
    sorted_provinces = sorted(data.items(), key=lambda x: get_province_sort_key(x[0], x[1]))

    for province_name, province_data in sorted_provinces:
        codes = province_data['codes']

        # Group codes by city
        city_groups = defaultdict(list)
        for code, city in codes.items():
            city_key = get_city_key(city)
            city_groups[city_key].append((code, city))

        # Sort cities by name
        sorted_cities = {}
        for city_key in sorted(city_groups.keys()):
            # Sort codes alphabetically
            code_list = sorted(city_groups[city_key], key=lambda x: x[0])
            for code, city in code_list:
                sorted_cities[code] = city

        sorted_data[province_name] = {
            'prefix': province_data['prefix'],
            'codes': sorted_cities
        }

    return sorted_data


def main():
    input_file = '/workspace/dlake/life/car/carPrefix.json'
    output_file = '/workspace/dlake/life/car/carPrefix.json'

    # Load data
    print(f"Loading {input_file}...")
    data = load_json(input_file)

    # Sort data
    print("Sorting data...")
    sorted_data = sort_data(data)

    # Save data
    print(f"Saving to {output_file}...")
    save_json(sorted_data, output_file)

    print("Done!")


if __name__ == '__main__':
    main()
