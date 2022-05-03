#!/usr/bin/python3

from numpy import append
from scapy.all import *

def write_pkt(pkt):
    wrpcap('snappy-sniffer.pcap', pkt, append=True)

sniff(iface='eth0', prn=write_pkt, store=0)
