#!/usr/bin/env python3
#*code:UTF-8*

import os
from time import sleep
from cl import *
def clear_screen():
    clear = 'clear'
    if os.name in ('nt', 'dos'):
        clear = 'cls'
    os.system(clear)

def banner():
    print(f'''
        
          {Bl} V 1.0 {G}   
     __    __  __    __  __    __ 
    /  |  /  |/  |  /  |/  |  /  |
    $$ |  $$ |$$ |  $$ |$$ |  $$ |
    $$  \/$$/ $$  \/$$/ $$  \/$$/ 
     $$  $$<   $$  $$<   $$  $$<  
      $$$$  \   $$$$  \   $$$$  \  
     $$ /$$  | $$ /$$  | $$ /$$  |
    $$ |  $$ |$$ |  $$ |$$ |  $$ |
    $$/   $$/ $$/   $$/ $$/   $$/ 
                    
                 {Y}
DEV: {Bf}
                 {R}
Mahmod Khamal   Ahmed Khalid{Y}

GitHUB:{R}
 
https://github.com/Lzboy17/              
                              
{W}''')
clear_screen()
sleep(2)
print(f"[{ok}] XXX loading... ")
sleep(4)
clear_screen()
sleep(1)
banner()
                    
