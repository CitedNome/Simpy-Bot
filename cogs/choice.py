import os
import discord
import random
from discord.ext import commands
#Directory
os.chdir("/mnt/DATI/Documenti/Carlo/Simpy")

class Choice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Choice Cog is online!")

    @commands.command(help="Lancia una moneta", aliases=["coin", "moneta"])
    async def flip(self, ctx, *args):
        testacroce = ['`Testa!`', '`Croce!`']
        await ctx.send(random.choice(testacroce))

    @commands.command(help="Lancia un dado a 6 facce", aliases=["dice"])
    async def dado(self, ctx, max=6):
        n = random.randrange(1, max)
        await ctx.send(str(n))

    @commands.command(help="Fa una scelta tra possibilità multiple", aliases=["scegli", "scelta"])
    async def choose(slef, ctx, *choices:str):
        await ctx.send(random.choice(choices))

    @commands.command(help="Inizia un sondaggio (richiede supporto file)")
    async def survey(self, ctx):
        survey = open("Things/Survey.py", "rt")
        contents = survey.read()
        survey.close
        embed=discord.Embed(
        title="Sondaggio",
        color=discord.Color.blue()
        )
        exec(contents)
        await ctx.send(embed=embed)

    @commands.command(help="Ricevi una risposta alle tue domande", aliases=["8"])
    async def eight_ball(self, ctx, *args):
        risposte=["Ovviamente sì", "Lol no", "Ti piacerebbe", "Sì", "No", "Forse", "Indubbiamente", "Non credo proprio", "Non ne sarei così sicuro", "AHAHAHAHAHAH", "Certo", "Pover* illus*", "Boh"]
        risposta=random.choice(risposte)
        await ctx.send(f"<@{ctx.author.id}>, la risposta alla tua domanda è:\n{risposta}")

def setup(client):
    client.add_cog(Choice(client))
