from matrix_client.client import MatrixClient
from rich.console import Console
from threading import Thread
from time import sleep
import random
console = Console()

client = MatrixClient("http://matrix.org")

usfile = input("Users : ")

accs = open(usfile, "r+")

accs = accs.readlines()

chat = input("Chat: ")
message = input("Text: ")
delay_is = input("y/n (Delay?): ")
par = int(input("Strength: "))

if delay_is == "y":
	delay = float(input("Delay (Optimal 2): "))

def spammer():
	while True:
		xt = random.randint(0, len(accs)-1)
		auth = accs[xt]
		auth = auth.strip().split(":")
		token = client.login(username=auth[0], password=auth[1])
		room = client.join_room(chat)
		for x in range(len(accs)):
			try:
				resp = room.send_text(message)
				console.print(f"[{x}] Account [bold green] send text![/] ")
			except Exception as e:
				print(f"Err:\n{e}")

def spammerd():
	while True:
		xt = random.randint(0, len(accs)-1)
		auth = accs[xt]
		auth = auth.strip().split(":")
		token = client.login(username=auth[0], password=auth[1])
		room = client.join_room(chat)
		for x in range(len(accs)):
			try:
				resp = room.send_text(message)
				console.print(f"[{x}] Account [bold green] send text![/] ")
			except Exception as e:
				print(f"Err:\n{e}")
		sleep(delay)


if delay_is == "n":
	tgpool = [
		Thread(target=spammer) for _ in range(par)
	]
	for thr in tgpool:
		thr.start()
else:
	tgpool = [
		Thread(target=spammerd) for _ in range(par)
	]
	for thr in tgpool:
		thr.start()
