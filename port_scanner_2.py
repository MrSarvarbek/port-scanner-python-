#!/usr/bin/python

import socket
import optparse
import threading 
import 	subprocess
import os

'''
port scannerlash uchun dastur optparse modulidan foydalanilgan 
coder: hac0_net
'''
os.system("clear")
subprocess.call("figlet -t port scanner ",shell=True)
subprocess.call("figlet  -t  'by hac0_net' ",shell=True)
def  scan(host,port):
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if s.connect_ex((host,port)):
		print(f"Port {port} yopiq")
	else:
		print(f"Port {port} ochiq")
	s.close()

def main():
    	
	parser=optparse.OptionParser("use -> ./filename(chmod +x filename) --h hostname --p port ")
	parser.add_option("--h" , dest="host" , help="target hostini/ip/kiritish!!!")
	parser.add_option("--p", dest="port" , help="taget portini kitish!!!")
	(options,args)=parser.parse_args()
	host=options.host
	port=str(options.port).split(",")
	
	if (host==None) | (port==None):
		print(parser.usage)
		exit()
	else:
		scanner(host,port)
		
def scanner(host,port):
	for iport in port:
		t=threading.Thread(target=scan, args=(host,int(iport)))
		t.start()

	
if __name__ == "__main__":
    main()

	


