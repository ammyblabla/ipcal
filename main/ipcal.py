import ipaddress

def bit_not(n, numbits=32):
    return (1 << numbits) - 1 - n

def gen_subnet(prefix):
    subnet_int = 0
    for i in range (0, 32):
        if i >= (32-prefix):
            subnet_int += 2**i
    return ipaddress.IPv4Address(subnet_int)

def wildcard_mask(ip):
    subnet = gen_subnet(ip)
    ip_not_int = bit_not(int(subnet))
    ip_not = ipaddress.IPv4Address(ip_not_int)
    return ip_not

def is_ip(ip_str):
    try:
        ip = ipaddress.IPv4Address(ip_str)
        return True
    except:
        return False

def is_prefix(prefix_str):
    try:
        prefix = int(prefix_str)
        if (prefix > 0) and (prefix <= 32):
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
    return ipaddress.ip_network(ip_network_string)

def broadcast_address(ip, prefix):
    or_address = bit_not(int(gen_subnet(prefix)))
    ip_int = int(ip)
    ans = ipaddress.IPv4Address(or_address | ip_int)
    return ans

def host_no(prefix):
    if prefix == 32:
        return 1
    return 2**(32-prefix)

def usable_host_no(prefix):
    if prefix == 32:
        return 0
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

def binary_ip(ip):
    ip_bin = bin(int(ip))
    ip_str = str(ip_bin)[2::]
    return ip_str

def binary_subnet_mask(prefix):
    subnet_str = str(gen_subnet(prefix))
    subnet_list_str = subnet_str.split('.')
    subnet_bin_str = []
    for i in subnet_list_str:
        binary_str =  binary_ip(i)
        while(len(binary_str) < 8):
            binary_str = '0' + binary_str
        subnet_bin_str.append(binary_str)
    point = '.'
    return point.join(subnet_bin_str)

def hex_ip(ip):
    return str(hex(int(ip)))

def ip_type(ip):
    if ip.is_multicast:
        return 'Multicast'
    elif ip.is_loopback:
        return 'Loopback'
    elif ip.is_private:
        return 'Private'
    else:
        return 'Public'

def all_possible_network(ip, prefix):
    network_ip = network_address(ip, prefix)
    start_prefix = (prefix//8) * 8
    network_ip_for_start_prefix = network_address(ip, start_prefix)
    ans = []
    for i in range(0, 2**(prefix - start_prefix)):
        ip_detail = {}
        this_ip_int = (i)*(2 ** (32-prefix)) + int(network_ip_for_start_prefix)
        this_ip = ipaddress.IPv4Address(this_ip_int)
        ip_detail['this_ip'] = str(this_ip)
        ip_detail['range'] = usable_range(this_ip, prefix)
        ip_detail['broadcast'] = str(broadcast_address(this_ip, prefix))
        print(ip_detail)
        ans.append(ip_detail)
    return ans


def generate_all_subnet_list():
    ans_list=[]
    for i in range(0, 32):
        subnet_ip = str(gen_subnet(32-i))+'/'+str(32-i)
        tup = ((32-i),subnet_ip)
        ans_list.insert(i, tup)
    return tuple(ans_list)