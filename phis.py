import requests
import sys
import time
import os

print("""\033[31m
 _______  ___      _______  _______  ___   _______    _______  __   __  ___   _______ 
|       ||   |    |       ||  _    ||   | |       |  |       ||  | |  ||   | |       |
|  _____||   |    |   _   || |_|   ||   | |_     _|  |    _  ||  |_|  ||   | |  _____|
| |_____ |   |    |  | |  ||       ||   |   |   |    |   |_| ||       ||   | | |_____ 
|_____  ||   |___ |  |_|  ||  _   | |   |   |   |    |    ___||       ||   | |_____  |
 _____| ||       ||       || |_|   ||   |   |   |    |   |    |   _   ||   |  _____| |
|_______||_______||_______||_______||___|   |___|    |___|    |__| |__||___| |_______|
""")

print("""\033[33m
1--->Instagram
0--->Exit""")
print("\033[31mMORE is COMING SOON...")


seçim = input("Seçiminiz--->")
def loading_animation():
        symbols = ["-", "|", "/", "\\"]
    
        for i in range(1, 16):
            sys.stdout.write('\r')
            sys.stdout.write('-' * i + symbols[i % len(symbols)])
            sys.stdout.flush()
            time.sleep(0.2)




if(seçim == "0"):
    print("\033[34mExited")
if(seçim == "1"):
    sayfaismi = input("Sayfa İsmi--->")
    mail = input("Mail Adresiniz--->")
    print("\033[32m|")
    loading_animation()
    os.system("clear")
    

    api_url = "http://smmslowy-001-site1.atempurl.com/api/yenisayfa.php"
    params = {"sayfaismi": sayfaismi, "mail": mail}

    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        print("""\033[31m
        _______  ___      _______  _______  ___   _______    _______  __   __  ___   _______ 
        |       ||   |    |       ||  _    ||   | |       |  |       ||  | |  ||   | |       |
        |  _____||   |    |   _   || |_|   ||   | |_     _|  |    _  ||  |_|  ||   | |  _____|
        | |_____ |   |    |  | |  ||       ||   |   |   |    |   |_| ||       ||   | | |_____ 
        |_____  ||   |___ |  |_|  ||  _   | |   |   |   |    |    ___||       ||   | |_____  |
         _____| ||       ||       || |_|   ||   |   |   |    |   |    |   _   ||   |  _____| |
        |_______||_______||_______||_______||___|   |___|    |___|    |__| |__||___| |_______|
        """)
        print(f"\033[31m\nUrl:  http://smmslowy-001-site1.atempurl.com/login/sayfaismi.php")
    else:
        print(f"Hata! HTTP durumu: {response.status_code}")
        print("API yanıtı:", response.text)
else:
    print("Geçersiz seçim. Lütfen 1'i seçin.")