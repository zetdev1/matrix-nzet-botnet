from matrix_client.client import MatrixClient
from rich.console import Console
import os

console = Console()

client = MatrixClient("https://matrix.org")

usfile = input("Users file: ")

accs = open(usfile, "r")

accs = accs.readlines()


# Next

chat = input("Chat: ")
video = input("Video: ")
vidname = input("Video Name: ")


auth = accs[0]
auth = auth.strip().split(":")
client.login(username=auth[0], password=auth[1])
room = client.join_room(chat)

with open(video, 'rb') as datafile:
	data = datafile.read()
	uri = client.upload(content=data, content_type='video/mp4')
	print(uri)

while True:
	for x in range(len(accs)):
		try:
			auth = accs[x]
			auth = auth.strip().split(":")
			client.login(username=auth[0], password=auth[1])
			room.send_video(uri, vidname)
			console.print("[bold green] {x} [/] Send video to {chat}!")
		except Exception as e:
			print(e)
