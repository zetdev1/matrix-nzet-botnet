from rich.console import Console

console = Console()

import os

os.system("clear")

# Main


print("""

╭━╮╭━╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮
┃┃╰╯┃┃╱╭╯╰╮╱╱╱╱╱╱╱╱╱┃┃
┃╭╮╭╮┣━┻╮╭╋━┳╮╭╮╱╱╱╱┃╰━┳━╮
┃┃┃┃┃┃╭╮┃┃┃╭┻╋╋╯╭━━╮┃╭╮┃╭╮╮
┃┃┃┃┃┃╭╮┃╰┫┃╭╋╋╮╰━━╯┃╰╯┃┃┃┃
╰╯╰╯╰┻╯╰┻━┻╯╰╯╰╯╱╱╱╱╰━━┻╯╰╯
""")
print("Developer: ZetDev | Version : 0.1.1")
modules = os.listdir("modules")
mods = 0
for module in modules:
	mods += 1
	name = os.path.basename(f"modules/{module}")
	name = os.path.splitext(name)[0]
	console.print(f"[{mods}] [bold magenta]{name}[/]")

while True:
	option = int(input(">> "))
	if option > mods:
		console.print("[bold red] {Error}[/] You are entered incorrect option.")
	else:
		real = option - 1
		os.system(f"python3 modules/{modules[real]}")
