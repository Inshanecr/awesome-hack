# ----- T.me/LooQaat || T.me/Pythonte ----
from os import system
try:
  from colorama import Fore,init 
  from time import sleep 
  from command import *
  from banner import *
except ImportError:
    system("pip install colorama ")


system("clear")
system("neofetch")

while True:
 try: 
   banner()
   user =input(Fore.CYAN+"which Tool You need : ")
   system("clear")
   if user == "1":
          short()
   elif user == "2":
          camScan()
   elif user == "0":
        exit("Goodbye")
 except KeyboardInterrupt:
    exit(Fore.CYAN+"\nGoodbye")
 



   
#pyshorteners.exceptions.ShorteningErrorException:
