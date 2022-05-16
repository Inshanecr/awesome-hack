try:
  import pyshorteners
  from ipapi import location
  from colorama import Fore,init
  from requests import get
  from os import system 
  import re
  from time import sleep 
except Exception as e:
  print(e)




#CAMERA SCANNER    
def camScan():
 try:
    init()
    print()
    print("""
              [1] USA   [6] German
              [2] JAPAN   [7] Thailand 
              [3] Italy   [8] russia
              [4] Korea     [9] IRAN
                   [5] France  
              """)
    countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "IR"]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input("OPTIONS : "))
    if num not in range(1, 145+1):
        raise IndexError

    country = countries[num-1]
    res = get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;31m", ip)
 except:
   pass
 finally:
    print("\033[1;37m")


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
          system("clear")
          print(f"""
          {ye}[1]{y} Chilp.it {ye}[2]{y} clck.ru
          {ye}[3]{y} Da.hd   {ye} [4]{y} Is.gd
          {ye}[5]{y} Os.db    {ye}[6]{y} Tinyurl.com {re}
                  """)
          link = pyshorteners.Shortener()
          opt =int(input("which One You need :"))
          url = input("send Your URL  : ")
          if opt ==1 :
              print("shortUrl :"+link.chilpit.short(url)) 
          elif opt == 2:
             print("shortUrl :"+link.clckru.short(url))
          elif opt == 3:
             print("shortUrl :"+link.dagd.short(url))
          elif opt == 4:
             print("shortUrl :"+link.isgd.short(url))#validator
          elif opt == 5:
             print("shortUrl :"+link.osdb.short(url))
          elif opt == 6:
             print("shortUrl :"+link.tinyurl.short(url))
   
    












