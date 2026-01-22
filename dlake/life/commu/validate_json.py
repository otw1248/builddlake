# Created by AI Assistant on 2026-01-22

import json
from pathlib import Path


def validate_json_file(file_path, output_json=False):
    """Validate JSON file and extract categoryList"""
    try:
        # Read and parse JSON file
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print("✓ JSON file is valid\n")
        print("=" * 60)
        
        # Get categoryList
        category_list = data.get('categoryList', [])
        print(f"\nCategory List ({len(category_list)} categories):")
        print("-" * 60)
        for i, category in enumerate(category_list, 1):
            print(f"{i:2d}. {category}")
        
        # Get services grouped by category
        services = data.get('services', [])
        
        print("\n" + "=" * 60)
        print("Services by Category:")
        print("=" * 60 + "\n")
        
        for category in category_list:
            category_services = [s for s in services if s.get('category') == category]
            print(f"\n【{category}】({len(category_services)} services)")
            print("-" * 60)
            
            for service in category_services:
                name = service.get('name', 'N/A')
                phone = service.get('phone', '')
                verified = '✓' if service.get('verifiedFlag') else '✗'
                
                # Format phone number display
                phone_display = f"Tel: {phone}" if phone else ""
                
                # Format weibo/douyin/wechat info
                platforms = []
                if service.get('wechat'):
                    platforms.append(f"微信:{service['wechat']}")
                if service.get('douyin'):
                    platforms.append(f"抖音:{service['douyin']}")
                if service.get('weibo'):
                    platforms.append(f"微博:{service['weibo']}")
                
                platform_info = f" | {', '.join(platforms)}" if platforms else ""
                
                print(f"  [{verified}] {name}")
                if phone_display or platform_info:
                    print(f"        {phone_display}{platform_info}")
        
        # Summary statistics
        print("\n" + "=" * 60)
        print("Summary Statistics:")
        print("=" * 60)
        print(f"Total Categories: {len(category_list)}")
        print(f"Total Services: {len(services)}")
        verified_count = sum(1 for s in services if s.get('verifiedFlag'))
        print(f"Verified Services: {verified_count}/{len(services)}")
        print(f"Last Verified: {data.get('lastVerified', 'N/A')}")
        
        # Output JSON if requested
        if output_json:
            output_data = {
                "categoryList": category_list,
                "servicesByCategory": {}
            }
            for category in category_list:
                category_services = [s for s in services if s.get('category') == category]
                output_data["servicesByCategory"][category] = category_services
            
            output_file = Path(__file__).parent / 'life-communication-validated.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, ensure_ascii=False, indent=2)
            print(f"\n✓ Validated JSON saved to: {output_file}")
        
        return data
        
    except json.JSONDecodeError as e:
        print(f"✗ JSON parsing error: {e}")
        return None
    except FileNotFoundError:
        print(f"✗ File not found: {file_path}")
        return None
    except Exception as e:
        print(f"✗ Error: {e}")
        return None


if __name__ == '__main__':
    # Validate the life-communication.json file
    json_file = Path(__file__).parent / 'life-communication.json'
    validate_json_file(json_file, output_json=True)
