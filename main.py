from discord_webhook import DiscordWebhook
import requests
import os
import time

def is_valid_webhook(url):
    try:
        requests.post(url, json={'content': '@everyone discord.gg/DM8GtTT4rX'})
        return True
    except requests.exceptions.RequestException:
        return False

while True:
    print('\r\n\n                       ▄▀▄     ▄▀▄' + "\n"
      '                      ▄█░░▀▀▀▀▀░░█▄' + "\n"
      '                  ▄▄  █░░░░░░░░░░░█' + "\n"
      '                 █▄▄█ █░░▀░░┬░░▀░░█ █▄▄█' + "\n"
      "\n"
      "                 Author: Kars#9142\n"
      "                 GitHub: https://github.com/ArabicCat\n\n")
    url = input("Enter the url you wanna spam (leave empty for default) \n> ")

    if not is_valid_webhook(url):
        print("Error: Invalid webhook URL")
        continue

    msg = input("\nEnter the message you wanna spam (leave empty for default)\n> ")
    amount = int(input("\nEnter the amount you wanna spam the message (25+ = RATELIMMITED)\n> "))

    # If the user doesn't provide a message, use the default message
    if not msg:
        msg = "@everyone hey babe, i 32 year old girl from canada look for sex. click my link and enter email for hot video: https://discord.gg/DM8GtTT4rX"

    webhook = DiscordWebhook(url=(url), rate_limit_retry=True,
                            content=((msg)))
    count = 1
    while count <= (amount):
        response = webhook.execute()
        print(f"Send message #{count}")
        count += 1
        time.sleep(0.1)

    # Log the number of messages sent to the webhook
    with open("logs.txt", "a") as log_file:
        log_file.write(f"{amount} Messages sent to: {url}\n")

    again = input("\nPress ENTER to exetute the script again.")
    if again.lower() != "":
        break 
    os.system('cls' if os.name == 'nt' else 'clear')