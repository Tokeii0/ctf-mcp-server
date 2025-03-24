import os
from PIL import Image
from pyzbar.pyzbar import decode
import qrcode
def encode_qrcode(text, size,savepath, filename):
    """
    生成二维码
    :param text: 二维码内容
    :param size: 二维码大小
    :param savepath: 保存路径,不要使用相对路径
    :param filename: 保存文件名
    :return: 生成结果
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    if savepath != '':
        # 确保保存路径存在
        if not os.path.exists(savepath):
            os.makedirs(savepath, exist_ok=True)
        # 使用os.path.join正确拼接路径
        save_file_path = os.path.join(savepath, filename)
    else:
        save_file_path = filename
        
    img.save(save_file_path)
    return f"二维码已保存到: {save_file_path}"
    

def decode_qrcode(image_path):
    """
    解码二维码
    :param image_path: 二维码图片路径
    :return: 解码结果
    """
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
        return None

    try:
        # 加载图片
        decoded_objects = decode(Image.open(image_path))

        if decoded_objects:
            # Extract the data from the first decoded object
            data = decoded_objects[0].data.decode('utf-8')
            return data
        else:
            print("No QR code detected or unable to decode.")
            return None
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return None
