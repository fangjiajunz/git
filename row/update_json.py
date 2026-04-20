import os
import json

def update_chip_names():
    # 获取当前脚本所在目录
    root_dir = os.getcwd()
    
    # 遍历当前目录下的所有子项
    for folder_name in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder_name)
        
        # 确保是文件夹且内部存在 tag.json
        if os.path.isdir(folder_path):
            json_path = os.path.join(folder_path, 'tag.json')
            
            if os.path.exists(json_path):
                try:
                    # 1. 读取 JSON 内容
                    with open(json_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # 2. 修改 chipName 为当前文件夹名
                    data['chipName'] = folder_name
                    
                    # 3. 写回文件
                    with open(json_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                    
                    print(f"成功更新: {folder_name}/tag.json")
                
                except Exception as e:
                    print(f"错误 - 无法处理 {folder_name}: {e}")

if __name__ == "__main__":
    update_chip_names()