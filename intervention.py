import webbrowser, os, time, sys
import colorama
from colorama import init, Fore, Style
import ctypes
def logo():
    if os.name == "nt":
        ctypes.windll.kernel32.SetConsoleTitleW('Intervention | Coded by: Kill All Snitches | github.com/killallsnitches')
        os.system('cls')    
    else:
        os.system('clear')
    print(Fore.CYAN + """
  _____ _   _ _______ ______ _______      ________ _   _ _______ _____ ____  _   _ 
 |_   _| \ | |__   __|  ____|  __ \ \    / /  ____| \ | |__   __|_   _/ __ \| \ | |
   | | |  \| |  | |  | |__  | |__) \ \  / /| |__  |  \| |  | |    | || |  | |  \| |
   | | | . ` |  | |  |  __| |  _  / \ \/ / |  __| | . ` |  | |    | || |  | | . ` |
  _| |_| |\  |  | |  | |____| | \ \  \  /  | |____| |\  |  | |   _| || |__| | |\  |
 |_____|_| \_|  |_|  |______|_|  \_\  \/   |______|_| \_|  |_|  |_____\____/|_| \_|

""")
    print(Fore.WHITE + "                       File Sniping Helper by:" + Fore.RED + " Kill All Snitches")
    print(Style.RESET_ALL)
                                                                                                                                
def engine():
    logo()
    print("""
    [1] Bing
    [2] Google
    """)
    x = input('Engine: ')
    if x == '1':
        bing()
    elif x == '2':
        google()
    else:
        engine()



def google():
    anon = 'anonfile.com+'
    driv = 'drive.google.com+'
    medi = 'mediafire.com+'
    zipp = 'zippyshare.com+'
    past = 'pastebin.com+'
    site = 'site:'
    logo()
    print("""
    [1] Anonfile
    [2] Google Drive
    [3] Mediafire
    [4] Zippyshare
    [5] Pastebin
    [<] Back
    """)
    mode = input('Service: ')
    if mode == '1':
        logo()        
        key = input('Enter your keyword: ')
        webbrowser.open('https://google.com/search?q='+site+anon+key)
        google()
    elif mode == '2':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://google.com/search?q='+site+driv+key)
        google()
    elif mode == '3':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://google.com/search?q='+site+medi+key)
        google()
    elif mode == '4':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://google.com/search?q='+site+zipp+key)
        google()

    elif mode == '5':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://google.com/search?q='+site+past+key)
        google()
    elif mode == '<':
        engine()
    else:
        google()
    

def bing():
    anon = 'anonfile.com+'
    driv = 'drive.google.com+'
    medi = 'mediafire.com+'
    zipp = 'zippyshare.com+'
    past = 'pastebin.com+'
    site = 'site:'
    logo()
    print("""
    [1] Anonfile
    [2] bing Drive
    [3] Mediafire
    [4] Zippyshare
    [5] Pastebin
    [<] Back
    """)
    mode = input('Service: ')
    if mode == '1':
        logo()        
        key = input('Enter your keyword: ')
        webbrowser.open('https://bing.com/search?q='+site+anon+key)
        bing()
    elif mode == '2':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://bing.com/search?q='+site+driv+key)
        bing()
    elif mode == '3':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://bing.com/search?q='+site+medi+key)
        bing()
    elif mode == '4':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://bing.com/search?q='+site+zipp+key)
        bing()

    elif mode == '5':
        logo()
        key = input('Enter your keyword: ')
        webbrowser.open('https://bing.com/search?q='+site+past+key)
        bing()
    elif mode == '<':
        engine()
    else:
        bing()


engine()
