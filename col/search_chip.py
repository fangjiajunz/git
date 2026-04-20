import os
import json

def search_chip_company(search_name, root_dir='.'):
    """
    搜索芯片名称并返回对应的公司
    """
    search_name = search_name.strip().lower()
    results = []

    # 遍历当前目录下的所有子文件夹
    for folder_name in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder_name)
        
        # 确保是文件夹且内部存在 tag.json
        if os.path.isdir(folder_path):
            json_path = os.path.join(folder_path, 'tag.json')
            
            if os.path.exists(json_path):
                try:
                    with open(json_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    chip_name = data.get('chipName', '').strip().lower()
                    company = data.get('company', '未知公司')

                    # 检查是否匹配（包含或完全匹配）
                    if search_name in chip_name or search_name in folder_name.lower():
                        results.append({
                            'folder': folder_name,
                            'chipName': data.get('chipName', '未知'),
                            'company': company
                        })
                
                except Exception as e:
                    print(f"读取 {folder_name}/tag.json 出错: {e}")

    return results

if __name__ == "__main__":
    import sys
    
    # 如果通过命令行参数传入了芯片名
    if len(sys.argv) > 1:
        search_term = " ".join(sys.argv[1:])
    else:
        # 否则交互式输入
        search_term = input("请输入要搜索的芯片名称: ")
    
    if search_term:
        print(f"\n正在搜索 '{search_term}'...\n")
        matches = search_chip_company(search_term)
        
        if matches:
            print(f"找到 {len(matches)} 个匹配项:")
            print("-" * 40)
            for m in matches:
                print(f"文件夹: {m['folder']}")
                print(f"芯片名: {m['chipName']}")
                print(f"公司  : {m['company']}")
                print("-" * 40)
        else:
            print("未找到匹配的芯片。")
    else:
        print("请输入有效的芯片名称。")
