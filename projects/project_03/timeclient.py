import socket
import time

def get_time():
    seconds_delta = 2208988800
    seconds_since_unix_epoch = int(time.time())
    return seconds_delta + seconds_since_unix_epoch

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("time.nist.gov", 37))

data = s.recv(4)

s.close()

nist_time = int.from_bytes(data, "big")

print("NIST time  :", nist_time)
print("System time:", get_time())