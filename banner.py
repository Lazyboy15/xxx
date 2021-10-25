import os
from time import sleep
W="\033[1;37m" # Whit
G="\033[1;32m" # 
def clear_screen():
    clear = 'clear'
    if os.name in ('nt', 'dos'):
        clear = 'cls'
    os.system(clear)

def banner():
    print(f'''{G}

    ▄      ▄     ▄       ▄  
▀▄   █ ▀▄   █     █  ▀▄   █ 
  █ ▀    █ ▀  ██   █   █ ▀  
 ▄ █    ▄ █   █ █  █  ▄ █   
█   ▀▄ █   ▀▄ █  █ █ █   ▀▄ 
 ▀      ▀     █   ██  ▀

DEV: @ LZBOY17 
     @ DAMAR{W}
''')

os.system("aplay /home/blackjack/Downloads/'Strange _Things.wav'")
clear_screen()
banner()
                    
