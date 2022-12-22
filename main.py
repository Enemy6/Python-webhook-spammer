from discord_webhook import DiscordWebhook
from colorama import init, Fore, Style
import requests

init(autoreset=True)

def is_valid_webhook(url):
    try:
        requests.post(url, json={'content': 'oh no...'})
        return True
    except requests.exceptions.RequestException:
        return False

while True:
    print('\n\n                       ▄▀▄     ▄▀▄' + "\n"
      '                      ▄█░░▀▀▀▀▀░░█▄' + "\n"
      '                  ▄▄  █░░░░░░░░░░░█' + "\n"
      '                 █▄▄█ █░░▀░░┬░░▀░░█ █▄▄█' + "\n"
      "\n"
      "                 Author: Kars#9142\n"
      "                 GitHub: https://github.com/ArabicCat\n\n")
    url = input(Fore.GREEN + "Enter the url you wanna spam \n> ")

    if not is_valid_webhook(url):
        print(Fore.RED + "Error: Invalid webhook URL")
        continue

    # Save the URL to the log file
    with open("logs.txt", "a") as log_file:
        log_file.write(url + "\n" + "\n")

    msg = input(Fore.GREEN + "\nEnter the message you wanna spam \n> ")
    amount = int(input(Fore.GREEN + "\nEnter the amount you wanna spam the message\n> "))

    webhook = DiscordWebhook(url=(url), rate_limit_retry=True,
                            content=("@everyone " + (msg)))
    count = 1
    while count <= (amount):
        response = webhook.execute()
        print(Fore.YELLOW + f"Send message #{count}")
        count += 1

    again = input(Style.BRIGHT + Fore.GREEN + "\nPress ENTER to exetute the script again.\n\n")
    if again.lower() != "":
        break 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")