try:
    from colorama import Fore, Style, init
except ImportError:
    raise RuntimeError(
        "The colorama module must be installed\nYou can install it with 'pip install colorama'"
    )
try:
    import discord_webhook
except ImportError:
    raise RuntimeError(
        "The discord-webhook module must be installed\nYou can install it with 'pip install discord-webhook'"
    )
try:
    import requests
except ImportError:
    raise RuntimeError(
        "The requests module must be installed\nYou can install it with 'pip install requests'"
    )
import os
import sys

init()


def main():
    option = input(f"Please select a option:\n1 Manual\n2 Auto\n> ")

    try:
        if option == "1":
            os.system(f"{sys.executable} ./manual.py")
        elif option == "2":
            os.system(f"{sys.executable} ./auto.py")
        else:
            print(
                f"{Fore.RED}Invalid option. Please choose numer 1 or 2.{Style.RESET_ALL}"
            )
            main()

    except Exception as e:
        print(Fore.RED + "An error occurred:", e)


if __name__ == "__main__":
    print(
        f"{Fore.CYAN}\r\n\n                       ▄▀▄     ▄▀▄" + "\n"
        "                      ▄█░░▀▀▀▀▀░░█▄" + "\n"
        "                  ▄▄  █░░░░░░░░░░░█" + "\n"
        "                 █▄▄█ █░░▀░░┬░░▀░░█ █▄▄█" + "\n"
        "\n"
        "                 Author: Kars#9142\n"
        "                 GitHub: https://github.com/ArabicCat\n"
    )

    main()
