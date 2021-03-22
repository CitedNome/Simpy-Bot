import os
import asyncio
import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.utils import get
from ffmpeg import FFmpeg
import youtube_dl
#Directory
os.chdir("/mnt/DATI/Documenti/Carlo/Simpy")

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Voice Cog is online!")

    @commands.command(help="Connette Simpy ad un canale vocale")
    async def join(self, ctx, chname='Generale'):
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=chname)
        await voiceChannel.connect()

    @commands.command(help="Sposta o connette Simpy al tuo canale vocale")
    async def joinme(self, ctx):
        global voice
        try:
            channel = ctx.author.voice.channel
        except:
            return await ctx.send("Non sei conness* ad un canale vocale!")
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

    @commands.command(help="Disconnette Simpy da un canale vocale")
    async def leave(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("Non sono connesso ad un canale vocale!")

    @commands.command(help="Riproduce l'audio di un video di Youtube")
    async def play(self, ctx, *url:str):
        if url:
            song_there = os.path.isfile("song.mp3")
            try:
                if song_there:
                    os.remove("song.mp3")
            except PermissionError:
                await ctx.send("Aspetta che il brano in riproduzione finisca o usa il comando $stop.")
                return

            voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
            if not voice.is_connected():
                voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Generale')
                await voiceChannel.connect()

            ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': True,
                'outtmpl': "./song.mp3",
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            song_search = " ".join(url)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([f"ytsearch1:{song_search}"])
            voice.play(discord.FFmpegPCMAudio("song.mp3"))
        else:
            await ctx.send("Assicurati di aver inserito il nome della canzone o un url di youtube!")

    @commands.command(help="Soundboard Mista")
    async def mix(self, ctx, arg):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if arg == "seal":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Seal.mp3"))
        elif arg == "spermo":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Spermo.mp3"))
        elif arg == "euforico":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Euforico.mp3"))
        elif arg == "cri":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Cri.mp3"))
        elif arg == "carlo":
            message = await ctx.send("Irene basta hai rotto il *quack*!")
            await message.add_reaction("🦆")

    @commands.command(help="Soundboard Barbero", aliases=["barb", "bar"])
    async def barbero(self, ctx, arg):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if arg == "completo":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Barbero_completo.mp3"))
        elif "bruciar" in arg:
            await ctx.send(":fire: Andiamo a bruciargli la casa! :fire:")
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Barbero.mp3"))
        elif arg == "furore":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Furore.mp3"))
        elif "risparmia" in arg:
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Risparmiati.mp3"))
        elif arg == "buonasera":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Buonasera.mp3"))

    @commands.command(help="Soundboard Hazbin/Helluva", aliases=["hh"])
    async def hazbin(self, ctx, arg):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if arg == "kinky":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Kinky.mp3"))
        elif "suck" in arg:
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Suck.mp3"))
        elif arg == "no":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Al_No.mp3"))
        elif "daddy" in arg:
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Daddy.mp3"))
        elif arg == "drug":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Drug.mp3"))
        elif arg == "god":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/God.mp3"))
        elif arg == "retarded":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Retarded.mp3"))
        elif arg == "jambalaya":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Jambalaya.mp3"))
        elif arg == "lonely":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Lonely.mp3"))
        elif arg == "pervert":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Pervert.mp3"))
        elif arg == "speak":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Speak.mp3"))
        elif arg == "stage":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Stage.mp3"))
        elif arg == "maybe":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Maybe.mp3"))
        elif arg == "smile":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Smile.mp3"))
        elif arg == "fair":
            voice.play(discord.FFmpegPCMAudio("/home/palpix/Documenti/Carlo/Audio/Fair.mp3"))

    @commands.command(help="Ascolta l'ultima versione dell'Inno Gordiano")
    async def inno(self, ctx, path_file:str="Inno"):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            if voice.is_playing():
                voice.stop()
                voice.play(discord.FFmpegPCMAudio(f"/home/palpix/Documenti/Carlo/Audio/Inno/{path_file}.mp3"))
            else:
                voice.play(discord.FFmpegPCMAudio(f"/home/palpix/Documenti/Carlo/Audio/Inno/{path_file}.mp3"))

    @commands.command(help="Mette in pausa l'audio in riproduzione")
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        elif not voice.is_connected():
            await ctx.send("Non sono in un canale vocale al momento!")
        else:
            await ctx.send("Non sto riproducendo audio al momento!")

    @commands.command(help="Riprende la riproduzione di un audio precedentemente messo in pausa")
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        elif not voice.is_connected():
            await ctx.send("Non sono in un canale vocale al momento!")
        else:
            await ctx.send("L'audio non è in pausa!")

    @commands.command(help="Ferma la riproduzione di un brano, eliminandolo dalla coda di riproduzione")
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            voice.stop()
        else:
            await ctx.send("Non sono in un canale vocale al momento!")

    @commands.command(pass_context=True, help="Modifica il volume [Non Funzionante]")
    async def volume(self, ctx, volume:float):
        if ctx.voice_client is None:
            return await ctx.send("Non sono connesso ad un canale vocale")
        ctx.voice_client.source.volume = volume/100
        await ctx.send(f"Volume impostato al {volume}%")

def setup(client):
    client.add_cog(Voice(client))
