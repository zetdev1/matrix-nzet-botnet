from matrix_client.client import MatrixClient
from rich.console import Console
console = Console()

client = MatrixClient("http://matrix.org")

usfile = input("Users : ")

accs = open(usfile, "r+")

accs = accs.readlines()

chat = input("Chat: ")
audio = input("Audio path: ")
audname = input("Audio name: ")

auth = accs[0]
auth = auth.strip().split(":")
client.login(username=auth[0], password=auth[1])
room = client.join_room(chat)

with open(audio, 'rb') as datafile:
            data = datafile.read()
            uri = client.upload(content=data, content_type='audio/x-mp3')
            print(uri)

while True:
	for x in range(len(accs)):
		try:
			auth = accs[x]
			auth = auth.strip().split(":")
			client.login(username=auth[0], password=auth[1])
			room.send_audio(uri, audname)
			console.print(f"[bold red] MatrixBotnet [/] Send audio to room from {x} account.")
		except Exception as e:
			print(e)
