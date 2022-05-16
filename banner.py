from time import sleep 
from colorama import Fore
y = Fore.GREEN
ye = Fore.YELLOW
re = Fore.RESET
def banner():#banner
  ban =(f"""
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤

{ye}[3] >>{y} Get Fake information

{ye}[2] >>{y} Show hacked camera
                            
{ye}[1] >>{y} URL shorter
                              
{ye}[0] >>{y} exit {re}
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
""")
  for Line in ban.split("\n"):
    sleep(0.1)
    print(Line)        
