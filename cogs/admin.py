import os
import discord
import datetime
from discord.ext import commands
#Directory
os.chdir("/mnt/DATI/Documenti/Carlo/Simpy")

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin Cog is online!")

    @commands.command(help="Elimina gli ultimi messaggi di un canale")
    @commands.has_role("Admin")
    async def purge(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)

    @commands.command(help="Ritorna un messaggio con la latenza di risposta del bot")
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")

    @commands.command(help="Invia un feedback allo sviluppatore di Simpy")
    async def feedback(self, ctx, *args):
        print("È stato inviato un feedback!")
        feedfile = open("Things/Feedback.txt", "a")
        feedfile.write("\n" + str(datetime.datetime.now()) + " - " + str(ctx.author) + " :  ")
        for arg in args:
            feedfile.write(" " + arg)
        feedfile.close
        await ctx.author.send("Grazie mille per il tuo feedback!")

    @commands.command(help="Registra il tuo ID e altre informazioni simili")
    async def trackme(self, ctx):
        print(ctx.author)
        print(ctx.message)
        print(ctx.guild)
        await ctx.send("Grazie mille per aver donato i tuoi dati alla scienza!")

    @commands.command(help="Banna un membro del server")
    @commands.has_role("Admin")
    async def ban(self, ctx, member:discord.Member,*, reason=None):
        await member.ban(reason=reason)

    @commands.command(help="Kickka un membro dal server")
    @commands.has_role("Admin")
    async def kick(self, ctx, member:discord.Member,*, reason=None):
        await member.kick(reason=reason)

    @commands.command(help="Muta un membro del server")
    @commands.has_role("Admin")
    async def mute(self, ctx, member:discord.Member,*, reason=None):
        everyone = message.guild.get_role(753723195718107219)
        bup_roles = message.author.roles
        bup_roles.remove(everyone)
        role = discord.utils.get(message.guild.roles, name="Muted")
        await member.remove_roles(*bup_roles)
        await member.add_roles(role)
        await ctx.send(f"{member} è stat* mutat* per {reason}")

    @commands.command(help="Gestisci la slowmode del canale testuale in cui ti trovi")
    @commands.has_role("Admin")
    @commands.guild_only()
    async def slowmode(self, ctx, sec: int):
        await ctx.channel.edit(slowmode_delay=sec)
        await ctx.send(f"Impostata la slowmode del canale {ctx.channel.name} a {sec} secondi!")

    @commands.command(help="Disconnetti Simpy da Discord")
    @commands.has_role("Admin")
    async def logout(self, ctx):
        if str(ctx.author) == "Zoldie#4848":
            qexit = input("Disconnect from Discord? y/n")
            if qexit == "y":
                await ctx.send("Ci vediamo gente, io vado!")
                await self.client.logout()
                print(f'{client.user} has logout from Discord!')
            elif qexit == "n":
                pass
            else:
                print(qexit)
                print("Invalid Input!")
        else:
            await ctx.send("Non hai permessi sufficienti per utilizzare questo comando!")

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("Devi avere il ruolo 'Admin' per poter utilizzare questo comando!")
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("Devi avere il ruolo 'Admin' per poter utilizzare questo comando!")
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("Devi avere il ruolo 'Admin' per poter utilizzare questo comando!")

def setup(client):
    client.add_cog(Admin(client))
