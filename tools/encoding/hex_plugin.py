import binascii

def hex_encode(data):
    """
    Hex 编码
    :param data: 要编码的数据
    :return: 编码后的十六进制字符串
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return binascii.hexlify(data).decode('utf-8')

def hex_decode(data):
    """
    Hex 解码
    :param data: 要解码的十六进制字符串
    :return: 解码后的数据
    """
    try:
        return binascii.unhexlify(data).decode('utf-8')
    except UnicodeDecodeError:
        return binascii.unhexlify(data)
