import os
import notify2
import discord
from discord.ext import commands
import datetime


simpyver="Beta 3.1.0"

os.chdir("/mnt/DATI/Documenti/Carlo/Simpy")

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "$", intents=intents)

@client.group(help="Cambia lo status di Simpy")
async def status(ctx):
    pass
@status.command(invoke_without_command=True)
async def idle(ctx):
    await client.change_presence(status=discord.Status.idle)
@status.command(invoke_without_command=True)
async def online(ctx):
    await client.change_presence(status=discord.Status.online)
@status.command(invoke_without_command=True)
async def offline(ctx):
    await client.change_presence(status=discord.Status.offline)
@status.command(invoke_without_command=True)
async def invisible(ctx):
    await client.change_presence(status=discord.Status.invisible)
@status.command(invoke_without_command=True)
async def game(ctx, arg):
    await client.change_presence(activity=discord.Game(f"{arg}"))
@status.command(invoke_without_command=True)
async def listen(ctx, arg):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{arg}"))

@client.event
async def on_ready():
    print(f"\nSimpy è Online\nLogged in at: {datetime.datetime.now()}\n")
    notify2.init("Simpy-Bot")
    n = notify2.Notification("Simpy-Bot", "Simpy è Online!", "/mnt/DATI/Documenti/Carlo/Simpy/icon.png")
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(10000)
    n.show()

@client.command(help="Carica un'estensione")
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"L'estensione {extension} è stata caricata.")
    print(f"[COGS] L'estensione {extension} è stata caricata da {ctx.author}")

@client.command(help="Ricarica un'estensione")
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"L'estensione {extension} è stata ricaricata.")
    print(f"[COGS] L'estensione {extension} è stata ricaricata da {ctx.author}")

@client.command(help="De-carica un'estensione")
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"L'estensione {extension} è stata de-caricata.")
    print(f"[COGS] L'estensione {extension} è stata de-caricata da {ctx.author}")


for filename in os.listdir('/mnt/DATI/Documenti/Carlo/Simpy/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('')
