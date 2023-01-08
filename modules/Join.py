from matrix_client.client import MatrixClient
from matrix_client.api import MatrixHttpApi
from rich.console import Console

client = MatrixClient("http://matrix.org")

usfile = input("Users : ")

accs = open(usfile, "r+")

accs = accs.readlines()

chat = input("Enter chat from matrix: ")
for x in range(len(accs)):
	auth = accs[x]
	auth = auth.strip().split(":")
	token = client.login(username=auth[0], password=auth[1])
	room = client.join_room(chat)
	print(f"[{x}] Account joined! | Room: {room}")
