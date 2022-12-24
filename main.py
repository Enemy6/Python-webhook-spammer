from colorama import Fore, Style, init
import os 

# Initialize colorama
init()

print(f'{Fore.CYAN}\r\n\n                       ▄▀▄     ▄▀▄' + "\n"
      '                      ▄█░░▀▀▀▀▀░░█▄' + "\n"
      '                  ▄▄  █░░░░░░░░░░░█' + "\n"
      '                 █▄▄█ █░░▀░░┬░░▀░░█ █▄▄█' + "\n"
      "\n"
      "                 Author: Kars#9142\n"
      "                 GitHub: https://github.com/ArabicCat\n")
option = input("Please select a option:\n1 Manual\n2 Auto\n> ")

# Check the user's input and run the appropriate script
if option == "1":
    os.system('manual.py')
elif option == "2":
    os.system('auto.py')
else:
    print(Fore.RED + "Invalid option. Please chooce number 1 or 2.")