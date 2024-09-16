#!/usr/bin/python

# import qilinadigan kutubxonalar

import socket
import time 
import  subprocess
import os


'''
port scanner qilish uchun boshlang'ich dastur
coder: hac0_net
'''
os.system("clear")
subprocess.call("figlet -t port scanner ",shell=True)
subprocess.call("figlet  -t  'by hac0_net' ",shell=True)
pockets = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
host=input("targetni kitiring :  target=")
print("aynan bitta portni tekshirmoqchimisiz yoki ko'proq")
id1=int(input("bitta port (1) / ko'proq port (0) : ID="))

def check_id1():
	if id1==1:
		scan_port(host)
	elif id1==0:
		scan_ports(host)
	else:
		print("siz noto'g'ri qiymat kiritdingiz !!!")
		print("yana urunib ko'rasizmi !!!")
		id2=input("yes/no : ID=")
		if id2.lower()=='yes':
			check_id1()
		else:
			print('dastur yakunlandi !!!')

def scan_port(host):
	port=int(input("portni kiriting : port="))
	if pockets.connect_ex((host , port)):
		print("target={} port={} port yopiq ---".format(host,port))
		
	else:
		print("target={} port={} port ochiq +++".format(host,port))
	print("dastur yakunlandi !!!")
	
	
def scan_ports(host):#!
	print("port chegaralarini kiriting.")
	id3=int(input(" quyi chegara : <<")) 
	id4=int(input(" yuqori chegara : >>"))
	for port in range(id3,id4+1):
		if pockets.connect_ex((host , port)):
       			print("target={} port={} port yopiq ---".format(host,port))
		else:
	        	print("target={} port={} port ochiq +++".format(host,port))
		time.sleep(1)
	print("dastur yakunlandi !!!")
	
check_id1()
	
	


