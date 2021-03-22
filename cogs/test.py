import os
import discord
import random
import json
import asyncio
import datetime
import time
import wikipedia
import youtube_search as ytbs
from discord.ext import commands
#Directory
os.chdir("/mnt/DATI/Documenti/Carlo/Simpy")

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Test Cog is online!")

    @commands.command(help="Effettua una ricerca su Wikipedia")
    async def wiki(self, ctx, search:str, lang="it"):
        wikipedia.set_lang(f"{lang}")
        if search == "Irene" or search == "irene":
            embed=discord.Embed(title="Suorsovrana Irene", description="L'Egregia Suorsovrana Irene è una dei massimi esponenti conosciuti dell'Impero Gordiano. È inoltre l'essere mortale più vicino al sommo Dio Gordy.", color=0xfffffe)
            embed.set_author(name="Wikipedia", icon_url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fpngimg.com%2Fuploads%2Fwikipedia%2Fwikipedia_PNG35.png&f=1&nofb=1")
            embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F7%2F77%2FWikipedia_svg_logo.svg%2F1200px-Wikipedia_svg_logo.svg.png&f=1&nofb=1")
            embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif search == "Asia" or search == "asia":
            embed=discord.Embed(title="Asia", description="La Segretaria Messaggera Asia è la segretaria ufficiale della Suorsovrana Irene... [UD]", color=0xfffffe)
            embed.set_author(name="Wikipedia", icon_url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fpngimg.com%2Fuploads%2Fwikipedia%2Fwikipedia_PNG35.png&f=1&nofb=1")
            embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F7%2F77%2FWikipedia_svg_logo.svg%2F1200px-Wikipedia_svg_logo.svg.png&f=1&nofb=1")
            embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif search == "Carlo" or search == "carlo":
            embed=discord.Embed(title="Carlo", description="Il signor cortese paggio cavalier custode dell'acciaio inox e del legno massiccio... [UD]", color=0xfffffe)
            embed.set_author(name="Wikipedia", icon_url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fpngimg.com%2Fuploads%2Fwikipedia%2Fwikipedia_PNG35.png&f=1&nofb=1")
            embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F7%2F77%2FWikipedia_svg_logo.svg%2F1200px-Wikipedia_svg_logo.svg.png&f=1&nofb=1")
            embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            try:
                ws=wikipedia.page(search)
                embed=discord.Embed(title=ws.title, url=ws.url, description=ws.summary, color=0xfffffe)
                embed.set_author(name="Wikipedia", icon_url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fpngimg.com%2Fuploads%2Fwikipedia%2Fwikipedia_PNG35.png&f=1&nofb=1")
                embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F7%2F77%2FWikipedia_svg_logo.svg%2F1200px-Wikipedia_svg_logo.svg.png&f=1&nofb=1")
                embed.set_image(url=ws.images[0])
                embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
            except wikipedia.exceptions.DisambiguationError as e:
                await ctx.send(f"Sembra che la ricerca \"*{search}*\" si riferisca a più pagine di Wikipedia:\n{e.options}")
            except wikipedia.exceptions.PageError:
                await ctx.send(f"Sembra che non esista una pagina Wikipedia per \"*{search}*\".")
            except discord.errors.HTTPException:
                await ctx.send(f"Sembra che questa pagina abbia troppe informazioni per essere inserita in un embed.\nTi lascio il link per raggiungere la pagina:\n{ws.url}")

    @commands.command(help="Cerca un video su YouTube", aliases=["youtube", "yt"])
    async def youtube_search(self, ctx, *, search):
        results = ytbs.YoutubeSearch(search, max_results=3).to_dict()
        try:
            tit1 = results[0]["title"]
            rurl1 = results[0]["url_suffix"]
            url1 = "https://www.youtube.com" + rurl1
            img1 = results[0]["thumbnails"][0]
            view1 = results[0]["views"]
            cha1 = results[0]["channel"]
            dur1 = results[0]["duration"]#>>
            tit2 = results[1]["title"]
            rurl2 = results[1]["url_suffix"]
            url2 = "https://www.youtube.com" + rurl2
            img2 = results[1]["thumbnails"][0]
            view2 = results[1]["views"]
            cha2 = results[1]["channel"]
            dur2 = results[1]["duration"]#>>
            tit3 = results[2]["title"]
            rurl3 = results[2]["url_suffix"]
            url3 = "https://www.youtube.com" + rurl3
            img3 = results[2]["thumbnails"][0]
            view3 = results[2]["views"]
            cha3 = results[2]["channel"]
            dur3 = results[2]["duration"]#>>

            embed1=discord.Embed(title="[1] " + tit1, description=url1, url=url1, color=0xff0000)
            embed1.set_thumbnail(url=img1)
            embed1.add_field(name="Visualizzazioni:", value=view1.rstrip(" visualizzazioni"), inline=True)
            embed1.add_field(name="Canale:", value=cha1, inline=True)
            embed1.add_field(name="Durata:", value=dur1, inline=True)
            embed2=discord.Embed(title="[2] " + tit2, description=url2, url=url2, color=0xff0000)
            embed2.set_thumbnail(url=img2)
            embed2.add_field(name="Visualizzazioni:", value=view2.rstrip(" visualizzazioni"), inline=True)
            embed2.add_field(name="Canale:", value=cha2, inline=True)
            embed2.add_field(name="Durata:", value=dur2, inline=True)
            embed3=discord.Embed(title="[3] " + tit3, description=url3, url=url3, color=0xff0000)
            embed3.set_thumbnail(url=img3)
            embed3.add_field(name="Visualizzazioni:", value=view3.rstrip(" visualizzazioni"), inline=True)
            embed3.add_field(name="Canale:", value=cha3, inline=True)
            embed3.add_field(name="Durata:", value=dur3, inline=True)

            await ctx.send(embed=embed1)
            await ctx.send(embed=embed2)
            await ctx.send(embed=embed3)
        except:
            await ctx.send("La ricerca richiesta ha portato ad un errore.")

def setup(client):
    client.add_cog(Test(client))
