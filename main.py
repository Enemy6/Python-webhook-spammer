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
    url = input(Fore.GREEN + "Enter the url you wanna spam (leave empty for default) \n> ")

    if not is_valid_webhook(url):
        print(Fore.RED + "Error: Invalid webhook URL")
        continue

    msg = input(Fore.GREEN + "\nEnter the message you wanna spam (leave empty for default)\n> ")
    amount = int(input(Fore.GREEN + "\nEnter the amount you wanna spam the message (25+ = RATELIMMITED)\n> "))

    # If the user doesn't provide a message, use the default message
    if not msg:
        msg = "@everyone hey babe, i 32 year old girl from canada look for sex. click my link and enter email for hot video: https://discord.gg/DM8GtTT4rX"

    webhook = DiscordWebhook(url=(url), rate_limit_retry=True,
                            content=((msg)))
    count = 1
    while count <= (amount):
        response = webhook.execute()
        print(Fore.YELLOW + f"Send message #{count}")
        count += 1

    # Log the number of messages sent to the webhook
    with open("logs.txt", "a") as log_file:
        log_file.write(f"{amount} Messages sent to: {url}\n" + "\n")

    again = input(Style.BRIGHT + Fore.GREEN + "\nPress ENTER to exetute the script again.\n\n")
    if again.lower() != "":
        break 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")