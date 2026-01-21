#!/usr/bin/env python3
"""
Created by AI Assistant on 2026-01-21
"""

import json
import re
from pathlib import Path

def add_en_fields():
    # Read JSON file
    json_file = Path("/workspace/dlake/life/commu/life-communication.json")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Add enName and enDescription to each service
    for service in data['services']:
        name = service['name']
        description = service['description']
        
        # Generate English name and description
        en_info = generate_english_info(name, description)
        if en_info['enName']:
            service['enName'] = en_info['enName']
        if en_info['enDescription']:
            service['enDescription'] = en_info['enDescription']
    
    # Write back to JSON file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Added enName and enDescription to {len(data['services'])} services")

def generate_english_info(name, description):
    """Generate English name and description based on Chinese name"""
    # Map common service names to English
    mapping = {
        "12345市民服务热线": {"enName": "12345 Government Service Hotline", "enDescription": "National Unified Government Service Hotline"},
        "个人所得税": {"enName": "Personal Income Tax", "enDescription": "State Taxation Administration Personal Income Tax Service"},
        "国家医保中心": {"enName": "National Medical Insurance Center", "enDescription": "National Healthcare Security Administration Hotline"},
        "交管12123": {"enName": "Traffic Management 12123", "enDescription": "National Traffic Safety Integrated Service Management Platform"},
        "国家网络身份认证": {"enName": "National Network ID", "enDescription": "National Internet + Trusted Identity Authentication Platform"},
        "消费者权益保护": {"enName": "Consumer Rights Protection", "enDescription": "National Market Supervision Complaint and Report Hotline"},
        "卫健委": {"enName": "National Health Commission", "enDescription": "National Health Commission Service Hotline"},
        "人力资源和社会保障": {"enName": "HR and Social Security", "enDescription": "National Human Resources and Social Security Service Hotline"},
        "国家税务局": {"enName": "State Taxation Administration", "enDescription": "State Taxation Administration Service Hotline"},
        "国家气象局": {"enName": "CMA", "enDescription": "China Meteorological Administration Service Hotline"},
        "国家药监局": {"enName": "NMPA", "enDescription": "National Medical Products Administration Service Hotline"},
        "全国网络举报": {"enName": "Internet Report Center", "enDescription": "China Internet Illegal and Bad Information Reporting Center"},
        "国家邮政局": {"enName": "State Post Bureau", "enDescription": "State Post Bureau Service Hotline"},
        "国家自然资源和规划": {"enName": "Ministry of Natural Resources", "enDescription": "Ministry of Natural Resources Service Hotline"},
        "国家发改委": {"enName": "NDRC", "enDescription": "National Development and Reform Commission Service Hotline"},
        "中国疾控中心": {"enName": "China CDC", "enDescription": "Chinese Center for Disease Control and Prevention"},
        "全国一体化政务服务中心": {"enName": "National Government Service", "enDescription": "National Integrated Online Government Service Platform"},
        "中国标准信息服务": {"enName": "China Standard Info", "enDescription": "China Standard Information Service Network"},
        "国家图书馆": {"enName": "National Library", "enDescription": "National Library of China Service"},
        "领事直通车": {"enName": "Consular Services", "enDescription": "MFA Global Consular Protection and Service Hotline"},
        "交警": {"enName": "Traffic Police", "enDescription": "National Road Traffic Management Alarm Phone"},
        "公安部交通管理局": {"enName": "Traffic Management Bureau", "enDescription": "Traffic Management Bureau of MPS"},
        "中国质检": {"enName": "China Quality Inspection", "enDescription": "State Quality Supervision Inspection and Quarantine Service Hotline"},
        "中国企业信用信息": {"enName": "Enterprise Credit Info", "enDescription": "National Enterprise Credit Information Publicity System"},
        "人民法院": {"enName": "People's Court", "enDescription": "National Court Litigation Service Hotline"},
        "人民检察院": {"enName": "People's Procuratorate", "enDescription": "National Procuratorial Organs Unified Service Hotline"},
        "移民局": {"enName": "NIA", "enDescription": "National Immigration Administration Service Hotline"},
        "中国海关": {"enName": "China Customs", "enDescription": "China Customs Service Hotline"},
        "中国民航": {"enName": "CAAC", "enDescription": "Civil Aviation Administration of China Service Hotline"},
        "航旅纵横": {"enName": "UMETrip", "enDescription": "UMETrip Customer Service"},
        "国家电网": {"enName": "State Grid", "enDescription": "State Grid Corporation of China Service Hotline"},
        "中国铁路": {"enName": "China Railway", "enDescription": "China Railway Customer Service Center"},
        "中国工商银行(工行)": {"enName": "ICBC", "enDescription": "ICBC Customer Service and Credit Card Center"},
        "中国农业银行(农行)": {"enName": "ABC", "enDescription": "Agricultural Bank of China Customer Service and Credit Card Center"},
        "中国建设银行(建行)": {"enName": "CCB", "enDescription": "China Construction Bank Customer Service and Credit Card Center"},
        "中国银行(中行)": {"enName": "BOC", "enDescription": "Bank of China Customer Service and Credit Card Center"},
        "交通银行(交行)": {"enName": "BoCom", "enDescription": "Bank of Communications Customer Service and Credit Card Center"},
        "中国邮政储蓄银行(邮储)": {"enName": "PSBC", "enDescription": "Postal Savings Bank of China Customer Service and Credit Card Center"},
        "招商银行": {"enName": "CMB", "enDescription": "China Merchants Bank Customer Service and Credit Card Center"},
        "中信银行": {"enName": "CITIC Bank", "enDescription": "CITIC Bank Customer Service and Credit Card Center"},
        "浦发银行": {"enName": "SPDB", "enDescription": "SPDB Customer Service and Credit Card Center"},
        "兴业银行": {"enName": "CIB", "enDescription": "Industrial Bank Customer Service and Credit Card Center"},
        "平安银行": {"enName": "Ping An Bank", "enDescription": "Ping An Bank Customer Service and Credit Card Center"},
        "中国民生银行": {"enName": "CMBC", "enDescription": "China Minsheng Bank Customer Service and Credit Card Center"},
        "中国银联": {"enName": "UnionPay", "enDescription": "China UnionPay Customer Service Hotline"},
        "中国移动": {"enName": "China Mobile", "enDescription": "China Mobile Communication Service Hotline"},
        "中国联通": {"enName": "China Unicom", "enDescription": "China Unicom Communication Service Hotline"},
        "中国电信": {"enName": "China Telecom", "enDescription": "China Telecom Communication Service Hotline"},
        "中国广电": {"enName": "China Broadnet", "enDescription": "China Broadcasting Network Communication Service Hotline"},
        "微信": {"enName": "WeChat", "enDescription": "Tencent WeChat Customer Service"},
        "支付宝": {"enName": "Alipay", "enDescription": "Alipay Customer Service Hotline"},
        "抖音": {"enName": "Douyin", "enDescription": "ByteDance Douyin Customer Service"},
        "微博": {"enName": "Weibo", "enDescription": "Sina Weibo Customer Service"},
        "京东": {"enName": "JD", "enDescription": "JD.com Mall Customer Service"},
        "淘宝": {"enName": "Taobao", "enDescription": "Taobao Customer Service Hotline"},
        "拼多多": {"enName": "Pinduoduo", "enDescription": "Pinduoduo Customer Service"},
        "美团": {"enName": "Meituan", "enDescription": "Meituan Customer Service Hotline"},
        "滴滴": {"enName": "DiDi", "enDescription": "Didi Customer Service"},
        "高德地图": {"enName": "Amap", "enDescription": "Alibaba Amap"},
        "腾讯地图": {"enName": "Tencent Maps", "enDescription": "Tencent Maps Customer Service"},
        "百度地图": {"enName": "Baidu Maps", "enDescription": "Baidu Maps Customer Service"},
        "中信证券": {"enName": "CITIC Securities", "enDescription": "CITIC Securities Customer Service"},
        "国泰君安证券": {"enName": "GTJA", "enDescription": "Guotai Junan Securities Customer Service"},
        "华泰证券": {"enName": "Huatai Securities", "enDescription": "Huatai Securities Customer Service"},
        "广发证券": {"enName": "GF Securities", "enDescription": "GF Securities Customer Service"},
        "中国银河证券": {"enName": "China Galaxy", "enDescription": "China Galaxy Securities Customer Service"},
        "招商证券": {"enName": "CMS", "enDescription": "China Merchants Securities Customer Service"},
        "海通证券": {"enName": "Haitong Securities", "enDescription": "Haitong Securities Customer Service"},
        "申万宏源证券": {"enName": "Shenwan Hongyuan", "enDescription": "Shenwan Hongyuan Securities Customer Service"},
        "中金公司": {"enName": "CICC", "enDescription": "CICC Customer Service"},
        "中信期货": {"enName": "CITIC Futures", "enDescription": "CITIC Futures Customer Service"},
        "国泰君安期货": {"enName": "GTJA Futures", "enDescription": "Guotai Junan Futures Customer Service"},
        "永安期货": {"enName": "Yongan Futures", "enDescription": "Yongan Futures Customer Service"},
        "银河期货": {"enName": "Galaxy Futures", "enDescription": "Galaxy Futures Customer Service"},
        "海通期货": {"enName": "Haitong Futures", "enDescription": "Haitong Futures Customer Service"},
        "广发期货": {"enName": "GF Futures", "enDescription": "GF Futures Customer Service"},
        "南华期货": {"enName": "Nanhua Futures", "enDescription": "Nanhua Futures Customer Service"},
        "方正中期期货": {"enName": "Founder Mid-term", "enDescription": "Founder Mid-term Futures Customer Service"},
        "光大期货": {"enName": "Everbright Futures", "enDescription": "Everbright Futures Customer Service"},
        "上交所": {"enName": "SSE", "enDescription": "Shanghai Stock Exchange"},
        "深交所": {"enName": "SZSE", "enDescription": "Shenzhen Stock Exchange"},
        "京交所": {"enName": "BSE", "enDescription": "Beijing Stock Exchange"},
        "中国证券登记结算有限公司": {"enName": "CSDCC", "enDescription": "China Securities Depository and Clearing Corporation"},
        "医院": {"enName": "Hospital", "enDescription": "National Public Health Public Welfare Hotline"},
        "图书馆": {"enName": "Library", "enDescription": "Public Library Service"},
        "自来水": {"enName": "Water Supply", "enDescription": "Water Supply Service Hotline"},
        "天然气": {"enName": "Natural Gas", "enDescription": "Natural Gas Supply Service Hotline"},
        "中国石化": {"enName": "Sinopec", "enDescription": "Sinopec Customer Service Hotline"},
        "中国石油": {"enName": "PetroChina", "enDescription": "PetroChina Customer Service Hotline"},
        "暖气": {"enName": "Heating", "enDescription": "Heating Service Hotline"},
        "物业公司": {"enName": "Property Management", "enDescription": "Property Management Service Hotline"},
        "顺丰速运": {"enName": "SF Express", "enDescription": "SF Express Customer Service"},
        "京东物流": {"enName": "JD Logistics", "enDescription": "JD Express Customer Service"},
        "中通快递": {"enName": "ZTO Express", "enDescription": "ZTO Express Customer Service"},
        "圆通速递(YTO)": {"enName": "YTO Express", "enDescription": "YTO Express Customer Service"},
        "申通快递(STO)": {"enName": "STO Express", "enDescription": "STO Express Customer Service"},
        "韵达速递(Yunda)": {"enName": "Yunda Express", "enDescription": "Yunda Express Customer Service"},
        "邮政EMS": {"enName": "China Post EMS", "enDescription": "China Post EMS Customer Service"},
        "德邦快递": {"enName": "Deppon Express", "enDescription": "Deppon Express Customer Service"},
        "极兔速递": {"enName": "J&T Express", "enDescription": "J&T Express Customer Service"},
        "百世快递(BEST)": {"enName": "BEST Express", "enDescription": "BEST Express Customer Service"},
        "山姆会员店(Sam's Club)": {"enName": "Sam's Club", "enDescription": "Sam's Club Customer Service"},
        "开市客": {"enName": "Costco", "enDescription": "Costco Customer Service"},
        "百联集团": {"enName": "Bailian Group", "enDescription": "Bailian Group Customer Service"},
        "永旺(Aeon)": {"enName": "Aeon", "enDescription": "Aeon Supermarket Customer Service"},
        "奥乐齐": {"enName": "ALDI", "enDescription": "ALDI Customer Service"},
        "盒马": {"enName": "Hema", "enDescription": "Freshippo Hema Customer Service"},
        "必胜客": {"enName": "Pizza Hut", "enDescription": "Pizza Hut Customer Service Hotline"},
        "叮咚买菜": {"enName": "Dingdong", "enDescription": "Dingdong Maicai Customer Service"},
        "瑞幸咖啡": {"enName": "Luckin Coffee", "enDescription": "Luckin Coffee Customer Service"},
        "库迪咖啡": {"enName": "Cotti Coffee", "enDescription": "Cotti Coffee Customer Service"},
        "可口可乐(Coca-Cola)": {"enName": "Coca-Cola", "enDescription": "Coca-Cola Customer Service"},
        "百事可乐(Pepsi)": {"enName": "Pepsi", "enDescription": "Pepsi Customer Service"},
        "麦当劳(McDonald's)": {"enName": "McDonald's", "enDescription": "McDonald's Customer Service Hotline"},
        "肯德基": {"enName": "KFC", "enDescription": "KFC Customer Service Hotline"},
        "星巴克": {"enName": "Starbucks", "enDescription": "Starbucks Customer Service Hotline"},
        "汉堡王": {"enName": "Burger King", "enDescription": "Burger King Customer Service Hotline"},
        "途虎养车": {"enName": "Tuhu", "enDescription": "Tuhu Customer Service"},
        "宜家(IKEA)": {"enName": "IKEA", "enDescription": "IKEA Customer Service Hotline"},
        "人民银行": {"enName": "PBOC", "enDescription": "People's Bank of China Financial Consumer Protection Hotline"},
        "证监会": {"enName": "CSRC", "enDescription": "China Securities Regulatory Commission Service Hotline"},
        "银监会": {"enName": "CBIRC", "enDescription": "China Banking and Insurance Regulatory Commission Service Hotline"},
        "国家外汇管理局": {"enName": "SAFE", "enDescription": "State Administration of Foreign Exchange"},
        "中国保险行业协会": {"enName": "IAC", "enDescription": "Insurance Association of China"},
        "中国人寿": {"enName": "China Life", "enDescription": "China Life Insurance Customer Service"},
        "中国平安保险": {"enName": "Ping An Insurance", "enDescription": "Ping An Insurance Customer Service"},
        "中国太平洋保险": {"enName": "CPIC", "enDescription": "Pacific Insurance Customer Service"},
        "中国人民保险": {"enName": "PICC", "enDescription": "People's Insurance Customer Service"},
        "中国太平保险": {"enName": "China Taiping", "enDescription": "China Taiping Insurance Customer Service"},
        "泰康人寿": {"enName": "Taikang Life", "enDescription": "Taikang Life Insurance Customer Service"},
        "新华人寿": {"enName": "New China Life", "enDescription": "New China Life Insurance Customer Service"},
        "世界卫生组织": {"enName": "WHO", "enDescription": "World Health Organization China Representative Office"},
    }
    
    return mapping.get(name, {"enName": "", "enDescription": ""})

if __name__ == "__main__":
    add_en_fields()
