from os import system 
system("apt install neofetch")
system("clear")
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
    system("pip install random")
    system("pip install faker")
    system("pip install requests")
    system("pip install time")
    system("pip install colorama")
    system("pip install ipapi")
    system("pip install pyshorteners")
    exit("\nRun script again")




#CAMERA SCANNER    
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
      y = Fore.GREEN
      ye = Fore.YELLOW
      re = Fore.RESET
      ip = get("https://api.ipify.org").text
      print('\n' + Fore.MAGENTA + ip + Fore.RESET)
      http = get("https://api.ipify.org").text
      cou = location(http)["country"]
      if cou == "IR":
          exit(Fore.LIGHTBLACK_EX + "Your IP has " + Fore.LIGHTRED_EX + "BLOCKED from server" + Fore.LIGHTBLUE_EX + "[ Turn on VPN ] " + Fore.RESET + '|' + Fore.RED + " Your country "+ Fore.WHITE +" ↬ " +Fore.GREEN + cou +"\n\n\n\n"+Fore.RESET)
      else:
        try:
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
        
        except KeyboardInterrupt:
          exit(Fore.CYAN+"\nGoodbye")
 
def getInfo():
  try:
    country = input(Fore.YELLOW+"send Your country name : ")
    faker = Faker(country)
    number = int(input(Fore.LIGHTBLUE_EX+"How much you need : "))
    file = open("file-fake.txt","w")
    for i in range(1,number+1):
         fn= faker.name()
         un = faker.user_name()
         pwd = faker.password()
         el = faker.email()
         jn = faker.job()
         adrs = faker.address()
         file.write(f"""
    fullname = {fn}
    username = {un}
    password = {pwd}
    email = {el}
    job = {jn}
    address = {adrs}
         """)
        
    file.close()
    print(Fore.GREEN+"\nplease check file-fake.txt  "+Fore.RESET)
  
  except AttributeError:
      exit(Fore.CYAN+"\nplease write country short name"+Fore.RED+"\nexample => German: de "+Fore.RESET)
  except KeyboardInterrupt:
    exit(Fore.CYAN+"\nGoodbye")

