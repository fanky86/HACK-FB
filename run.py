import os, sys

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
N = '\x1b[0m'    # WARNA MATI

def clear():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")

try:
    import requests
except ImportError:
    clear();print(f"\n [{M}!{N}] Modul {H}requests{N} belum terinstall!...\n")
    os.system("pip install requests")

try:
    import bs4
except ImportError:
    clear();print(f"\n [{M}!{N}] Modul {H}Bs4{N} belum terinstall!...\n")
    os.system("pip install bs4")

try:
    import rich
except ImportError:
    clear();print(f"\n [{M}!{N}] Modul {H}Rich{N} belum terinstall!..\n.")
    os.system("pip install rich")
##############################################################################
try:
    __import__("/data/rud").main()
except Exception as e:
    exit(str(e))

if __name__=='__main__':
    os.system("git pull")
