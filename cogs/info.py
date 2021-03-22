import os
import discord
from discord.ext import commands
#Directory
os.chdir("/mnt/DATI/Documenti/Carlo/Simpy")

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Info Cog is online!")

    @commands.command(help="Invia una lista con regole ed informazioni del server", aliases=['info', "aiuto"])
    async def helpme(self, ctx):
        embed = discord.Embed(
        title="Informazioni del Server",
        color=discord.Color.blue()
        )
        embed.set_author(name="Simpy-Bot", icon_url="https://discordtemplates.me/static/img/icon.png")
        embed.add_field(name="Generali", value="Server per giocare e guardare film/serie tv insieme!", inline=False)
        embed.add_field(name="Ruoli", value="Il ruolo Admin è strettamente riservato al proprietario del server, che possiede tutti i privilegi disponibili.\nIl ruolo Dj dà accesso al canale riservato alla gestione delle playlist del bot MEE6.\nAi giocatori verrà assegnato un ruolo in base ai giochi che utilizzano, che darà loro accesso ai canali testuali e vocali dei rispettivi giochi.\nDiscorso simile avviene per gli ospiti delle stream di serie tv e film.", inline=False)
        embed.add_field(name="Contenuto Messaggi", value="Sono ammesse parolacce, bestemmie e black-humor.\nMessaggi formulati in particolari modi e/o fastidiosi portano al warn automatico.\nSpam e invio di materiale inappropriato vengono puniti severamente.\nLe seguenti frasi/parole sono proibite e porteranno al mute temporaneo: 'Eren è figo', 'Eren è meglio di', 'Gordy fa schifo', 'Levi fa schifo'\nPer sapere di più sulle segnalazioni digita $helpwarn.")
        embed.add_field(name="Canali", value="Nel canale testuale generale si può parlare di qualsiasi cosa si voglia, a meno che non esista un canale testuale adibito a ciò di cui si vuole parlare.\nI canali testuali e vocali dei videogiochi devono essere utilizzati unicamente per parlare del gioco in oggetto.\nIl canale testuale music-quiz va utilizzato unicamente per giocare ai quiz musicali.\nIl canale bot-playlist va utilizzato unicamente per interagire con le funzioni musicali di MEE6.\nNei canali log e report vengono inviati tutti i report e le attività degli utenti nel server, è vietato scrivere messaggio alcuno.", inline=False)
        embed.add_field(name="Bot", value="I bot utilizzati in questo server sono MEE6 (un bot commerciale) e Simpy (un bot creato e gestito da Zoldie).\nMEE6 è online 24/7 (in quanto gestito da server esterni)\nSimpy è online unicamente quando il suo file Python è in compilazione, i membri possono fare richiesta per avere il file in oggetto al proprietario, dimostrando prima di essere in grado di utilizzarlo correttamente.", inline=False)
        embed.add_field(name="Comandi Simpy", value="Se vuoi avere una lista dei comandi di Simpy digita in chat $help per una semplice lista dei comandi oppure $helpcom per una descrizione più dettagliata.", inline=False)
        embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.author.send(embed=embed)

    @commands.command(help="Invia una lista dei comandi con il loro funzionamento", aliases=["comandi", "commands"])
    async def helpcom(self, ctx):
        command = open("Things/Commands.py","rt")
        content = command.read()
        command.close
        embed = discord.Embed(
        title="Lista Comandi Simpy",
        color=discord.Color.blue()
        )
        exec(content)
        embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.author.send(embed=embed)

    @commands.command(help="Invia informazioni sulle segnalazioni")
    async def helpwarn(self, ctx):
        embed = discord.Embed(
        title="Segnalazioni/Warn",
        color=discord.Color.blue()
        )
        embed.set_author(name="Simpy-Bot", icon_url="https://discordtemplates.me/static/img/icon.png")
        embed.add_field(name="Warn Automatici", value="Le segnalazioni automatiche avverranno in questi casi:\n-Testo ripetuto\n-Maiuscole eccessive (+ del 70% delle lettere del messaggio sono maiuscole)\n-Troppe Emoji (+ di 5 emoji presenti in un messaggio)\n-Troppi spoiler (+ di 5 spoiler presenti in un messaggio)\n-Troppe menzioni (+ di 5 in un messaggio)\n-Testo zalgo", inline=False)
        embed.add_field(name="Avvisi", value="Quando un utente tenta di utilizzare un comando elevato senza l'autorizzazione il bot invia a tutti gli Admin un avviso. Sta poi all'Admin decidere se segnalare e/o punire l'utente o no.")
        embed.add_field(name="Conseguenze Warn", value="3+ segnalazioni negli ultimi 10 minuti = Mute temporaneo per 1 ora\n10+ segnalazioni negli ultimi 10 giorni = Ban temporaneo per 5 giorni\n20+ segnalazioni negli ultimi 15 giorni = Espulsione\n50+ segnalazioni negli ultimi 365 giorni = Ban permanente", inline=False)
        embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.author.send(embed=embed)

    @commands.command(help="Invia il Changelog completo di Simpy")
    @commands.dm_only()
    async def update(self, ctx, page=1):
        if page == 1:
            update = open("Things/Update.py", "rt")
            content = update.read()
            update.close
            embed = discord.Embed(
            title="Ultimi Update",
            color=discord.Color.blue()
            )
            embed.add_field(name="Pagina 1/4", value="Per visualizzare le altre pagine digita in chat '$update <*numero_pagina*>.\n\n", inline=False)
            exec(content)
            embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
            await ctx.author.send(embed=embed)
        elif page == 2:
            update = open("Things/Update2.py", "rt")
            content = update.read()
            update.close
            embed = discord.Embed(
            title="Ultimi Update",
            color=discord.Color.blue()
            )
            embed.add_field(name="Pagina 2/4", value="Per visualizzare le altre pagine digita in chat '$update <*numero_pagina*>'.\n\n", inline=False)
            exec(content)
            embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
            await ctx.author.send(embed=embed)
        elif page == 3:
            update = open("Things/Update3.py", "rt")
            content = update.read()
            update.close
            embed = discord.Embed(
            title="Ultimi Update",
            color=discord.Color.blue()
            )
            embed.add_field(name="Pagina 3/4", value="Per visualizzare le altre pagine digita in chat '$update <*numero_pagina*>'\n\n")
            exec(content)
            embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
            await ctx.author.send(embed=embed)
        elif page == 4:
            update = open("Things/Update4.py", "rt")
            content = update.read()
            update.close
            embed = discord.Embed(
            title="Ultimi Update",
            color=discord.Color.blue()
            )
            embed.add_field(name="Pagina 4/4", value="Per visualizzare le altre pagine digita in chat '$update <*numero_pagina*>'\n\n")
            exec(content)
            embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
            await ctx.author.send(embed=embed)
        else:
            await ctx.send("La pagina che stai cercando non esiste.")

    @commands.command(help="Nuovo sistema di visualizzazione changelog", aliases=["changelog", "cl"])
    @commands.guild_only()
    async def better_changelog(self, ctx):
        embed = discord.Embed(title="Navigatore Changelog", description="Benvenuto al navigatore del changelog di Simpy! Nelle pagine del Changelog trovi tutte le modifiche che sono state fatte a Simpy nel corso del suo sviluppo.\nAggiungi una reazione a quelle già esistenti per visualizzare la pagina che desideri.\nL'ordine delle pagine è dalla più vecchia alla più recente.\nDopo 2 minuti il changelog verrà eliminato per non intasare le chat.", color=discord.Color.blue())
        embed.set_author(name="Simpy-Bot", icon_url="https://discordtemplates.me/static/img/icon.png")
        embed.add_field(name="==[1️⃣]==", value="09/10/20\n11/12/20", inline=True)
        embed.add_field(name="==[2️⃣]==", value="11/12/20\n15/01/21", inline=True)
        embed.add_field(name="==[3️⃣]==", value="15/01/21\n27/02/21", inline=True)
        embed.add_field(name="==[4️⃣]==", value="27/02/21\noggi", inline=True)
        embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        dir = await ctx.send(embed=embed, delete_after=120)
        await dir.add_reaction("1️⃣")
        await dir.add_reaction("2️⃣")
        await dir.add_reaction("3️⃣")
        await dir.add_reaction("4️⃣")
        try:
            reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in ["1️⃣", "2️⃣", "3️⃣", "4️⃣"], timeout=60.0)
        except asyncio.TimeoutError:
            print("Checker:\n=====================================\nChangelog_Director Request Time Ended\n=====================================")
        else:
            if reaction.emoji == "1️⃣":
                update = open("Things/Update.py", "rt")
                content = update.read()
                update.close
                embed = discord.Embed(
                title="Changelog - Pagina 1",
                description="Registro dei cambiamenti allo script di Simpy dal giorno 09/10/20 al giorno 11/12/20.",
                color=discord.Color.blue()
                )
                exec(content)
                embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed, delete_after=120)
                await dir.clear_reaction("1️⃣")
                await dir.clear_reaction("2️⃣")
                await dir.clear_reaction("3️⃣")
                await dir.clear_reaction("4️⃣")
            elif reaction.emoji == "2️⃣":
                update = open("Things/Update2.py", "rt")
                content = update.read()
                update.close
                embed = discord.Embed(
                title="Changelog - Pagina 2",
                description="Registro dei cambiamenti allo script di Simpy dal giorno 11/12/20 al giorno 15/01/21.",
                color=discord.Color.blue()
                )
                exec(content)
                embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed, delete_after=120)
                await dir.clear_reaction("1️⃣")
                await dir.clear_reaction("2️⃣")
                await dir.clear_reaction("3️⃣")
                await dir.clear_reaction("4️⃣")
            elif reaction.emoji == "3️⃣":
                update = open("Things/Update3.py", "rt")
                content = update.read()
                update.close
                embed = discord.Embed(
                title="Changelog - Pagina 3",
                description="Registro dei cambiamenti allo script di Simpy dal giorno 21/01/21 al giorno 27/02/21.",
                color=discord.Color.blue()
                )
                exec(content)
                embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed, delete_after=120)
                await dir.clear_reaction("1️⃣")
                await dir.clear_reaction("2️⃣")
                await dir.clear_reaction("3️⃣")
                await dir.clear_reaction("4️⃣")
            elif reaction.emoji == "4️⃣":
                update = open("Things/Update4.py", "rt")
                content = update.read()
                update.close
                embed = discord.Embed(
                title="Changelog - Pagina 4",
                description="Registro dei cambiamenti allo script di Simpy dal giorno 27/02/21 ad oggi.",
                color=discord.Color.blue()
                )
                exec(content)
                embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed, delete_after=120)
                await dir.clear_reaction("1️⃣")
                await dir.clear_reaction("2️⃣")
                await dir.clear_reaction("3️⃣")
                await dir.clear_reaction("4️⃣")

    @commands.command(help="Invia una lista delle feature in arrivo")
    async def soon(self, ctx):
        soon = open("Things/Soon.py", "rt")
        content = soon.read()
        soon.close
        embed = discord.Embed(
        title="Features in Corso di Sviluppo e Features Programmate",
        color=discord.Color.blue()
        )
        exec(content)
        embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.author.send(embed=embed)

    @commands.command(help="Invia informazioni tecniche sul server")
    @commands.guild_only()
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url)
        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=icon)
        embed.set_author(name="Simpy-Bot", icon_url="https://discordtemplates.me/static/img/icon.png")
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(help="Invia la lista dei comandi vocali", aliases=["sfx"])
    async def soundboard(self, ctx):
        embed = discord.Embed(
        title='Soundboard',
        color=discord.Color.blue()
        )
        embed.set_author(name="Simpy-Bot", icon_url="https://discordtemplates.me/static/img/icon.png")
        embed.add_field(name="Informazioni Generali", value="La soundboard serve per riprodurre audio attraverso Simpy, può essere utilizzata da tutti i membri, ma funziona unicamente quando Simpy è in un canale vocale.\nPer il corretto funzionamento del comando è necessario digitare *$[nome_della_sezione] [keyword]*\nEs: '$barbero bruciare'.", inline=False)
        embed.add_field(name="Alessandro Barbero ($barbero)", value=">completo: Riproduce interamente la canzone 'Andiamo a bruciargli la casa',\n>bruciare: Riproduce la frase 'Andiamo a bruciargli la casa'.\n>furore: Riproduce la frase 'Il furore dilaga in città'.\n>risparmia: Riproduce la frase 'Stavolta non vengono risparmiati'.\n>buonasera: Riproduce la frase 'Buonasera'.\n", inline=False)
        embed.add_field(name="Hazbin Hotel($hazbin)", value=">kinky: Riproduce la frase 'Kinky',\n>suck: Riproduce la frase 'I can suck your dick'.\n>no: Riproduce la frase 'Ah! No!'.\n>daddy: Riproduce la frase 'Oh Harder daddy!'.\n>drug: Riproduce la frase 'My drugs!'.\n>god: Riproduce la frase 'Oh my god'.\n>retarded: Riproduce la frase 'Retarded'.\n>jambalaya: Riproduce la frase 'Well I'm starved, who wants some jambalaya?'.\n>lonely: Riproduce la frase 'When I'm lonely, I become hungry...'.\n>pervert: Riproduce la frase 'Oh not like that, pervert!'.\n>speak: Riproduce la frase 'May I speak now?'.\n>stage: Riproduce la frase 'The world is a stage and a stage is a world of entertainment.'.\n>smile: Riproduce la frase 'Smile my dear, you know you're never fully dressed without one'.\n>maybe: Riproduce la frase 'Maybe...'.\n>fair: Riproduce la frase 'Fair Enough'.\n", inline=False)
        embed.add_field(name="Mix ($mix)", value=">seal: Riproduce il verso di una foca.\n>spermo: Riproduce la frase 'Lo spermo ioooo'.\n>euforico: riproduce la frase 'Sono veramente euforico!'\n>cri: riproduce il suono dei grilli.\n", inline=False)
        embed.set_footer(text=f"Informazioni richieste da {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #Error Handler
    @better_changelog.error
    async def changelog_error(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send("Questo comando può essere utilizzato solo nei server, nei DM puoi usare il comando $update.")
    @update.error
    async def update_error(self, ctx, error):
        if isinstance(error, commands.PrivateMessageOnly):
            await ctx.send("Questo comando può essere utilizzato solo nei DM di Simpy, nei server puoi usare il comando $changelog.")
    @serverinfo.error
    async def serverinfo_error(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send("Questo comando può essere utilizzato solo nei server.")

def setup(client):
    client.add_cog(Info(client))
