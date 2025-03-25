from mcp.server.fastmcp import FastMCP
from typing import Optional
from tools.qrcode_plugin import encode_qrcode
from tools.encoding import base64_encode, encode_base58, encode_base45, hex_encode
from tools.zip_plugin import zip_file
from tools.xor_plugin import xor_string,xor_file,xor_image
from tools.pic.acg_pic_plugin import get_acg_image
from tools.pic.lsb_plugin import lsb_encode


# 创建MCP服务器
mcp = FastMCP("ctftools_feces_making_machine_server")


@mcp.tool()
def create_qr(text: str, size: Optional[int] = 200, savepath: Optional[str] = '', filename: Optional[str] = "qrcode.png"):
    '''
    生成二维码
    :param text: 二维码内容
    :param size: 二维码大小
    :param savepath: 保存路径,不要使用相对路径
    :param filename: 保存文件名
    :return: 生成结果
    '''
    return encode_qrcode(text, size, savepath, filename)

@mcp.tool()
def get_acg_image_(save_path: Optional[str] = None, filename: Optional[str] = None):
    '''
    获取随机ACG图片
    :param save_path: 保存路径，默认为当前目录
    :param filename: 保存的文件名，默认为随机生成
    :return: 保存结果信息
    '''
    return get_acg_image(save_path, filename)
@mcp.tool()
def lsb_encode_(image_path: str, text: str, output_path: Optional[str] = None):
    '''
    从图片中提取LSB隐写信息
    :param image_path: 图片路径
    :param text: 要隐写的信息
    :param output_path: 输出图片路径，默认为原图片添加.lsb后缀
    :return: 操作结果信息
    '''
    return lsb_encode(image_path, text, output_path)

@mcp.tool()
def hex_encode_(text: str):
    '''
    Hex 编码
    :param text: 要编码的字符串
    :return: 编码后的字符串
    '''
    return hex_encode(text)

@mcp.tool()
def b64_encode(text: str):
    '''
    Base64 编码
    :param text: 要编码的字符串
    :return: 编码后的字符串
    '''
    return base64_encode(text)


@mcp.tool()
def b58_encode(data: str):
    '''
    Encode data to Base58
    :param data: data to encode
    :return: encoded data
    '''
    return encode_base58(data)

@mcp.tool()
def b45_encode(data: str):
    '''
    Encode data to Base45
    :param data: data to encode
    :return: encoded data
    '''
    return encode_base45(data)


@mcp.tool()
def zip_file_(file_path: str, zip_path: str):
    '''
    压缩文件
    :param file_path: 要压缩的文件路径
    :param zip_path: 压缩后的ZIP文件路径
    :return: 压缩结果信息
    '''
    return zip_file(file_path, zip_path)

@mcp.tool()
def xor_string_(text: str, key: str):
    '''
    对字符串进行XOR操作
    :param text: 要进行XOR操作的字符串
    :param key: XOR密钥
    :return: XOR操作后的结果
    '''
    return xor_string(text, key)

@mcp.tool()
def xor_file_(file_path: str, key: str, output_path: Optional[str] = None):
    '''
    对文件内容进行XOR操作
    :param file_path: 要进行XOR操作的文件路径
    :param key: XOR密钥
    :param output_path: 输出文件路径，默认为原文件添加.xor后缀
    :return: 操作结果信息
    '''
    return xor_file(file_path, key, output_path)

@mcp.tool()
def xor_image_(image_path: str, key: str, output_path: Optional[str] = None):
    '''
    对图片进行XOR操作
    :param image_path: 要进行XOR操作的图片路径
    :param key: XOR密钥
    :param output_path: 输出图片路径，默认为原图片添加.xor后缀
    :return: 操作结果信息
    '''
    return xor_image(image_path, key, output_path)
# uuid
@mcp.tool()
def uuid():
    import uuid
    '''
    生成UUID
    :return: UUID
    '''
    return str(uuid.uuid4())

if __name__ == "__main__":
    mcp.run()