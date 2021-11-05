import discord, asyncio
from discord.ext import commands
from cryptography.fernet import Fernet


client = commands.Bot(command_prefix="c!", description="Maj")
client.remove_command("help")


@client.event
async def on_ready():
    print("Maintenance Mod Ready.")
    while True:
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="➜ Grosse MAJ in comming...", type=3))
        await asyncio.sleep(5)


key = open("key.key", "rb").read()
f = Fernet(key)
with open("token", "rb") as file:
    encrypted_data = file.read()
decrypted_data = f.decrypt(encrypted_data)


client.run(decrypted_data.decode())
