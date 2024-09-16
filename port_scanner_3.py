#!/usr/bin/python

import socket
import optparse
import threading 
import subprocess
import os

'''
port scannerlash uchun to'liq dastur 
coder: hac0_net
'''
os.system("clear")
def scan(dhost, dport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((dhost, dport)):
        print(f"Port {dport} yopiq")
    else:
        print(f"Port {dport} ochiq")
    s.close()

def main():
    subprocess.call("figlet -t port scanner ",shell=True)
    subprocess.call("figlet  -t  'by hac0_net' ",shell=True)
    parser = optparse.OptionParser("use -> ./filename(chmod +x filename) --h hostname --p port ")
    parser.add_option("--h", dest="dhost", type=str, help="Hostni aniqlashtirish")
    parser.add_option("--p", dest="dport", type=str, help="Portni aniqlashtirish")
    (options, args) = parser.parse_args()
    dhost = options.dhost
    dport = str(options.dport).split(",")

    if (dhost == None) or (dport[0] == None):
        print(parser.usage)
        exit()
    else:
        scanner(dhost, dport)

def scanner(dhost, dport):
    try:
        tghost = socket.gethostbyname(dhost)
    except socket.gaierror:
        print("Host xato kiritildi!")
        return

    try:
        tgname = socket.gethostbyaddr(dhost)
        print(f"{dhost}-host <-> {tgname[0]}-name")
    except socket.herror:
       	pass

    for port in dport:
        t = threading.Thread(target=scan, args=(dhost, int(port)))
        t.start()

if __name__ == "__main__":
    main()

