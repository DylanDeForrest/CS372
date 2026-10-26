
def ip_to_bytes(ip):
    result = b""
    ip_split = ip.split('.')
    for section in ip_split:
        section = int(section)
        result += section.to_bytes(1, "big")
    return result


def checksum(pseudo_header, tcp_data):
    data = pseudo_header + tcp_data

    total = 0
    offset = 0

    while offset < len(data):
        word = int.from_bytes(data[offset:offset + 2], "big")
        total += word
        total = (total & 0xffff) + (total >> 16)

        offset += 2

    return (~total) & 0xffff
        
        
    
for i in range(10):
    with open(f"tcp_addrs_{i}.txt") as fp:
        src_ip, dst_ip = fp.read().split()
        
    with open(f"tcp_data_{i}.dat", "rb") as fp:
        tcp_data = fp.read()
        
        tcp_length = len(tcp_data)

    pseudo_header = (
        ip_to_bytes(src_ip)
        + ip_to_bytes(dst_ip)
        + b"\x00"
        + b"\x06"
        + tcp_length.to_bytes(2, "big")
    )

    original_checksum = int.from_bytes(tcp_data[16:18], "big")

    tcp_zero_checksum = tcp_data[:16] + b"\x00\x00" + tcp_data[18:]

    if len(tcp_zero_checksum) % 2 == 1:
        tcp_zero_checksum += b"\x00"

    calculated_checksum = checksum(pseudo_header, tcp_zero_checksum)

    if calculated_checksum == original_checksum:
        print("PASS")
    else:
        print("FAIL")


        
    