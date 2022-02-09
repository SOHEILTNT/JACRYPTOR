import os, sys
from colorama import Fore as color
from time import sleep
import design

bold = '\033[1m'
endbold = '\033[0m'

def decoder_menu(user_input):
    if(user_input == 1):
        os.system('clear');design.main_banner.banner()
        print(color.WHITE+"Enter Your Encrypted text in base64")
        user_option = input(color.RED+"\n[☢] "+color.RED+"JA.CRYPTOR"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"base64-decryptor"+color.LIGHTRED_EX+"-->")
        os.system(f'echo {user_option} | base64 -d')
        input('\n press any key +endbold')
    elif (user_input == 2):
            os.system('clear');design.main_banner.banner()
            print(color.WHITE+"Enter your text")
            user_option = input(color.RED+"\n[☢] "+color.RED+"JA.CRYPTOR"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"Hex-decryptor"+color.LIGHTRED_EX+"-->")
            print(bold+color.WHITE+"ENCRYPTED ☟\n")
            os.system(f'echo {user_option} | xxd -p -r')
            input(bold+color.BLUE+"\Press Any Key")
    elif (user_input == 3):
            os.system('clear');design.main_banner.banner()
            print(color.WHITE+"Enter your text")
            user_option = input(color.RED+"\n[☢] "+color.RED+"JA.CRYPTOR"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"Rot13-decryptor"+color.LIGHTRED_EX+"-->")
            print(bold+color.WHITE+"ENCRYPTED ☟\n")
            os.system(f"echo {user_option} | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
            input(bold+color.BLUE+"\Press Any Key")
    elif (user_input == 0):
            pass
    else:
            print('Bad Input')
            sleep(3);sys.exite()