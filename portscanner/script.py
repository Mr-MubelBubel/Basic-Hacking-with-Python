#!/usr/bin/python3
import sys, time
import socket as s

if len(sys.argv) != 3:
    print('Usage:')
    print('./' + sys.argv[0] + ' [ip] [standardport-endport] \n')
    sys.exit()

ip = sys.argv[1]
ports = sys.argv[2].split('-')

ts = time.time()
print('[+] Running portscanner on {}'.format(ip))

for port in range(int(ports[0]), int(ports[1]) + 1):
    print('[+] Scanning port {}'.format(port))
    soc = s.socket(s.AF_INET, s.SOCK_STREAM)

soc.settimeout(6)
res = soc.connect_ex((ip, port))

if res == 0:
    banner = ''
    if port == 80:
        soc.send(b'GET / HTTP/1.1\r\nHost: {}\r\n\r\n'.format(ip))
    try:
        banner = soc.recv(1024)
        banner = banner.decode('UTF-8', errors='replace').strip()
        if port == 80:
            tmp = banner.split('\r\n')
            for line in tmp:
                if line.strip().lower().startswith('server'):
                    banner = line.strip()
    except:
        pass
    print('[+] Port {} is open'.format(port))

soc.close()

td = time.time() - ts
print('[+] Scanning finished in {} seconds'.format(td))