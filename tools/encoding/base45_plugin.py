import base45

def encode_base45(data):
    """
    Encode data to Base45
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return base45.b45encode(data).decode('utf-8')

def decode_base45(data):
    """
    Decode Base45 data
    """
    try:
        return base45.b45decode(data).decode('utf-8')
    except:
        return base45.b45decode(data)
