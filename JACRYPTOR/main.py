'''
creator : SOHEILTNT
Email : soheil.abbasi.v@gmail.com
Instagram : soheil.a.b1


Version : 1.0.0 , 2022
Date : 2022.2.9

         __o__        o                  o__ __o     o__ __o    \o       o/   o__ __o    ____o__ __o____     o__ __o        o__ __o       
             |         <|>                /v     v\   <|     v\    v\     /v   <|     v\    /   \   /   \     /v     v\      <|     v\      
        / \        / \               />       <\  / \     <\    <\   />    / \     <\        \o/         />       <\     / \     <\     
            \o/      o/   \o           o/             \o/     o/      \o/      \o/     o/         |        o/           \o   \o/     o/     
         |      <|__ __|>         <|               |__  _<|        |        |__  _<|/        < >      <|             |>   |__  _<|      
            < >     /       \          \\              |       \      / \       |                 |        \\           //    |       \     
\        |    o/         \o     o    \         /  <o>       \o    \o/      <o>                o          \         /     <o>       \o   
     o       o   /v           v\   <|>    o       o    |         v\    |        |                <|           o       o       |         v\  
 <\__ __/>  />             <\  < >    <\__ __/>   / \         <\  / \      / \               / \          <\__ __/>      / \ .
 '''

from inspect import EndOfBlock
import os, sys, design
from colorama import Fore as color
from time import sleep
import decoder

bold = '\033[1m'
endbold = '\033[0m'

########################################

try:
    from colorama import Fore as color 
except:
    print("Install The colorama library")

#########################################


while True:
    
    try:
        os.system('clear');design.main_banner();design.menu() 
        option =int(input(color.RED+"\n[☢] "+color.RED+"JA.CRYPTOR"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+"-->"))

    #CHECK FOR OPTION   
        if (option == 1):
            os.system('clear');design.main_banner.banner()
            print(color.WHITE+"Enter your text")
            user_option = input(color.RED+"\n[☢] "+color.RED+"JA.CRYPTOR"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"base64"+color.LIGHTRED_EX+"-->")
            print(bold+color.WHITE+"ENCRYPTED ☟\n")
            os.system(f'echo {user_option} | base64')
            input(bold+color.BLUE+"\Press Any Key")
            continue
        elif (option == 2):
            os.system('clear');design.main_banner.banner()
            print(color.WHITE+"Enter your text")
            user_option = input(color.RED+"\n[☢] "+color.RED+"JA.CRYPTOR"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"Hex"+color.LIGHTRED_EX+"-->")
            print(bold+color.WHITE+"ENCRYPTED ☟\n")
            os.system(f'echo {user_option} | xxd -p')
            input(bold+color.BLUE+"\Press Any Key")
            continue
        elif (option == 3):
            os.system('clear');design.main_banner.banner()
            print(color.WHITE+"Enter your text")
            user_option = input(color.RED+"\n[☢] "+color.RED+"JA.CRYPTOR"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"Rot13"+color.LIGHTRED_EX+"-->")
            print(bold+color.WHITE+"ENCRYPTED ☟\n")
            os.system(f"echo {user_option} | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
            input(bold+color.BLUE+"\Press Any Key")
            continue
        elif(option == 4):
            os.system('clear');design.main_banner();design.main_banner.decoder_menu
            option =int(input(color.RED+"\n[☢] "+color.RED+"JA.CRYPTOR"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"Decoder"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+"-->"))
            decoder.decoder_menu(option)
            continue
        elif (option == 0):
            print("THANKS FOR USING JACRYPTOR");sleep(0.2)
            sys.exite
        else:
            print('Invalid Input')
            sleep(3);sys.exite()
    except:
        sys.exite()
