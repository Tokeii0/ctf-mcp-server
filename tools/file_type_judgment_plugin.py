import os
from magika import Magika

def identify_file_type(file_path):
    """
    使用Magika判断文件类型
    :param file_path: 文件路径
    :return: 文件类型信息
    """
    if not os.path.exists(file_path):
        return f"错误: 文件不存在: {file_path}"
    
    try:
        m = Magika()
        res = m.identify_path(file_path)
        return f"文件类型: {res.output.label}"
    except Exception as e:
        return f"判断文件类型时出错: {str(e)}"
