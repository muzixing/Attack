###Ataack game

These are some easy network attack examples implemented by scapy. Just play for fun.

* arp\_attack
    Attack a specific target by sending ARP packet with fake gateway information.

    Parameter: target IP

    Usage: 

        sudo python arp_attack.py 192.168.0.3

* arp\_attack\_all\_hosts
    Attack all targets in local network by sending ARP packet with fake gateway information.

    Parameter: ipprefix, mask length

    Usage:

        sudo python arp_attack_all_hosts.py 192.168.3.0, 24

* dnsAttack
    Fake DNS attacking.

    Parameter: None

    Usage: sudo python dnsAttack.py

* crawer\_thread\_pool
    DoS Attack: Start multiple threads to get resources from target website to raise the delay of answering requests.

    Parameter: number of thread, target url

    Usage:

        sudo python crawer_thread_pool.py 10 http://www.baidu.com

* ping\_of\_death
    Send a overlength ICMP packet to target host to crash down the target system. Actually, most system can defend this attack.

    Parameter: target IP

    Usage:

        sudo python ping_of_death 192.168.0.3

Enjoy it.
