# ----- T.me/LooQaat || T.me/Pythonte ----
from os import system
import subprocess
from time import sleep
try:
  from colorama import Fore,init  
  from command import *
  from banner import *
except ImportError:
    exit("please Install Libaries\ncommand => python -m pip install -r requirements.txt")

#check neofetch
neofetch = subprocess.getoutput("neofetch")
if "not found" in neofetch:
  system("apt install neofetch")
  exit("please Run Script again")


while True:
 try: 
   clear()
   system("neofetch")
   banner()
   user =input(Fore.CYAN+"which Tool You need : ")
   if user == "1":
          clear()
          Urlban()
          short()
   elif user == "2":
          clear()
          CameraBan()
          camScan()
   elif user == "3":
          clear()
          Fakeban()
          getInfo()
   elif user == "0":
          exit("\nGoodbye")
 except KeyboardInterrupt:
    exit(Fore.CYAN+"\nGoodbye")
 
