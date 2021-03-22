import os
import time
import notify2
import asyncio
import discord
from discord.ext import commands
from discord.utils import get
#Directory
os.chdir("/mnt/DATI/Documenti/Carlo/Simpy")
#SETTINGS
tmt = 30 #Secondi di Temp-Mute
#Cointainers
mute_words = ["eren è figo", "eren è meglio", "gordy fa schifo", "levi fa schifo"]
ciao_words = ["ciao", "helo", "hello", "salve", "salvia", "halo", "tao", "taoo"]
hate_words = ["simpy fai schifo", "simpy ti odio", "fai schifo simpy", "ti odio simpy", "simpy sei brutto", "simpy puzzi", "simpy puzza"]
call_words = ["simpy?", "simpy!", "hey simpy"]
loll_words = ["lol", "lul", "lal", "lil", "lel", "xd", "luk", "lok"]
#Custom Emojis
sangwoo = "<:Sangwoo:799573524976762911>"
yoonbum = "<:Yoonbum:799566988984713236>"
#Channels
#Notify2
notify2.init("Simpy-Bot")

class Message(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Messages Cog is online!")

    @commands.Cog.listener()
    async def on_member_join(member):
        gchannel = discord.utils.get(self.client.get_all_channels(), name='generale')
        print(f"{member.name} si è unito ad un server")
        try:
            embed=discord.Embed(title=f"Benvenut* {member.name}!", description="Per ricevere informazioni sul server digita $info", color=discord.Color.blue())
            await client.send_message(member, embed=embed)
            print(f"Messaggio di benvenuto inviato a {member.name}")
        except:
            print(f"Impossiblie inviare messaggio di benvenuto a {member.name}")
        await welcomechannel.send(f"Ciao {member.name}, ti do' il benvenuto nel server dell'Impero Gordiano!")

    @commands.Cog.listener()
    async def on_member_leave(member):
        print(f"{member.name} ha lasciato un server")
        try:
            embed=discord.Embed(title=f"Addio {member.name}!", color=discord.Color.blue())
            await client.send_message(member, embed=embed)
            print(f"Messaggio di addio inviato a {member.name}")
        except:
            print(f"Impossibile inviare il messaggio di addio a {member.name}")
        await welcomechannel.send(f"Addio {member.name}!")

    @commands.Cog.listener()
    async def on_message(self, message):
        #[0]
        if message.author == self.client.user:
            return
        #Mute
        elif any(word in message.content.lower() for word in mute_words):
            if str(message.author) != "Zoldie#4848":
                everyone = message.guild.get_role(753723195718107219)
                bup_roles = message.author.roles
                bup_roles.remove(everyone)
                role = discord.utils.get(message.guild.roles, name="Muted")
                await message.channel.send(f"<@{message.author.id}> verrai temp-mutat* per {tmt} secondi per questo!")
                muteN = notify2.Notification("Simpy-Bot", f"<@{message.author.name}> è stat* temp-mutato per {tmt} secondi", "/mnt/DATI/Documenti/Carlo/Simpy/icon.png")
                muteN.set_timeout(10000)
                muteN.show()
                await message.author.remove_roles(*bup_roles)
                await message.author.add_roles(role)
                embed=discord.Embed(title="Mute Temporaneo", description=f"Sei appena stat* mutat* per {tmt} secondi dal Server dell'Impero Gordiano per aver scritto il seguente messaggio:\n\n`\"{message.content}\"`\n\nSe vuoi evitare di venire bannat* nuovamente, ti consiglio di leggere la lista delle frasi e parole 'bannate' che trovi nel comando $helpme/$info sotto la voce \"Contenuto dei Messaggi\".\n\nA breve ri-otterrai il diritto di parola insieme ai ruoli che possedevi precedentemente.", color=discord.Color.red())
                try:
                    await message.author.send(embed=embed)
                except:
                    await message.channel.send(f"I DM di @{message.author.id} sono chiusi.")
                await asyncio.sleep(tmt)
                await message.author.remove_roles(role)
                await message.author.add_roles(*bup_roles)
                await message.channel.send(f"Adesso puoi parlare di nuovo <@{message.author.id}>, vedi di comportarti bene e di non dire altre profanità!\nTi tengo d'occhio... 👀")
            else:
                await message.channel.send("Carlo **PUÒ!**")
        #Reaction
        elif 'miao' in message.content.lower():
            await message.add_reaction("😺")
            await message.channel.send("Meow!")
        elif 'killing' in message.content.lower():
            await message.add_reaction(yoonbum)
            await message.add_reaction(sangwoo)
        #Text Responses
        elif any(word in message.content.lower() for word in ciao_words):
            if str(message.author) == "Zoldie#4848":
                await message.channel.send("Ciao papà!")
            elif str(message.author) == "Kula#1911":
                await message.channel.send("Ciao Grande Cicciona!")
            elif str(message.author) == "cotoletta#2106":
                await message.channel.send("Ciao Wiener Schnitzel!")
            elif str(message.author) == "avocasioo#5167":
                await message.channel.send("Miao Avocasio!")
            elif str(message.author) == "Gordy#0762":
                await message.channel.send("Salve Suorsovrana!")
            elif str(message.author) == "Chris262727#6509":
                await message.channel.send("Ciao Gutu!")
            elif str(message.author) == "Ines#9109":
                await message.channel.send("Ciao Nonna!")
            else:
                await message.channel.send("Ciao " + str(message.author) + "!")
        elif any(word in message.content.lower() for word in call_words):
            await message.channel.send("Dicami!")
        elif "sosneb" in message.content.lower():
            await message.channel.send("Sosneb anche secondo me")
        elif "hehe" in message.content.lower():
            await message.channel.send("HEHE TE NANDAYO")
        elif ':joy:' in message.content.lower():
            await message.channel.send(":joy:")
        elif any(word in message.content.lower() for word in loll_words):
            if not 'black' in message.content.lower():
                await message.channel.send("LOL XD :joy:")
            else:
                pass
        elif 'lmao' in message.content.lower():
            await message.channel.send("Lmao")
        elif 'cacca' in message.content.lower():
            await message.channel.send("LA CACCAA! :poop:")
        elif 'uwu' in message.content.lower():
            await message.channel.send(":smiling_face_with_3_hearts:")
        elif message.content.startswith("gg"):
            await message.channel.send("GG!")
        elif message.content.lower().startswith("simpy come stai?") or message.content.lower().startswith("come stai simpy?"):
            await message.channel.send("Bene, tu?")
        elif any(word in message.content.lower() for word in hate_words):
            await message.channel.send(":pleading_face:")
        elif message.content.lower().startswith("simpy ti voglio bene") or message.content.lower().startswith("ti voglio bene simpy"):
            await message.channel.send("Anche io ti voglio bene!")
        elif message.content.lower().startswith("ti amo simpy") or message.content.lower().startswith("simpy ti amo"):
            if str(message.author) == "cotoletta#2106":
                await message.channel.send("Anche io ti amo!")
            else:
                await message.channel.send("Scusa ma ti vedo solo come un amic*")
        elif 'sei bello' in message.content.lower():
            await message.channel.send("UwU :smiling_face_with_3_hearts:\nTutto grazie a Hilari!")
        elif "fammi un caffè" in message.content.lower():
            await message.channel.send("Ecco a lei! :coffee:")
        elif 'esplodi' in message.content.lower():
            await message.channel.send(":boom:")
        elif message.content.lower().startswith("grazie simpy"):
            await message.channel.send("Prego!")
        elif 'bruciargli la casa' in message.content.lower():
            await message.channel.send(":fire: Andiamo a bruciargli la casa! :fire:")

def setup(client):
    client.add_cog(Message(client))
