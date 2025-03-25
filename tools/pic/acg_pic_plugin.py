import requests
import os
import random
import string
from PIL import Image
from io import BytesIO

def get_acg_image(save_path=None, filename=None):
    """
    获取随机ACG图片
    :param save_path: 保存路径，默认为当前目录
    :param filename: 保存的文件名，默认为随机生成
    :return: 保存结果信息
    """
    api_url = "https://api.yujn.cn/api/gzl_ACG.php"
    
    try:
        # 发送请求获取图片
        response = requests.get(api_url, stream=True)
        
        if response.status_code != 200:
            return f"错误: API请求失败，状态码: {response.status_code}"
        
        # 设置默认保存路径和文件名
        if not save_path:
            save_path = os.getcwd()
        
        if not filename:
            # 生成随机文件名
            random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            filename = f"acg_image_{random_str}.jpg"
        
        # 确保目录存在
        if not os.path.exists(save_path):
            os.makedirs(save_path, exist_ok=True)
        
        # 完整的文件保存路径
        full_path = os.path.join(save_path, filename)
        
        # 保存图片
        with open(full_path, 'wb') as f:
            f.write(response.content)
        
        return f"成功获取ACG图片并保存至: {full_path}"
    
    except Exception as e:
        return f"获取图片时出错: {str(e)}"
