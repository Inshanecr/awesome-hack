try:
  import pyshorteners
  from ipapi import location
  from colorama import Fore,init
  from requests import get
  from os import system 
  import re
  from time import sleep 
  from command import *
except Exception as e:
  print(e)

system("clear")
system("neofetch")

y = Fore.GREEN
ye = Fore.YELLOW
re = Fore.RESET
def banner():#banner
  ban =(f"""
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
{ye}[2] >>{y} Show hacked camera
                            
{ye}[1] >>{y} URL shorter
                              
{ye}[0] >>{y} exit {re}
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
""")
  for Line in ban.split("\n"):
    sleep(0.1)
    print(Line)
          
while True:
   banner()
   user =input("which Tool You need : ")
   system("clear")
   if user == "1":
          short()
   elif user == "2":
          camScan()
   elif user == "0":
        exit("Goodbye")
 



#pyshorteners.exceptions.ShorteningErrorException: