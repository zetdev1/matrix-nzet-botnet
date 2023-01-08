from matrix_client.client import MatrixClient
from rich.console import Console
from threading import Thread
from time import sleep
import random
console = Console()

client = MatrixClient("http://matrix.org")

usfile = input("Users: ")

accs = open(usfile, "r+")

accs = accs.readlines()
phrases = []
phrases_count = int(input("Count of phrases: "))
chat = input("Chat: ")
t = 0
while t < phrases_count:
	message = input("Text: ")
	phrases.append(message)
	t += 1

auth = accs[0]
auth = auth.strip().split(":")
client.login(username=auth[0], password=auth[1])
room = client.join_room(chat)

while True:
	for x in range(len(accs)):
		try:
			auth = accs[x]
			auth = auth.strip().split(":")
			client.login(username=auth[0], password=auth[1])
			resp = room.send_text(random.choice(phrases))
			console.print(f"[{x}] Account [bold green] send text![/] ")
		except Exception as e:
			print(f"Err:\n{e}")
