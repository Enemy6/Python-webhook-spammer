from discord_webhook import DiscordWebhook
from colorama import Fore, Style, init
import requests
import os
import time

def is_valid_webhook(url: str) -> bool:
    try:
        res = requests.post(
            url,
            json={
                "content": "@everyone it seems someone leaked your webhook url!!! https://discord.gg/DM8GtTT4rX"
            },
        )
        return bool(res.status_code == 204)
    except requests.exceptions.RequestException:
        return False

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{Fore.CYAN}\r\n\n                       ▄▀▄     ▄▀▄' + "\n"
      '                      ▄█░░▀▀▀▀▀░░█▄' + "\n"
      '                  ▄▄  █░░░░░░░░░░░█' + "\n"
      '                 █▄▄█ █░░▀░░┬░░▀░░█ █▄▄█' + "\n"
      "\n"
      "                 Author: Kars#9142\n"
      "                 GitHub: https://github.com/ArabicCat\n\n")
    url = input(f"{Fore.GREEN}Enter the url you wanna spam (leave empty for default) \n> ")

    if not is_valid_webhook(url):
        print(f"{Fore.RED}Error: Invalid webhook URL")
        continue

    msg = input("\nEnter the message you wanna spam (leave empty for default)\n> ")
    amount = int(input("\nEnter the amount you wanna spam the message (25+ = RATELIMMITED)\n> "))

    # If the user doesn't provide a message, use the default message
    if not msg:
        msg = "@everyone it seems someone leaked your webhook url!!! https://discord.gg/DM8GtTT4rX"

    webhook = DiscordWebhook(url=(url), rate_limit_retry=True,
                            content=((msg)))
    count = 1
    while count <= (amount):
        response = webhook.execute()
        print(f"{Fore.YELLOW}Send message #{count}")
        count += 1
        time.sleep(0.1)

    again = input(f"{Fore.GREEN}\nPress ENTER to exetute the script again.")
    if again.lower() != "":
        break 
    os.system('cls' if os.name == 'nt' else 'clear')