from mcp.server.fastmcp import FastMCP
from typing import Optional
from tools.qrcode_plugin import decode_qrcode
from tools.base64_plugin import base64_decode
from tools.base58_plugin import decode_base58
from tools.base45_plugin import decode_base45
from tools.zip_plugin import extract_zip
from tools.xor_plugin import xor_string,xor_file,xor_image


# 创建MCP服务器
mcp = FastMCP("ctftools_Puzzle_server")


@mcp.tool()
def decode_qr(image_path: str):
    '''
    解码二维码
    :param image_path: 二维码图片路径
    :return: 解码结果
    '''
    return decode_qrcode(image_path)

@mcp.tool()
def b64_decode(text: str):
    '''
    Base64 解码
    字符集：A-Z a-z 0-9 + /
    :param text: 要解码的字符串
    :return: 解码后的字符串
    '''
    return base64_decode(text)

@mcp.tool()
def b58_decode(data: str):
    '''
    Decode Base58 data
    :param data: data to decode
    :return: decoded data
    '''
    return decode_base58(data)

@mcp.tool()
def b45_decode(data: str):
    '''
    Decode Base45 data
    :param data: data to decode
    :return: decoded data
    '''
    return decode_base45(data)

@mcp.tool()
def unzip(zip_path: str, extract_to: Optional[str] = None):
    '''
    解压缩ZIP文件
    :param zip_path: ZIP文件路径
    :param extract_to: 解压目标路径，默认为ZIP文件所在目录
    :return: 解压结果信息
    '''
    return extract_zip(zip_path, extract_to)


@mcp.tool()
def xor_string(text: str, key: str):
    '''
    对字符串进行XOR操作
    :param text: 要进行XOR操作的字符串
    :param key: XOR密钥
    :return: XOR操作后的结果
    '''
    return xor_string(text, key)

@mcp.tool()
def xor_file(file_path: str, key: str, output_path: Optional[str] = None):
    '''
    对文件内容进行XOR操作
    :param file_path: 要进行XOR操作的文件路径
    :param key: XOR密钥
    :param output_path: 输出文件路径，默认为原文件添加.xor后缀
    :return: 操作结果信息
    '''
    return xor_file(file_path, key, output_path)

@mcp.tool()
def xor_image(image_path: str, key: str, output_path: Optional[str] = None):
    '''
    对图片进行XOR操作
    :param image_path: 要进行XOR操作的图片路径
    :param key: XOR密钥
    :param output_path: 输出图片路径，默认为原图片添加.xor后缀
    :return: 操作结果信息
    '''
    return xor_image(image_path, key, output_path)


if __name__ == "__main__":
    mcp.run()