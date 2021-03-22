import os
import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl

os.chdir("/mnt/DATI/Documenti/Carlo/Simpy")

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Voice Cog is online!")

    @commands.command()
    async def join(self, ctx):
        global voice
        channel = ctx.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            print(f"Simpy si è connesso al canale vocale \"{channel}\"\n")
        await ctx.send(f"Mi sono connesso al canale vocale \"{channel}\"")

    @commands.command()
    async def leave(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.disconnect()
            print(f"Simpy si è disconnesso dal canale vocale\n")
            await ctx.send(f"Mi sono disconnesso dal canale vocale")
        else:
            await ctx.send("Non sono connesso ad un canale vocale!")

    @commands.command()
    async def play(self, ctx, url: str):
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
                print("Rimosso il file song.mp3")
        except PermissionError:
            print("Impossibile eliminare il file song.mp3 perché è in utilizzo")
            await ctx.send("Non è stato possibile cambiare il file")
            return
        await ctx.send("Preparando il file da riprodurre...")
        voice = get(self.client.voice_clients, guild=ctx.guild)
        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading Audio Now")
            ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"Renamed File {file}\n")
                os.rename(file, "song.mp3")

        voice.play(discord.FFmpecPCMAudio("song.mp3"), after=lambda e: print(f"{name} è stato riprodotto completamente."))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07
        nname = name.rsplit("-", 2)
        await ctx.send(f"Riproducendo: {nname}")
        print("Riproducendo l'audio...\n")

def setup(client):
    client.add_cog(Voice(client))
