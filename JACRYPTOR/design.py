from colorama import Fore as color
from time import sleep

bold = '\033[1m'
endbold = '\033[0m'

def main_banner():
    print(color.BLUE+'''
             __o__        o                  o__ __o     o__ __o    \o       o/   o__ __o    ____o__ __o____     o__ __o        o__ __o       
             |         <|>                /v     v\   <|     v\    v\     /v   <|     v\    /   \   /   \     /v     v\      <|     v\      
        / \        / \               />       <\  / \     <\    <\   />    / \     <\        \o/         />       <\     / \     <\     
            \o/      o/   \o           o/             \o/     o/      \o/      \o/     o/         |        o/           \o   \o/     o/     
         |      <|__ __|>         <|               |__  _<|        |        |__  _<|/        < >      <|             |>   |__  _<|      
            < >     /       \          \\              |       \      / \       |                 |        \\           //    |       \     
\        |    o/         \o     o    \         /  <o>       \o    \o/      <o>                o          \         /     <o>       \o   
     o       o   /v           v\   <|>    o       o    |         v\    |        |                <|           o       o       |         v\  
 <\__ __/>  />             <\  < >    <\__ __/>   / \         <\  / \      / \               / \          <\__ __/>      / \ 
    Base64 | Hex | Rot13                                                                                                                   ''')


    print(color.YELLOW+'''
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    | Developer : SOHEILTNT           |
    | Email: soheil.abbasi.v@gmail.com|
    | Instagram : soheil.a.b1         |
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    ''')
    sleep(0.5)


def menu():
    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Base64")
    print(color.CYAN+"--------------------")
    sleep(0.1)
    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Hex")
    print(color.CYAN+"--------------------")
    sleep(0.1)
    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Rot13")
    print(color.CYAN+"--------------------")
    sleep(0.1)
    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Decoder")
    print(color.CYAN+"--------------------")
    sleep(0.1)
    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Exite"+endbold)
def decoder_menu():
    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Base64")
    print(color.CYAN+"--------------------")
    sleep(0.1)
    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Hex")
    print(color.CYAN+"--------------------")
    sleep(0.1)
    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Rot13")
    print(color.CYAN+"--------------------")
    sleep(0.1)
    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Decoder")
    print(color.CYAN+"--------------------")
    sleep(0.1)
    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Back"+endbold)
        


