import os
import discord
import random
import json
import asyncio
import datetime
import time
from discord.ext import commands
#Directory
os.chdir("/mnt/DATI/Documenti/Carlo/Simpy")

class Cromo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cromo Cog is online!")

    async def open_cromo(self, user):
        chromo = self.client.get_cog("Cromo")
        users = await chromo.get_cromo_data()
        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 0

        with open("Things/Cromosomi.json", "w") as f:
            users = json.dump(users,f)
            return True

    async def get_cromo_data(self):
        with open("Things/Cromosomi.json", "r") as f:
            users = json.load(f)
        return users

    @commands.command(help="Aggiungi dei cromosomi alla persona taggata", aliases=["+", "add"])
    async def addc(self, ctx, tag:discord.Member, acromo=1):
        chromo = self.client.get_cog("Cromo")
        await chromo.open_cromo(tag)
        users = await chromo.get_cromo_data()
        if acromo == 0:
            user = ctx.author
            earnings = acromo
            await ctx.send(f"Hey hey {ctx.author.mention}, credi di essere spiritoso/a? Ti meriti un cromosoma extra per questo!")
            users[str(user.id)]["wallet"] += 1
            with open("Things/Cromosomi.json", "w") as f:
                json.dump(users,f)
        elif acromo < 0:
            if str(ctx.author) == "Zoldie#4848":
                user = tag
                earnings = acromo
                await ctx.send(f"Congratulazioni {tag.mention} hai ottenuto {acromo} cromosomi extra!")
                users[str(user.id)]["wallet"] += earnings
                with open("Things/Cromosomi.json", "w") as f:
                    json.dump(users,f)
            else:
                await ctx.send("Hey cosa credi di fare?")
        else:
            user = tag
            earnings = acromo
            await ctx.send(f"Congratulazioni {tag.mention} hai ottenuto {acromo} cromosomi extra!")
            users[str(user.id)]["wallet"] += earnings
            with open("Things/Cromosomi.json", "w") as f:
                json.dump(users,f)

    @commands.command(help="Controlla quanti cromosomi possiedi")
    async def cromo(self, ctx, target:discord.Member=None):
        chromo = self.client.get_cog("Cromo")
        crim = ["https://www.universityofcalifornia.edu/sites/default/files/x-chromosome-image.jpg",
                "https://www.focus.it/images/2020/07/13/cromosoma-x_w630.jpg",
                "https://www.medimagazine.it/wp-content/uploads/2020/08/538e4300cc7b2fc960de1bcb4df498f5_large_.jpg",
                "https://sciencecue.it/wp-content/uploads/2017/09/cromosoma-X.jpg",
                "https://scitechdaily.com/images/Y-Chromosome.jpg",
                "https://www.sciencealert.com/images/2020-07/processed/chromosome_1024.jpg",
                "https://thumbs.dreamstime.com/b/x-chromosome-green-background-depth-field-effect-scientific-concept-d-illustration-75054870.jpg",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTt77wA1fwyTI-_4BoDibjmZavP3lHyE-xblg&usqp=CAU",
                "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.icr.org%2Fi%2Fwide%2Fy_chromosome_wide.jpg&f=1&nofb=1"]
        if target is None:
            await chromo.open_cromo(ctx.author)
            user = ctx.author
            users = await chromo.get_cromo_data()
            cromo_amt = users[str(user.id)]["wallet"]
            scrim = random.choice(crim)
            embed = discord.Embed(title = f"Cromosomi di {ctx.author.name}", color = discord.Color.blue())
            embed.set_thumbnail(url=scrim)
            embed.add_field(name="Cromosomi Reali", value = "46")
            embed.add_field(name="Cromosomi Virtuali", value = cromo_amt)
            embed.add_field(name="Cromosomi Totali", value=cromo_amt + 46, inline=False)
            await ctx.send(embed=embed)
        else:
            await chromo.open_cromo(target)
            user = target
            users = await chromo.get_cromo_data()
            cromo_amt = users[str(user.id)]["wallet"]
            scrim = random.choice(crim)
            embed = discord.Embed(title = f"Cromosomi di {user.name}", color = discord.Color.blue())
            embed.set_thumbnail(url=scrim)
            embed.add_field(name="Cromosomi Reali", value = "46")
            embed.add_field(name="Cromosomi Virtuali", value = cromo_amt)
            embed.add_field(name="Cromosomi Totali", value=cromo_amt + 46, inline=False)
            await ctx.send(embed=embed)

    @commands.command(help="Inizia un giveaway di cromosomi")
    @commands.has_role("Admin")
    async def giveaway(self, ctx, prize:int, * , mins:int):
        chromo = self.client.get_cog("Cromo")
        embed = discord.Embed(title="Giveaway!", description=f"{prize} cromosomi!", color=ctx.author.color)
        embed.add_field(name="Regole", value="Reagisci con 🎉 per partecipare all'estrazione!", inline=False)
        embed.set_footer(text = f"Finisce tra {mins} minuti!")
        my_msg = await ctx.send(embed=embed)
        await my_msg.add_reaction("🎉")
        await asyncio.sleep(mins*60)
        new_msg = await ctx.channel.fetch_message(my_msg.id)
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        winner = random.choice(users)
        await ctx.send(f"Complimenti {winner.mention}, hai vinto il Giveaway!\n{prize} cromosomi sono stati aggiunti alla tua collezione!")
        #Add cromo
        await chromo.open_cromo(winner)
        users = await chromo.get_cromo_data()
        user = winner
        earnings = prize
        users[str(user.id)]["wallet"] += earnings
        with open("Things/Cromosomi.json", "w") as f:
            json.dump(users,f)

    @commands.command(help="Mostra la leaderboard", aliases=["classifica"])
    async def leaderboard(self, ctx, x=3):
        chromo = self.client.get_cog("Cromo")
        users = await chromo.get_cromo_data()
        leader_board = {}
        total = []
        for user in users:
            name = int(user)
            total_amount = users[user]["wallet"]
            leader_board[total_amount] = name
            total.append(total_amount)
        total = sorted(total, reverse=True)
        file = discord.File("file_location/medal.png", filename="medal.png")
        em = discord.Embed(title=f"Top {x} Utenti con più Cromosomi", description="*Basato sui Cromosomi Virtuali*", color=discord.Color.gold())
        em.set_thumbnail(url="attachment://file.png")
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            name = await self.client.fetch_user(id_)
            em.add_field(name = f"{index}. {name}", value = f"<==**{amt}**==>", inline=False)
            if index == x:
                break
            else:
                index += 1

        await ctx.send(file=file, embed=em)

    @commands.command(help="Tenta di vincere alla Slot Machine!")
    async def slot(self, ctx):
        chromo = self.client.get_cog("Cromo")
        await chromo.open_cromo(ctx.author)
        users = await chromo.get_cromo_data()
        emojis = "🍎🍊🍋🍉🥑🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.mention}**"
        if (a == b == c == "🥑"):
            await ctx.send(f"{slotmachine} Triplo Avocado! Hai vinto 15 cromosomi!")
            user = ctx.author
            users[str(user.id)]["wallet"] += 14
            with open("Things/Cromosomi.json", "w") as f:
                json.dump(users,f)
        elif (a == b == c != "🥑"):
            await ctx.send(f"{slotmachine} Triplo! Hai vinto 10 cromosomi!")
            user = ctx.author
            users[str(user.id)]["wallet"] += 9
            with open("Things/Cromosomi.json", "w") as f:
                json.dump(users,f)
        elif (a == b != "🥑") or (a == c != "🥑") or (b == c != "🥑"):
            await ctx.send(f"{slotmachine} Doppio! Hai vinto 3 cromosomi!")
            user = ctx.author
            users[str(user.id)]["wallet"] += 2
            with open("Things/Cromosomi.json", "w") as f:
                json.dump(users,f)
        elif (a == b == "🥑") or (a == c == "🥑") or (b == c == "🥑"):
            await ctx.send(f"{slotmachine} Doppio Avocado, hai vinto 5 cromosomi!")
            user = ctx.author
            users[str(user.id)]["wallet"] += 4
            with open("Things/Cromosomi.json", "w") as f:
                json.dump(users,f)
        else:
            await ctx.send(f"{slotmachine} Niente da fare!")
            user = ctx.author
            users[str(user.id)]["wallet"] -= 1
            with open("Things/Cromosomi.json", "w") as f:
                json.dump(users,f)

    @commands.command(help="Scommetti al gioco dei dadi!")
    async def dicebet(self, ctx, bet):
        chromo = self.client.get_cog("Cromo")
        await chromo.open_cromo(ctx.author)
        users = await chromo.get_cromo_data()
        emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        if bet in emojis:
            await ctx.send(f"**[ {a} {b} {c} ]**")
            if (bet == a == b == c):
                user = ctx.author
                users[str(user.id)]["wallet"] += 9
                with open("Things/Cromosomi.json", "w") as f:
                    json.dump(users,f)
                await ctx.send(f"Complimenti {ctx.author}! Hai vinto 10 cromosomi!")
            elif (bet == a == b) or (bet == b == c) or (bet == a == c):
                user = ctx.author
                users[str(user.id)]["wallet"] += 4
                with open("Things/Cromosomi.json", "w") as f:
                    json.dump(users,f)
                await ctx.send(f"Complimenti {ctx.author}! Hai vinto 5 cromosomi!")
            elif (bet == a) or (bet == b) or (bet == c):
                user = ctx.author
                users[str(user.id)]["wallet"] += 1
                with open("Things/Cromosomi.json", "w") as f:
                    json.dump(users,f)
                await ctx.send(f"Complimenti {ctx.author}! Hai vinto 3 cromosomi!")
            else:
                user = ctx.author
                users[str(user.id)]["wallet"] -= 1
                with open("Things/Cromosomi.json", "w") as f:
                    json.dump(users,f)
                await ctx.send("Rippete, niente da fare!")
        else:
            await ctx.send("Scommetti su una delle seguenti emoji: 1️⃣, 2️⃣, 3️⃣, 4️⃣, 5️⃣, 6️⃣.")

    @giveaway.error
    async def giveaway_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("Devi avere il ruolo 'Admin' per poter utilizzare questo comando!")

def setup(client):
    client.add_cog(Cromo(client))
