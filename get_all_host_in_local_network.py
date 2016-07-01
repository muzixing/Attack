#! /usr/bin/python
import nmap


def get_all_host_in_local_network(hosts):
    nm = nmap.PortScanner()
    nm.scan(hosts=hosts, arguments='-p 161 -sU ')

    hosts_list = [x for x in nm.all_hosts()]
    print hosts_list
    return hosts_list
