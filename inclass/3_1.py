import socket

message = "this is the message"

value = 44

def encode_data(message, value):
    message_encoded = message.encode('utf-8')
    total_length = 2 + len(message_encoded) + 4
    total_bytes = total_length.to_bytes(2, "big")
    value_bytes = value.to_bytes(4, "big", signed=True)
    
    data = bytearray()
    data.extend(total_bytes)
    data.extend(message_encoded)
    data.extend(value_bytes)
    
    return data
    
data = encode_data(message, value)


def decode_data(data):
    total_length = int.from_bytes(data[:2], "big")
    
    message = data[2:total_length - 4].decode("utf-8")
    
    value = int.from_bytes(
        data[total_length - 4:total_length], "big", signed=True
        )
    return message, value

print(decode_data(data))