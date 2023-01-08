from matrix_client.client import MatrixClient

client = MatrixClient("https://matrix.org")

user = input("User > ")
passi = input("Password > ")

token = client.login(username=user, password=passi)

with open("token.txt", "w+") as w:
	w.write(token)
	w.close()
	print(f"Token: {token}")
