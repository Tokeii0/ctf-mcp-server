import base64

def base64_encode(text):
    """
    Base64 编码
    :param text: 要编码的字符串
    :return: 编码后的字符串
    """
    message_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')
    return base64_message

def base64_decode(text):
    """
    Base64 解码
    :param text: 要解码的字符串
    :return: 解码后的字符串
    """
    base64_bytes = text.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('utf-8')
    return message
