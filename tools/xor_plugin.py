import os

def xor_string(text, key):
    """
    对字符串进行XOR操作
    :param text: 要进行XOR操作的字符串
    :param key: XOR密钥
    :return: XOR操作后的结果
    """
    if isinstance(text, str):
        text = text.encode('utf-8')
    if isinstance(key, str):
        key = key.encode('utf-8')
    
    result = bytearray()
    for i in range(len(text)):
        result.append(text[i] ^ key[i % len(key)])
    
    return result

def xor_file(file_path, key, output_path=None):
    """
    对文件内容进行XOR操作
    :param file_path: 要进行XOR操作的文件路径
    :param key: XOR密钥
    :param output_path: 输出文件路径，默认为原文件添加.xor后缀
    :return: 操作结果信息
    """
    if not os.path.exists(file_path):
        return f"错误: 文件不存在: {file_path}"
    
    if not output_path:
        output_path = file_path + ".xor"
    
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        if isinstance(key, str):
            key = key.encode('utf-8')
        
        result = bytearray()
        for i in range(len(data)):
            result.append(data[i] ^ key[i % len(key)])
        
        with open(output_path, 'wb') as f:
            f.write(result)
        
        return f"XOR操作完成，结果保存至: {output_path}"
    except Exception as e:
        return f"处理文件时出错: {str(e)}"
def xor_image(image_path, key, output_path=None):
    """
    对图片进行XOR操作
    :param image_path: 要进行XOR操作的图片路径
    :param key: XOR密钥
    :param output_path: 输出图片路径，默认为原图片添加.xor后缀
    :return: 操作结果信息
    """
    if not os.path.exists(image_path):
        return f"错误: 图片文件不存在: {image_path}"
    
    if not output_path:
        output_path = image_path + ".xor"
    
    try:
        with open(image_path, 'rb') as f:
            data = f.read()
        
        if isinstance(key, str):
            key = key.encode('utf-8')
        
        result = bytearray()
        for i in range(len(data)):
            result.append(data[i] ^ key[i % len(key)])
        
        with open(output_path, 'wb') as f:
            f.write(result)
        
        return f"图片XOR操作完成，结果保存至: {output_path}"
    except Exception as e:
        return f"处理图片时出错: {str(e)}"

