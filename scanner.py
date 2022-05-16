#------ T.me\LooQaat|T.me/Pythonte ------

try:
  from colorama import Fore,init
  from os import system 
  from time import sleep 
  from command import *
except ImportError:
    system("pip install colorama ")


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
