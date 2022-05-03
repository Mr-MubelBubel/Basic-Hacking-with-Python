#!/usr/bin/python3

from scapy.all import *

pcap = rdpcap('snappy-sniffer.pcap')

for pkt in pcap:
    print(pkt[IP].scr + ' --> ' + pkt[IP].dst)