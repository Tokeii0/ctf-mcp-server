import zipfile
import os

def extract_zip(zip_path, extract_to=None):
    """
    解压缩ZIP文件
    :param zip_path: ZIP文件路径
    :param extract_to: 解压目标路径，默认为ZIP文件所在目录
    :return: 解压结果信息
    """
    if not os.path.exists(zip_path):
        return f"错误: ZIP文件不存在: {zip_path}"
    
    if not extract_to:
        # 默认解压到ZIP文件所在目录
        extract_to = os.path.dirname(zip_path)
    
    # 确保目标目录存在
    if not os.path.exists(extract_to):
        os.makedirs(extract_to, exist_ok=True)
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        return f"成功解压到: {extract_to}"
    except zipfile.BadZipFile:
        return "错误: 无效的ZIP文件"
    except Exception as e:
        return f"解压过程中出错: {str(e)}"

def zip_file(file_path: str, zip_path: str):
    '''
    压缩文件
    :param file_path: 要压缩的文件路径
    :param zip_path: 压缩后的ZIP文件路径
    :return: 压缩结果信息
    '''
    if not os.path.exists(file_path):
        return f"错误: 文件不存在: {file_path}"
    
    try:
        with zipfile.ZipFile(zip_path, 'w') as zip_ref:
            zip_ref.write(file_path, arcname=os.path.basename(file_path))
        return f"成功压缩到: {zip_path}"
    except Exception as e:
        return f"压缩过程中出错: {str(e)}"