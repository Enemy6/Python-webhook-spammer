from discord_webhook import DiscordWebhook
from colorama import init, Fore, Style
import requests

print(Fore.BLUE + "ARABIC/JIMBOB'S WEBHOOK SPAMMER!!!!!!!!!  \n")

init(autoreset=True)

def is_valid_webhook(url):
    try:
        requests.post(url, json={'content': 'oh no...'})
        return True
    except requests.exceptions.RequestException:
        return False

while True:
    url = input(Fore.GREEN + "Enter the url you wanna spam \n> ")

    if not is_valid_webhook(url):
        print(Fore.RED + "Error: Invalid webhook URL")
        continue

    msg = input(Fore.GREEN + "\nEnter the message you wanna spam \n> ")
    amount = int(input(Fore.GREEN + "\nEnter the amount you wanna spam the message\n> "))

    webhook = DiscordWebhook(url=(url), rate_limit_retry=True,
                            content=("@everyone" + (msg)))
    count = 1
    while count <= (amount):
        response = webhook.execute()
        print(Fore.YELLOW + f"Send message #{count}")
        count += 1

    print(Fore.GREEN + "ez bitches")
    print(Style.BRIGHT + Fore.GREEN + "\n\nThanks for using my epic programm :)")

    again = input(Fore.BLUE + "Press ENTER to exetute the script again.\n\n")
    if again.lower() != "":
        break