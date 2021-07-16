import webbrowser, os, time, sys
import colorama
from colorama import init, Fore, Style
import ctypes
def logo():
    if os.name == "nt":
        ctypes.windll.kernel32.SetConsoleTitleW('Intervention | Coded by: vx#1234 | github.com/vx-dev')
        os.system('cls')    
    os.system('clear')
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
    anon = 'anonfile.com+'
    driv = 'drive.google.com+'
    medi = 'mediafire.com+'
    zipp = 'zippyshare.com+'
    past = 'pastebin.com+'
    inurl = 'inurl:'
    site = 'site:'
    o = '+OR+'
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
        logo()        
        key = input('Enter your keyword: ')
        webbrowser.open('https://google.com/search?q='+inurl+anon+key+o+site+anon+key)
        menu()
    elif mode == '2':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://google.com/search?q='+inurl+driv+key)
        menu()
    elif mode == '3':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://google.com/search?q='+inurl+medi+key)
        menu()
    elif mode == '4':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://google.com/search?q='+inurl+zipp+key)
        menu()

    elif mode == '5':
        logo()
        key = input('Enter your keyword')
        webbrowser.open('https://google.com/search?q='+inurl+past+key)
        menu()
    else:
        print("Invalid Option!")
        time.sleep(1000)
        menu()
menu()
