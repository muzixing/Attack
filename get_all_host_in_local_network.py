#! /usr/bin/python
import sys
import nmap


def get_all_host_in_local_network(hosts):
    nm = nmap.PortScanner()
    nm.scan(hosts=hosts, arguments='-p 161 -sU ')

    hosts_list = [x for x in nm.all_hosts()]
    return hosts_list

if __name__ == '__main__':
    hosts = get_all_host_in_local_network(sys.argv[1])
    print hosts
