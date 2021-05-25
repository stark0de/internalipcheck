from netaddr import *
import dns.resolver
from colorama import Fore, init
from termcolor import colored
import sys

init()

if len(sys.argv) != 2:
    print(Fore.WHITE+"Usage: python3 checkifresolvetoiternalip.py listwithdomains")
    sys.exit()

urls=open(sys.argv[1],"r").readlines()
#print(urls)
counter=0
resolver = dns.resolver.Resolver()
for j in urls:
    #print(j.strip)
    try:
       answers = resolver.query(j.strip(), 'A',lifetime=15)
       for i in answers:
           #print(i,type(i))
           test = IPAddress(str(i).strip()).is_private()
           if test == True:
               print(Fore.GREEN+"[+] Domain "+j.strip()+" resolves to the internal IP: "+str(i))
               counter+=1
           else:
               pass
    except Exception as e:
       print(e)
#print(counter)
if counter == 0:
    print(Fore.RED+"[-] No positive results")
