from colorama import Fore, Style, init
import os 

init()

print(f'{Fore.CYAN}\r\n\n                       ▄▀▄     ▄▀▄' + "\n"
      '                      ▄█░░▀▀▀▀▀░░█▄' + "\n"
      '                  ▄▄  █░░░░░░░░░░░█' + "\n"
      '                 █▄▄█ █░░▀░░┬░░▀░░█ █▄▄█' + "\n"
      "\n"
      "                 Author: Kars#9142\n"
      "                 GitHub: https://github.com/ArabicCat\n")
option = input("Please select a option:\n1 Manual\n2 Auto\n> ")

try:
    if option == "1":
        os.system('python ./manual.py')
    elif option == "2":
        os.system('python ./auto.py')
    else:
        print(Fore.RED + "Invalid option. Please choose numer 1 or 2.")
except Exception as e:
    print(Fore.RED + "An error occurred:", e)