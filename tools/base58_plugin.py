import base58

def encode_base58(data):
    """
    Encode data to Base58
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return base58.b58encode(data).decode('utf-8')

def decode_base58(data):
    """
    Decode Base58 data
    """
    try:
        return base58.b58decode(data).decode('utf-8')
    except:
        return base58.b58decode(data)

