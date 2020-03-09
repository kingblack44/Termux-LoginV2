from getpass import getpass
import os
import time

logo = """
\033[1;36m ██▓     ▒█████    ▄████  ██▓ ███▄    █    ▓█████▄  █    ██  ██▓     █    ██
\033[1;36m▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██▒ ██ ▀█   █    ▒██▀ ██▌ ██  ▓██▒▓██▒     ██  ▓██▒
\033[1;34m▒██░    ▒██░  ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒   ░██   █▌▓██  ▒██░▒██░    ▓██  ▒██░
\033[1;34m▒██░    ▒██   ██░░▓█  ██▓░██░▓██▒  ▐▌██▒   ░▓█▄   ▌▓▓█  ░██░▒██░    ▓▓█  ░██░
\033[1;92m░██████▒░ ████▓▒░░▒▓███▀▒░██░▒██░   ▓██░   ░▒████▓ ▒▒█████▓ ░██████▒▒▒█████▓▓
\033[1;97m●●●●●●●●●●●●●●●●●●●●\033[1;92m<><>\033[1;97m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
\033[1;97m	           Pembuat Tools\033[1;97m: \033[1;92mARIEL SANDY PERMANA
\033[1;97m	           Youtube\033[1;97m: \033[1;92mAriel 69 Channel
\033[1;97m	           Git Hub\033[1;97m: \033[1;92mhttps://github.com/Kingblack44
\033[1;97m●●●●●●●●●●●●●●●●●●●●\033[1;92m<><>\033[1;97m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●"""

logo2 = """
\033[1;36m▄▄▄█████▓   ▓█████     ██▀███      ███▄ ▄███▓    █    ██    ▒██   ██▒
\033[1;36m▓  ██▒ ▓▒   ▓█   ▀    ▓██ ▒ ██▒   ▓██▒▀█▀ ██▒    ██  ▓██▒   ▒▒ █ █ ▒░
\033[1;34m▒ ▓██░ ▒░   ▒███      ▓██ ░▄█ ▒   ▓██    ▓██░   ▓██  ▒██░   ░░  █   ░
\033[1;34m░ ▓██▓ ░    ▒▓█  ▄    ▒██▀▀█▄     ▒██    ▒██    ▓▓█  ░██░    ░ █ █ ▒
\033[1;92m  ▒██▒ ░    ░▒████▒   ░██▓ ▒██▒   ▒██▒   ░██▒   ▒▒█████▓    ▒██▒ ▒██▒
\033[1;97m●●●●●●●●●●●●●●●●●●●●\033[1;92m<><>\033[1;97m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
\033[1;97m	           Termux Login By\033[1;97m: \033[1;92mARIEL SANDY PERMANA
\033[1;97m	           Youtube\033[1;97m: \033[1;92mAriel 69 Channel
\033[1;97m	           Git Hub\033[1;97m: \033[1;92mhttps://github.com/Kingblack44
\033[1;97m●●●●●●●●●●●●●●●●●●●●\033[1;92m<><>\033[1;97m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●"""
def menu():
      while True:
           print("")
           os.system("clear")
           print (logo)
           print('')
           os.system('date | lolcat')
           try:
                x = str(input('\033[1;92mUsername \033[1;93m: '))
                print("")
                e = getpass('\033[1;92mPassword \033[1;93m: ')
                print ("")
                if x=="GANTI NAMA KALIAN" and e=="GANTI PASSWORD NYA":
                   print('Login Sukses Mohon Tunggu Sebentar...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   
                   print(logo2)
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Password/Usr Name Salah")
                      time.sleep(2)
                      print("")
           except Exception:
                      
                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Password/Usr Name Salah")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Password/Usr Name Salah")
                      time.sleep(2)
menu()
