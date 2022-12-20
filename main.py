from discord_webhook import DiscordWebhook
from colorama import init, Fore, Style
init(autoreset=True)
url =input(Fore.GREEN + "Enter the url you wanna spam \n> ")
msg = input(Fore.GREEN + "\nEnter the message you wanna spam (leave empty for default) \n> ")

webhook = DiscordWebhook(url=(url), rate_limit_retry=True,
                         content=(msg))

response = webhook.execute()#1
print(Fore.YELLOW + "\nSend message #1")
response = webhook.execute()#2
print(Fore.YELLOW + "Send message #2")
response = webhook.execute()#3
print(Fore.YELLOW + "Send message #3")
response = webhook.execute()#4
print(Fore.YELLOW + "Send message #4")
response = webhook.execute()#5
print(Fore.YELLOW + "Send message #5")
response = webhook.execute()#6
print(Fore.YELLOW + "Send message #6")
response = webhook.execute()#7
print(Fore.YELLOW + "Send message #7")
response = webhook.execute()#8
print(Fore.YELLOW + "Send message #8")
response = webhook.execute()#9
print(Fore.YELLOW + "Send message #9")
response = webhook.execute()#10
print(Fore.YELLOW + "Send message #10")
response = webhook.execute()#11
print(Fore.YELLOW + "Send message #11")
response = webhook.execute()#12
print(Fore.YELLOW + "Send message #12")
response = webhook.execute()#13
print(Fore.YELLOW + "Send message #13")
response = webhook.execute()#14
print(Fore.YELLOW + "Send message #14")
response = webhook.execute()#15
print(Fore.YELLOW + "Send message #15")
response = webhook.execute()#16
print(Fore.YELLOW + "Send message #16")
response = webhook.execute()#17
print(Fore.YELLOW + "Send message #17")
response = webhook.execute()#18
print(Fore.YELLOW + "Send message #18")
response = webhook.execute()#19
print(Fore.YELLOW + "Send message #19")
response = webhook.execute()#20
print(Fore.YELLOW + "Send message #20")

input(Style.BRIGHT + Fore.GREEN + "\n\nThanks for using my epic programm :)")