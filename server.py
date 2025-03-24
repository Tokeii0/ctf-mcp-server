from mcp.server.fastmcp import FastMCP
from typing import Optional
from tools.qrcode_plugin import encode_qrcode,decode_qrcode
from tools.base64_plugin import base64_encode,base64_decode
from tools.base58_plugin import encode_base58,decode_base58


# 创建MCP服务器
mcp = FastMCP("ctftools")


# 注册一个处理函数
import qrcode

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
def decode_qr(image_path: str):
    '''
    解码二维码
    :param image_path: 二维码图片路径
    :return: 解码结果
    '''
    return decode_qrcode(image_path)

@mcp.tool()
def b64_encode(text: str):
    '''
    Base64 编码
    :param text: 要编码的字符串
    :return: 编码后的字符串
    '''
    return base64_encode(text)

@mcp.tool()
def b64_decode(text: str):
    '''
    Base64 解码
    :param text: 要解码的字符串
    :return: 解码后的字符串
    '''
    return base64_decode(text)

@mcp.tool()
def b58_encode(data: str):
    '''
    Encode data to Base58
    :param data: data to encode
    :return: encoded data
    '''
    return encode_base58(data)

@mcp.tool()
def b58_decode(data: str):
    '''
    Decode Base58 data
    :param data: data to decode
    :return: decoded data
    '''
    return decode_base58(data)

if __name__ == "__main__":
    mcp.run()