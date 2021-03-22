import os
import discord
import random
import inspirobot
from discord.ext import commands
#Directory
os.chdir("/mnt/DATI/Documenti/Carlo/Simpy")

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun Cog is online!")

    @commands.command(help="Invia una battuta black humor", aliases=["lol", "battuta"])
    async def blacklol(self, ctx):
        bl = [
        "Sai qual’è la differenza tra un ebreo e una palla?\nÈ che la palla può uscire dal campo, l’ebreo no.",
        "Quale è la frase preferita dai Nazisti?....Hai da accendere?",
        "Cosa hanno in comune un ebreo e la benzina?\nTutti e due prendono facilmente fuoco!",
        "Sapete come si fa un rave party in Africa?\nAttaccando una fetta di pane sul soffitto!",
        "Qual è l'unica cosa bianca di un negro?\nIl padrone.",
        "Sai cosa hanno di speciale le barzellette sui bambini morti?\nNon invecchiano mai!",
        "Sai perchè gli USA non sanno giocare a scacchi?\nPerchè gli mancano due torri!",
        "Nonna, che puzza di morto che c'è!\nNonna?\n...\nNonna?",
        "Sai perchè gli ebrei erano le persone più pulite al mondo?\nNo, perché?\nPerchè si facevano sempre la doccia!",
        "Un professore nero entra in una nuova classe, e si presenta dicendo\n\"Salve ragazzi, sono Ugo, ma potete anche chiamarmi Prof-Ugo\"",
        "Sai qual è la parte più dura da mangiare di un vegetale?\nLa carrozzina!",
        "Tutti dicono sempre dei pedofili, ma sono gli unici che davvero rallentano di fronte alle scuole.",
        "Qual'è la differenza tra l'acne e un prete?\nPrima che l'acne ti venga in faccia devi avere 13 anni.",
        "Qual è la differenza tra uno pneumatico e un nero?\nChe lo pneumatico mette le catene solo d'inverno!",
        "Si dice che gli ebrei siano i re dell'evasione, infatti entrano dalla porta e escono dal camino.",
        "La differenza tra un ebreo e il pane?\nChe il pane quando lo metti in forno non urla!",
        "Chi vince in una gara di corsa fra un ebreo e un tedesco?\nIl tedesco, perché lo brucia in partenza.",
        "Chi vincerebbe una gara di arrampicata tra un alpinista e Gesù?\nGesù perché ha i chiodi!",
        "Sai perché Bob cade dall'altalena?\nBoh, perché?\nPerché non ha le braccia! Ahahaha\nMa è una cosa bruttissima!\nOk proviamo con un'altra... Toc Toc!\nChi è?\nDi certo non Bob!",
        "Com'era il campo di concentramento?\nMah, tutto fumo e niente arrosto.",
        "Se ci pensi le granate a gas sono dei Hitler portatili.",
        "Perché i neri hanno i palmi dei piedi e delle mani bianchi?\nPerché in tutti c'è del buono.",
        "Che differenza c'è tra un ebreo e la pasta Barilla?\nIl tempo di cottura",
        "Cosa disse Dio quando creò il secondo uomo nero?\nCazzo! ne ho bruciato un altro!",
        "Sai perché la torre di Pisa è storta?\nPerché ha i riflessi migliori delle torri gemelle!",
        "Sai qual è la disciplina di atletica preferita dagli africani?\nIl salto del pasto!",
        "La mia ex stava sulla sedia a rotelle e gliel'ho rubata.\nIndovina chi è tornata da me strisciando?",
        "Hai cotto troppo questo ebreo! È diventato così nero che ha provato a rubarmi la bici!",
        "Le persone sono come le monete: più sono scure e meno valgono.",
        "Qual è la differenza tra Babbo Natale ed un ebreo?\nBabbo Natale dai camini ci entra, gli ebrei ci escono!",
        "Una volta ho chiesto il numero ad una tipa ebrea e lei mi ha mostrato il braccio.",
        "Quando mi annoio sputo addosso ad un bambino cieco e gli dico che sta piovendo.",
        "Sai cosa divide l'uomo dalle scimmie?\nIl Mediterraneo!"
        "Un bambino ebreo sta giocando con della polvere in un campo di concentramento. Arriva una SS tedesca e gli chiede:\n\"Stai cercando qualcuno?\""
        ]
        Chosen_Blol= random.choice(bl)
        await ctx.send(Chosen_Blol)

    @commands.command(help="Invia l'immagine di un personaggio casuale di Camp Buddy", aliases=["cb"])
    @commands.has_role("DJ")
    async def campbuddy(self, ctx):
        cb = [
        "https://static.wikia.nocookie.net/campbuddy/images/6/6d/Image_%283%29.png/revision/latest/top-crop/width/360/height/450?cb=20181122021607", #Keitaro
        "https://static.wikia.nocookie.net/campbuddy/images/4/40/Hiro-body.png/revision/latest?cb=20190328112936", #Hiro
        "https://static.wikia.nocookie.net/campbuddy/images/1/1e/Eduard.png/revision/latest?cb=20181127235010", #Eduard
        "https://em.wattpad.com/fbe9e6872ece3deb307f68755e041835a85288de/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f75616f664a55516b4a64737a53673d3d2d3731373135373434362e313539336132316137383764613863303536303739383232363934372e706e67?s=fit&w=720&h=720", #Natsumi
        "https://www.blitsgames.com/wp-content/uploads/2019/01/seto.png", #Seto
        "https://static.wikia.nocookie.net/campbuddy/images/4/41/Aiden.png/revision/latest?cb=20181122023929", #Aiden
        "https://static.wikia.nocookie.net/campbuddy/images/3/31/Taiga.png/revision/latest/top-crop/width/360/height/450?cb=20181122030011", #Taiga
        "https://i.pinimg.com/originals/2e/f8/20/2ef8200dfe30e0a989c542c0ecc4c271.png", #Yoichi
        "https://cdn141.picsart.com/308952797133211.png?type=webp&to=min&r=640", #Hunter
        "https://static.wikia.nocookie.net/campbuddy/images/6/6e/Felix.png/revision/latest?cb=20181122030525", #Felix
        "https://static.wikia.nocookie.net/campbuddy/images/5/54/Yuri-0.png/revision/latest?cb=20181122025421", #Yuri
        "https://static.wikia.nocookie.net/campbuddy/images/e/e7/Kieran.png/revision/latest?cb=20191204062006", #Kieran
        "https://static.wikia.nocookie.net/campbuddy/images/7/7e/Yoshinori.png/revision/latest?cb=20181122025354", #Yoshinori
        "https://static.wikia.nocookie.net/campbuddy/images/e/e7/Goro.png/revision/latest/top-crop/width/360/height/450?cb=20181122025657", #Goro
        "https://static.wikia.nocookie.net/campbuddy/images/5/50/Lee.png/revision/latest/top-crop/width/360/height/450?cb=20181128000637", #Lee
        "https://static.wikia.nocookie.net/campbuddy/images/4/49/Jirou-new.png/revision/latest/scale-to-width-down/291?cb=20190328082146", #Jirou
        "https://www.blitsgames.com/wp-content/uploads/2020/09/noah.png", #Noah
        "https://www.blitsgames.com/wp-content/uploads/2020/09/chiaki.png", #Chiaki
        "https://www.blitsgames.com/wp-content/uploads/2020/09/avan.png", #Avan
        "https://www.blitsgames.com/wp-content/uploads/2020/09/marco.png" #Marco
        ]
        chosen_image = random.choice(cb)
        embed = discord.Embed(
        color=discord.Color.blue()
        )
        embed.set_image(url=chosen_image)
        await ctx.send(embed=embed)

    @commands.command(help="Invia un'immagine 'ispirazionale' dal sito inspirobot.me", aliases=["inspirobot", "inspire"])
    async def inspireme(self, ctx):
        cuote = inspirobot.generate()
        quote = cuote.url
        embed = discord.Embed(
        color=discord.Color.blue()
        )
        embed.set_author(name="InspiroBot", icon_url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Finspirobot.me%2Fwebsite%2Fimages%2Finspirobot-dark-green.png&f=1&nofb=1")
        embed.set_image(url=quote)
        await ctx.send(embed=embed)

    @commands.command(help="Ripete il messaggio che segue", aliases=["ripeti", "repeat"])
    async def echo(self, ctx, *, message=None):
        message = message or "Per favore inserire il messaggio da ripetere."
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(help="Invia uno scioglilingua con molte esse", aliases=["s"])
    async def esse(self, ctx):
        esse = [
        "Ti ci stizzisci? E stizziscitici pure!",
        "La ringrazio assai commosso a più non posso fino all’osso insieme al mio molosso che sembra un colosso anche se sono scosso e forse anche percosso può darsi per il mare mosso così e non è un paradosso prima che io mi butti nel fosso lei è promosso.",
        "Streghe strabiche straparlano dicendo stramberie che stravolgono gli struzzi stramazzandoli sulla strada.",
        "Se l’arcivescovo di Costantinopoli si volesse arcivescovoscostantinopolizzare, vi arcivescovocostantinopolizzereste voi per arcivescovoscostantinopolizzare lui?",
        "Sa chi sa se sa chi sa, che se sa non sa se sa, sol chi sa che nulla sa, ne sa più di chi ne sa.",
        "Una platessa lessa lesse la esse di Lessie su un calesse fesso.",
        "Sette sassi smussati.",
        "Sotto le frasche del capanno quattro gatti grossi stanno; sotto quattro grossi sassi, quattro gatti grossi e grassi.",
        "Pensa a chi ti pensa, non pensare a chi non ti pensa, perché se tu pensi a chi non ti pensa, quello che ti pensa potrebbe pensare che tu non lo stai pensando. Non pensare come pensi che pensi uno che non pensa; meglio pensare come pensi che pensi uno che pensa.\nPensaci."
        ]
        await ctx.send(random.choice(esse))

    @commands.command(help="Inverte le lettere del messaggio inviato", aliases=["inverti", "rovescia"])
    async def reverse(self, ctx, *, text:str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")

    @commands.command(help="Invia una parola casuale che inizia con salv")
    async def salv(self, ctx):
        salv=["Salvia", "Salvagente", "Salvezza", "Salvadanaio", "Salve", "Salvo", "Salvatore", "Salvaguardia", "Salvifico", "Salvi", "Salvazione", "Salvatichezza", "Salvagione", "Salvadrici", "Salvaggio", "Salvastrella", "Salvera", "Salvinia", "Salvietta", "Salvino", "Salvadoregna", "Salvatacco"]
        await ctx.send(random.choice(salv))

    @commands.command(help="Mostra l'avatar del membro taggato")
    @commands.guild_only()
    async def avatar(self, ctx, *, user: discord.Member = None):
        user = user or ctx.author
        await ctx.send(f"Avatar di **{user.name}**\n{user.avatar_url_as(size=1024)}")

    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send("Questo comando può essere utilizzato solo nei server.")

def setup(client):
    client.add_cog(Fun(client))
