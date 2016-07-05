import socket
import struct
import nmap


def get_victim_in_local_network(ipprefix, mask_len):
    gateway = int_to_ip(ip_to_int(ipprefix)+1)
    victim_list = get_all_host_in_local_network(ipprefix, mask_len)
    victim_list.remove(get_my_ip())
    victim_list.remove(gateway)
    return victim_list


def get_all_host_in_local_network(ipprefix, mask_len):
    hosts = ipprefix + '/' + mask_len
    nm = nmap.PortScanner()
    nm.scan(hosts=hosts, arguments='-p 161 -sU ')
    hosts_list = [x for x in nm.all_hosts()]
    return hosts_list


def get_my_ip():
    try:
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(('8.8.8.8', 80))
        (addr, port) = csock.getsockname()
        csock.close()
        return addr
    except socket.error:
        return "127.0.0.1"


def int_to_ip(int_ip):
    return socket.inet_ntoa(struct.pack('I', socket.htonl(int_ip)))


def ip_to_int(ip):
    return socket.ntohl(struct.unpack("I", socket.inet_aton(str(ip)))[0])
