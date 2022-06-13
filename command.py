from os import system 
from banner import *
system("apt install neofetch")
clear()
#Libaries
try:
  from faker import Faker
  import pyshorteners
  import random 
  from ipapi import location
  from colorama import Fore,init
  from requests import get
  import re
  from time import sleep
except ImportError:
    exit("please install Libary\ncommand => python -m pip install -r requirements.txt")

#CAMERA IP FINDER    
def camScan():
 try:
    print()
    colors =['\033[31m','\033[32m','\033[33m','\033[34m','\033[35m','\033[36m','\033[37m','\033[93m']
    Q = random.choice(colors)
    
    print(f"""{Q}
             [1] USA     [6] German
             [2] JAPAN   [7] Thailand 
             [3] Italy   [8] russia
             [4] Korea   [9] IRAN
                  [5] France  
              """)
    countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "IR"]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input('\033[36m'+"OPTIONS : "))
    if num not in range(1, 145+1):
        raise IndexError

    country = countries[num-1]
    res = get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]
    count = 0
    for page in range(int(last_page)):
        res = get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        count+=1
        print("\033[1;37m"+str(count))
        for ip in find_ip:
            print("\033[1;31m", ip)
 except KeyboardInterrupt:
   exit('\033[37m'+"\nGoodBye\n")
 finally:
    print("\033[1;37m"+"\nplease copy all ip\n")
    sleep(5)


#URL SHORTETR
def short():
        try:
            y = Fore.GREEN
            ye = Fore.YELLOW
            re = Fore.RESET
            print(f"""
            {ye}[1]{y} Chilp.it {ye}[2]{y} clck.ru
            {ye}[3]{y} Da.hd   {ye} [4]{y} Is.gd
            {ye}[5]{y} Os.db    {ye}[6]{y} Tinyurl.com {re}
                    """)
            link = pyshorteners.Shortener()
            opt =int(input('\033[34m'+"which One You need :"))
            url = input('\033[35m'+"send Your URL  : ")
            cy ='\033[36m'
            if opt ==1 :
                print(cy+"\nshortUrl :"+link.chilpit.short(url)) 
            elif opt == 2:
               print(cy+"\nshortUrl :"+link.clckru.short(url))
            elif opt == 3:
               print(cy+"\nshortUrl :"+link.dagd.short(url))
            elif opt == 4:
               print(cy+"\nshortUrl :"+link.isgd.short(url))#validator
            elif opt == 5:
               print(cy+"\nshortUrl :"+link.osdb.short(url))
            elif opt == 6:
               print(cy+"\nshortUrl :"+link.tinyurl.short(url))
        
        except Exception as e:
            exit(Fore.RED+"\n[-] please turn on VPN\n")
        except KeyboardInterrupt:
          exit(Fore.CYAN+"\nGoodbye")

#GET FAKE USER INFORMATION 
def getInfo():

  try:
    country = input(Fore.YELLOW+"send Your country name[example: fa-ir] : ")
    number = int(input(Fore.LIGHTBLUE_EX+"How much you need : "))
    count = 0
    faker = Faker(country)#Get Faker information 
    un = faker.user_name()
    fn= faker.name()
    pwd = faker.password()
    el = faker.email()
    jn = faker.job()
    adrs = faker.address()
    with open("file-fake.txt","w") as file:
        for i in range(1,number+1):
             count += 1
             file.write(f"""
[{count}]  -------------------------------
🗿 ＦＵＬＬ ＮＡＭＥ  = {fn}
⚙️ ＵＳＥＲ ＮＡＭＥ  = {un}
💳 ＰＡＳＳＷＯＲＤ = {pwd}
🛰 ＥＭＡＩＬ  = {el}
🏦 ＪＯＢ = {jn}
🏘 ＡＤＤＲＥＳＳ = {adrs}
             """)
        file.close()
        print(Fore.GREEN+"\nplease check file-fake.txt  "+Fore.RESET)
  
  except AttributeError:
      exit(Fore.CYAN+"\nplease write country short name"+Fore.RED+"\nexample => German: de "+Fore.RESET)
  except KeyboardInterrupt:
    exit(Fore.CYAN+"\nGoodbye")



