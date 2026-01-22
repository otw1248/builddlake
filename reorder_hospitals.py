#!/usr/bin/env python3
# Created by AI Assistant on 2026-01-22

import json

# Read the file
with open('/workspace/dlake/life/commu/life-communication.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Get all hospitals
hospitals = [s for s in data['services'] if s.get('category') == '医院']

print(f'Total hospitals: {len(hospitals)}')

# Define group order
def get_group_order(name):
    # Beijing (Group 1)
    if '北京协和医院' in name or '中国人民解放军总医院' in name or '北京大学' in name or '中日友好医院' in name or name == '北京医院':
        return 1
    # Shanghai (Group 2)
    elif '上海' in name or ('复旦' in name and '上海' not in name) or '瑞金' in name or '仁济' in name or '新华' in name or '长海' in name or '长征' in name or ('同济大学附属' in name and '西安' not in name):
        return 2
    # Jinan/Shandong (Group 3)
    elif '济南' in name or '齐鲁' in name or ('山东' in name and '江苏' not in name):
        return 3
    # Guangdong (Group 4)
    elif '广州' in name or '深圳' in name or '香港大学深圳' in name or ('广东省人民医院' in name):
        return 4
    # Sichuan/Chengdu (Group 5)
    elif '四川' in name:
        return 5
    # Hubei/Wuhan (Group 6)
    elif '湖北' in name or '华中科技' in name:
        return 6
    # Zhejiang/Hangzhou (Group 7)
    elif '浙江' in name:
        return 7
    # Jiangsu/Nanjing (Group 8)
    elif '南京' in name or '鼓楼' in name or ('江苏省人民医院' in name) or '东南大学附属' in name:
        return 8
    # Suzhou (Group 9)
    elif '苏州' in name or '常熟' in name or '昆山' in name:
        return 9
    # Shaanxi/Xi'an (Group 10)
    elif '西安' in name or '西京' in name:
        return 10
    # Tianjin (Group 11)
    elif '天津' in name:
        return 11
    # Chongqing (Group 12)
    elif '重庆' in name:
        return 12
    # Hunan/Changsha (Group 13)
    elif '湖南' in name or '湘雅' in name:
        return 13
    # Henan/Zhengzhou (Group 14)
    elif '河南' in name or '郑州' in name:
        return 14
    # Liaoning/Shenyang (Group 15)
    elif '辽宁' in name or '盛京' in name or ('中国医科大学' in name and '上海' not in name):
        return 15
    # Hebei (Group 16)
    elif '河北' in name:
        return 16
    # Fujian (Group 17)
    elif '福建' in name:
        return 17
    # Anhui (Group 18)
    elif '安徽' in name:
        return 18
    # Jiangxi (Group 19)
    elif '江西' in name or '南昌' in name:
        return 19
    # Yunnan (Group 20)
    elif '云南' in name or '昆明' in name:
        return 20
    # Guizhou (Group 21)
    elif '贵州' in name:
        return 21
    # Guangxi (Group 22)
    elif '广西' in name:
        return 22
    # Xinjiang (Group 23)
    elif '新疆' in name:
        return 23
    # Inner Mongolia (Group 24)
    elif '内蒙古' in name:
        return 24
    # Ningxia (Group 25)
    elif '宁夏' in name:
        return 25
    # Qinghai (Group 26)
    elif '青海' in name:
        return 26
    # Gansu (Group 27)
    elif '甘肃' in name:
        return 27
    # Jilin (Group 28)
    elif '吉林' in name:
        return 28
    # Heilongjiang (Group 29)
    elif '黑龙江' in name or '哈尔滨' in name:
        return 29
    # Hainan (Group 30)
    elif '海南' in name:
        return 30
    # Tibet (Group 31)
    elif '西藏' in name:
        return 31
    # Guangdong catch remaining
    elif '中山大学附属第一医院' in name or '南方医科大学南方医院' in name:
        return 4
    else:
        return 99

# Sort hospitals
sorted_hospitals = sorted(hospitals, key=lambda x: (get_group_order(x['name']), x['name']))

# Print groups
current_group = None
for h in sorted_hospitals:
    group = get_group_order(h['name'])
    if group != current_group:
        current_group = group
        print(f'\n--- Group {current_group} ---')
    print(f'  {h["name"]}')

# Rebuild services array
non_hospitals = [s for s in data['services'] if s.get('category') != '医院']
data['services'] = non_hospitals + sorted_hospitals

# Write back
with open('/workspace/dlake/life/commu/life-communication.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('\nHospital reordering complete!')
