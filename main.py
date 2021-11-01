import colorama
from discord.ext import commands
from colorama import Fore as C

token = ""

message = "Insert Message Here"

client = discord.Client(command_prefix="lol",self_bot = True)

@client.event
async def on_connect():
    try:
        for a in client.private_channels:
            await a.send(message)
            print(f"{C.BLUE}> Sent to:{C.RESET} {a}")
    except:
        pass

client.run(token, bot = False)
