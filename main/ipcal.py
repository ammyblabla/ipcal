import ipaddress

def bit_not(n, numbits=32):
    return (1 << numbits) - 1 - n

def gen_subnet(prefix):
    subnet_int = 0
    for i in range (0, 32):
        if i >= (32-prefix):
            # print(i)
            subnet_int += 2**i
    # print(subnet_int)
    return ipaddress.IPv4Address(subnet_int)

def is_ip(ip_str):
    try:
        ip = ipaddress.IPv4Address(ip_str)
        return True
    except:
        return False

def is_prefix(prefix_str):
    try:
        prefix = int(prefix_str)
        if (prefix > 0) and (prefix < 32):
            return True
        return False
    except:
        return False

def network_address(ip, prefix):
    subnet = int(gen_subnet(prefix))
    ip_int = int(ip)
    ans = ipaddress.IPv4Address(subnet & ip_int)
    return ans

def get_ip_network(ip, prefix):
    network_addr = network_address(ip, prefix)
    ip_network_string = str(network_addr) + '/' + str(prefix)
    # print(ip_network_string)
    return ipaddress.ip_network(ip_network_string)

def broadcast_address(ip, prefix):
    or_address = bit_not(int(gen_subnet(prefix)))
    ip_int = int(ip)
    ans = ipaddress.IPv4Address(or_address | ip_int)
    return ans

def host_no(prefix):
    return 2**(32-prefix)

def usable_host_no(prefix):
    return host_no(prefix) - 2

def get_all_host(ip_network):
    return list(ip_network.hosts()) 

def get_class(ip):
    ip_str = str(ip)
    first_octimal = int(ip_str.split('.')[0])
    
    if first_octimal <= 127:
        return 'A'
    elif first_octimal <= 191:
        return 'B'
    elif first_octimal <= 223:
        return 'C'
    elif first_octimal <= 239:
        return 'D'
    else:
        return 'E'

def usable_range(ip_addr, prefix):
    upper_bound = str(broadcast_address(ip_addr, prefix)-1)
    lower_bound = str(network_address(ip_addr, prefix)+1)
    return lower_bound + ' - ' + upper_bound

# if __name__ == '__main__':
#     # ip_str = input()
#     # prefix = int(input())
#     ip_str = '158.108.12.24'
#     ip = ipaddress.IPv4Address(ip_str)
#     prefix = 24
#     subnet = gen_subnet(prefix)
#     ip_network = get_ip_network(ip, prefix)
#     # print(network_address(ip, prefix))
#     # print(broadcast_address(ip, prefix))
#     # print(host_no(prefix))
#     # print(ip)
#     # print(get_ip_network(ip, prefix))
#     # print(get_all_host(ip_network))
#     print(usable_range(ip, prefix))

# ip
# network address
# useable host ip range
# broadcast address
# total number of hosts
# subnet mask
# ip class
# cidr notation (prefix)