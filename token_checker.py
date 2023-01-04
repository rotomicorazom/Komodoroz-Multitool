import requests, json, fade, discord, os, httpx, timer, time, base64, subprocess, threading
from threading import Thread
from colorama import Fore as F
from pystyle import *
from datetime import datetime
locker = threading.Lock()

cooldown = 5
w=F.LIGHTWHITE_EX
r=F.RED
g=F.GREEN
y=F.LIGHTYELLOW_EX
b=F.LIGHTBLUE_EX
black=F.LIGHTBLACK_EX
m=F.LIGHTMAGENTA_EX
c=F.LIGHTCYAN_EX
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
faded_gui_token_checker=fade.pinkred(token_checker_gui)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
clear()
print(faded_gui_token_checker)

def checker(token:str):
    session = requests.Session()
    cookiesheader={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "TE": "trailers"}
    boostsheader={
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "*/*",
        "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": token,
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTguMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk4LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTIxMDE3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        "X-Discord-Locale": "en-US",
        "X-Debug-Options": "bugReporterEnabled",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://discord.com/channels/@me",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers" 
    }
    getcookies = session.get("https://discord.com/channels/@me", headers=cookiesheader)
    boosts = session.get("https://discord.com/api/v9/users/guilds/premium/subscription-slots", headers=boostsheader)
    if boosts.status_code == 200:
        boosts = boosts.json()
        if len(boosts) > 0:
            noCooldown=0
            for boost in boosts:
                if boosts["cooldown_ends_at"] == None or time.time() > datetime.strptime(boosts["cooldown_ends_at"], "%Y-%m-%dT%H:%M:%S.%f%z").timestamp():
                    noCooldown+=1
            if noCooldown >= len(boosts):
                locker.acquire()
                with open("./results/token_checker/UsableBoosts.txt", "a", encoding="utf-8") as f:
                    f.write(token+"\n")
                with open("./data/token_checker/tokens.txt", "r+") as f:
                    t = f.read().splitlines()
                    f.seek(0)
                    for i in t:
                        if i != token:
                            f.write(f"{i}\n")
                    f.truncate()
                    locker.release()
                    print(f"{m}[{w}OK{m}] {g}Boosts Valid {y}{token}")
            else: 
                print(f"{m}[{w}!{m}] {y}{token}{black} - {b}{noCooldown}{black}/{b}{len(boosts)}{black} Boosts Valid")
        else:
            locker.acquire()
            with open("NoBoosts.txt", "a", encoding="utf-8") as f:
                f.write(token+"\n")
            with open("./data/token_checker/tokens.txt", "r+") as f:
                p = f.read().splitlines()
                f.seek(0)
                for i in p:
                    if i != token:
                        f.write(f"{i}\n")
                f.truncate()
            locker.release()
    else:
        z=open('./results/token_checker/InvalidTokens.txt', 'w')
        z.write(token+"\n")
        print(f"{m}[{w}ERROR{m}] {r}{token}  {w}--{m}>{black} Invalid Token")
        
def manager():
    for token in open('./data/token_checker/tokens.txt', 'r').read().splitlines():
        threading.Thread(target=checker, args=(token)).start()
        time.sleep(1)

if __name__ == "__main__":
    try:
        if os.name =="nt":
            os.system("cls")
            print(faded_gui_token_checker)
        else:
            os.system("clear")
            print(faded_gui_token_checker)
        manager()
        os.system("cls")
        os.system("python main.py")
    except KeyboardInterrupt:
        exit()