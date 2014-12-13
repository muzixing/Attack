from scapy import *
from scapy.all import *

a = IP(dst='8.8.8.8', src="10.103.22.202") #192.168.1.200 为伪造的源ip
b = UDP(dport=53)
c = DNS(id=1, qr=0, opcode=0, tc=0,
	rd=1, qdcount=1, ancount=0, nscount=0, arcount=0)
c.qd=DNSQR(qname='www.qq.com', qtype=1, qclass=1)
p = a/b/c
send(p)