from PIL import Image
import numpy as np
import os

def lsb_decode(image_path):
    """
    从图片中提取LSB隐写信息
    :param image_path: 图片路径
    :return: 提取的信息
    """
    if not os.path.exists(image_path):
        return f"错误: 图片文件不存在: {image_path}"
    
    try:
        img = Image.open(image_path)
        pixels = np.array(img)
        
        # 提取最低有效位
        extracted_bits = []
        for row in pixels:
            for pixel in row:
                # 对RGB通道提取LSB
                for color in pixel[:3]:  # 只处理RGB通道，不处理Alpha
                    extracted_bits.append(color & 1)  # 获取最低位
        
        # 将位转换为字节
        extracted_bytes = []
        null_byte_count = 0
        for i in range(0, len(extracted_bits), 8):
            if i + 8 <= len(extracted_bits):
                byte = 0
                for j in range(8):
                    byte = (byte << 1) | extracted_bits[i + j]
                extracted_bytes.append(byte)
                
                # 检测连续的空字节作为终止符
                if byte == 0:
                    null_byte_count += 1
                    if null_byte_count >= 3:  # 连续3个空字节视为终止
                        break
                else:
                    null_byte_count = 0
        
        # 如果找到终止符，截断数据
        if null_byte_count >= 3 and len(extracted_bytes) > 3:
            extracted_bytes = extracted_bytes[:-3]  # 移除终止符
        
        # 尝试将字节转换为文本
        try:
            message = bytes(extracted_bytes).decode('utf-8').strip('\x00')
            return message
        except UnicodeDecodeError:
            # 如果无法解码为文本，返回十六进制表示
            return bytes(extracted_bytes).hex()
            
    except Exception as e:
        return f"处理图片时出错: {str(e)}"

def lsb_encode(image_path, message, output_path=None):
    """
    将信息隐写到图片的LSB中
    :param image_path: 原图片路径
    :param message: 要隐写的信息
    :param output_path: 输出图片路径，默认为原图片添加.lsb后缀
    :return: 操作结果信息
    """
    if not os.path.exists(image_path):
        return f"错误: 图片文件不存在: {image_path}"
    
    if not output_path:
        output_path = image_path + ".lsb"
    
    try:
        # 将消息转换为位
        if isinstance(message, str):
            message = message.encode('utf-8')
        
        message_bits = []
        for byte in message:
            for i in range(7, -1, -1):
                message_bits.append((byte >> i) & 1)
        
        # 打开图片并获取像素
        img = Image.open(image_path)
        pixels = np.array(img).copy()  # 创建副本避免修改原数组
        
        # 检查图片容量是否足够
        max_bits = pixels.size * 3  # RGB通道
        if len(message_bits) > max_bits:
            return f"错误: 消息太长，图片容量不足。最大可存储 {max_bits//8} 字节"
        
        # 嵌入消息
        bit_index = 0
        for i in range(pixels.shape[0]):
            for j in range(pixels.shape[1]):
                for k in range(3):  # RGB通道
                    if bit_index < len(message_bits):
                        # 确保像素值保持在有效范围内
                        if message_bits[bit_index] == 1:
                            pixels[i, j, k] = pixels[i, j, k] | 1  # 设置最低位为1
                        else:
                            pixels[i, j, k] = (pixels[i, j, k] & 254)  # 设置最低位为0，使用 254 (11111110) 代替 ~1
                        bit_index += 1
                    else:
                        break
                if bit_index >= len(message_bits):
                    break
            if bit_index >= len(message_bits):
                break
        
        # 保存修改后的图片
        Image.fromarray(pixels).save(output_path)
        return f"LSB隐写完成，结果保存至: {output_path}"
        
    except Exception as e:
        return f"处理图片时出错: {str(e)}"


# # 测试写入 D:\AI\nav\stego_image.png test123
# if __name__ == "__main__":
#     #print(lsb_encode(r"D:\AI\nav\stego_image.png", "test123", r"D:\AI\nav\stego_image_lsb.png"))
#     print(lsb_decode(r"D:\AI\nav\stego_image_lsb.png"))
