def ip_to_bytes(ip):
    ip_split = ip.split('.')
    octets = []
    for i in range(len(ip_split)):
        octets.append(int(ip_split[i]))
    return (octets[0] << 24) | (octets[1] << 16) | (octets[2] << 8) | octets[3]

def decimal_to_ip(dec):
    a = (dec >> 24) & 255
    b = (dec >> 16) & 255
    c = (dec >> 8) & 255
    d = dec & 255
    return f"{a}.{b}.{c}.{d}"
    
    
print(decimal_to_ip(3325256824))
print(ip_to_bytes("192.168.1.2"))

