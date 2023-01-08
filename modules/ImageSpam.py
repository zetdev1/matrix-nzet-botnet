from matrix_client.client import MatrixClient
from rich.console import Console
import os

console = Console()

client = MatrixClient("https://matrix.org")

usfile = input("Users file: ")

accs = open(usfile, "r")

accs = accs.readlines()

imgs = os.listdir("pics")

# Next

chat = input("Chat: ")


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
			client.send_image("mxc://matrix.org/None", "nzet-botnet.jpg")
			console.print(f"account: {x} |  [bold green] Send photo! [/]")
		except Exception as e:
			console.print(f"account: {x} | [bold red] Send photo error. {e} [/]")
