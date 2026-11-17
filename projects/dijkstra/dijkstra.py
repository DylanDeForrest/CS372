import sys
import json
import math  # If you want to use math.inf for infinity

def find_router(routers, ip):
    for router in routers:
        if router.split(".")[:3] == ip.split(".")[:3]:
            return router

    return None


def dijkstras_shortest_path(routers, src_ip, dest_ip):
    """
    This function takes a dictionary representing the network, a source
    IP, and a destination IP, and returns a list with all the routers
    along the shortest path.

    The source and destination IPs are **not** included in this path.

    Note that the source IP and destination IP will probably not be
    routers! They will be on the same subnet as the router. You'll have
    to search the routers to find the one on the same subnet as the
    source IP. Same for the destination IP. [Hint: make use of your
    find_router_for_ip() function from the last project!]

    The dictionary keys are router IPs, and the values are dictionaries
    with a bunch of information, including the routers that are directly
    connected to the key.

    This partial example shows that router `10.31.98.1` is connected to
    three other routers: `10.34.166.1`, `10.34.194.1`, and `10.34.46.1`:

    {
        "10.34.98.1": {
            "connections": {
                "10.34.166.1": {
                    "netmask": "/24",
                    "interface": "en0",
                    "ad": 70
                },
                "10.34.194.1": {
                    "netmask": "/24",
                    "interface": "en1",
                    "ad": 93
                },
                "10.34.46.1": {
                    "netmask": "/24",
                    "interface": "en2",
                    "ad": 64
                }
            },
            "netmask": "/24",
            "if_count": 3,
            "if_prefix": "en"
        },
        ...

    The "ad" (Administrative Distance) field is the edge weight for that
    connection.

    **Strong recommendation**: make functions to do subtasks within this
    function. Having it all built as a single wall of code is a recipe
    for madness.
    """

    # TODO Write me!
    start = find_router(routers, src_ip)
    end = find_router(routers, dest_ip)
    
    if start == end:
        return []
    
    distance = {}
    parent = {}
    to_visit = list(routers)
    
    for router in routers:
        distance[router] = float("inf")
        parent[router] = None
    
    distance[start] = 0
    
    while to_visit:
        current = None
    
        for router in to_visit:
            if current is None or distance[router] < distance[current]:
                current = router
    
        if distance[current] == float("inf"):
            break
    
        to_visit.remove(current)
            
        for neighbor in routers[current]["connections"]:
            cost = routers[current]["connections"][neighbor]["ad"]
            new_distance = distance[current] + cost
    
            if neighbor in to_visit and new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                parent[neighbor] = current
    
    path = []
    current = end
    
    while current:
        path.append(current)
        current = parent[current]
    
    path.reverse()
    
    if path[0] != start:
        return []
    
    return path

#------------------------------
# DO NOT MODIFY BELOW THIS LINE
#------------------------------
def read_routers(file_name):
    with open(file_name) as fp:
        data = fp.read()

    return json.loads(data)

def find_routes(routers, src_dest_pairs):
    for src_ip, dest_ip in src_dest_pairs:
        path = dijkstras_shortest_path(routers, src_ip, dest_ip)
        print(f"{src_ip:>15s} -> {dest_ip:<15s}  {repr(path)}")

def usage():
    print("usage: dijkstra.py infile.json", file=sys.stderr)

def main(argv):
    try:
        router_file_name = argv[1]
    except:
        usage()
        return 1

    json_data = read_routers(router_file_name)

    routers = json_data["routers"]
    routes = json_data["src-dest"]

    find_routes(routers, routes)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    
