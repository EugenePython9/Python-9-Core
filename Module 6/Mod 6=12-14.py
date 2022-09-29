import base64


def encode_data_to_base64(data):
    spysok = []
    for item in data:
        spysok.append((base64.b64encode(item.encode('utf-8'))).decode('utf-8'))
    return spysok
        
        