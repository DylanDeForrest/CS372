
ips = (([192,168,17,2], [255,0,0,0]), 
       ([192,168,17,2], [255,255,0,0]), 
       ([192,168,17,2], [255,255,255,0]),
       ([192,168,17,2], [255,192,0,0]), 
       ([192,168,17,2], [255,255,248,0]))

new = []


for ip, mask in ips:
    network = []
    host = []
    for i in range(4):
        net_byte = ip[i] & mask[i]
        network.append(net_byte)
    
        host_byte = ip[i] & (~mask[i] & 0xff)
        host.append(host_byte)
        
    new.append((network, host))
    
for p in new: 
    print(p)
    
        
        
