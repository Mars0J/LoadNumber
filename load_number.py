
#usr/bin/python3

import os
import phonenumbers
from phonenumbers import geocoder,carrier,timezone
from colorama import init
from termcolor import colored 


def banner():
   os.system("clear")
   init()
   print(colored("""

    
▒█░░░ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀▄ 
▒█░░░ ▒█░░▒█ ▒█▄▄█ ▒█░▒█ 
▒█▄▄█ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▀ 

▒█▄░▒█ ▒█░▒█ ▒█▀▄▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ 
▒█▒█▒█ ▒█░▒█ ▒█▒█▒█ ▒█▀▀▄ ▒█▀▀▀ ▒█▄▄▀ 
▒█░░▀█ ░▀▄▄▀ ▒█░░▒█ ▒█▄▄█ ▒█▄▄▄ ▒█░▒█""","red"))

print(colored("""
Coder By Mars ""","blue"))
print(colored("""
Github : https://github.com/Mars0J
Youtube : https://youtube.com/channel/UCvndkeSdiN7LcQP4gS5pbeA
Discord : https://discord.gg/FbBzYNgewq""","magenta"))


def phone_info():
    while True:
        init()
        print(colored("[1] Çıkış / Exit","green"))
        print(colored("[2] Telefon No. Bilgi Topla / Phone Number in information","green"))
        i = input("⪼__🅻🅞🅐🅓🅽🅤🅜🅑🅔🅡__⪼")
        def operation():
            if (i=="1"):
                exit()
            elif(i=="2"):
                banner()
                number = input(colored("Telefon Numarasını Ülke Kodu İle Birlikte Giriniz - enter your phone number with country code (+90..........): ","green"))
                phone_number = phonenumbers.parse(number, None)
                print("Ülke/Şehir-Country/City: ",geocoder.description_for_number(phone_number, 'tr'))
                print("Saat dilimi-Time zone: ",timezone.time_zones_for_number(phone_number))
                print("Operatör-Operator: ",carrier.name_for_number(phone_number,'tr'))
            else:
                print("Hatalı İşlem-Incorect operation")
        operation()
banner()
phone_info()
