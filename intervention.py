import webbrowser, os, time, sys
import colorama
from colorama import init, Fore, Style
import ctypes
init(convert=True)
def logo():
    if os.name == "nt":
        ctypes.windll.kernel32.SetConsoleTitleW('Intervention | Coded by: vx#1234 | github.com/vx-dev')
    os.system('clear')
    os.system('cls')
    print(Fore.CYAN + """
  _____ _   _ _______ ______ _______      ________ _   _ _______ _____ ____  _   _ 
 |_   _| \ | |__   __|  ____|  __ \ \    / /  ____| \ | |__   __|_   _/ __ \| \ | |
   | | |  \| |  | |  | |__  | |__) \ \  / /| |__  |  \| |  | |    | || |  | |  \| |
   | | | . ` |  | |  |  __| |  _  / \ \/ / |  __| | . ` |  | |    | || |  | | . ` |
  _| |_| |\  |  | |  | |____| | \ \  \  /  | |____| |\  |  | |   _| || |__| | |\  |
 |_____|_| \_|  |_|  |______|_|  \_\  \/   |______|_| \_|  |_|  |_____\____/|_| \_|

""")
    print(Fore.BLUE + """                       File Sniping Helper by: vx#1234""")
    print(Style.RESET_ALL)
                                                                                                                                

def menu():
    logo()
    print("""
    [1] Anonfile
    [2] Google Drive
    [3] Mediafire
    [4] Zippyshare
    [5] Pastebin
    """)
    mode = input('Service: ')
    if mode == '1':
        anonfile()
    elif mode == '2':
        drive()
    elif mode == '3':
        mediafire()
    elif mode == '4':
        zippyshare()
    elif mode == '5':
        pastebin()
    else:
        print("Invalid Option!")
        time.sleep(1000)
        menu()

def anonfile():
    logo()
    key = input('Enter your keyword(s): ')
    webbrowser.open('https://google.com/search?q=inurl:anonfile.com+' + key)
    menu()

def drive():
    logo()
    key = input('Enter your keyword(s): ')
    webbrowser.open('https://google.com/search?q=inurl:drive.google.com+' + key)
    menu()

def mediafire():
    logo()
    key = input('Enter your keyword(s): ')
    webbrowser.open('https://google.com/search?q=inurl:mediafire.com+' + key)
    menu()

def zippyshare():
    logo()
    key = input('Enter your keyword(s): ')
    webbrowser.open('https://google.com/search?q=inurl:zippyshare.com+' + key)
    menu()

def pastebin():
    logo()
    key = input('Enter your keyword(s)')
    webbrowser.open('https://google.com/search?q=inurl:pastebin.com+' + key)
    menu()

menu()