import os
import discord
import random
from discord.ext import commands
#Directory
os.chdir("/mnt/DATI/Documenti/Carlo/Simpy")

player1 = ""
player2 = ""
turn = ""
gameOver = True
board = []
winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

class Game(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help="Inizia una partita a tris")
    async def tris(self, ctx, p1:discord.Member, p2:discord.Member):
        global player1
        global player2
        global turn
        global gameOver
        global count

        if gameOver:
            global board
            board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:"]
            turn = ""
            gameOver = False
            count = 0
            player1 = p1
            player2 = p2
            #Print Board
            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + board[x]
            #Randomize the first player
            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await ctx.send("È il turno di <@" + str(player1.id) + ">")
            elif num == 2:
                turn = player2
                await ctx.send("È il turno di <@" + str(player2.id) + ">")
        else:
            await ctx.send("Qualcuno sta già giocando!")

    @commands.command(help="Piazza il tuo segno su una casella")
    async def place(self, ctx, pos:int):
        global turn
        global player1
        global player2
        global board
        global count
        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                    board[pos - 1] = mark
                    count += 1
                    #print board
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + board[x]
                    checkWinner(winningConditions, mark)
                    print(count)
                    if gameOver == True:
                        await ctx.send(mark + " ha vinto!")
                    elif count >= 9:
                        gameOver = True
                        await ctx.send("La partita è finita in parità!")
                    #Switch turn
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1
                else:
                    await ctx.send("Assicurati di aver inserito un numero tra 1 e 9 libero.")
            else:
                await ctx.send("Non è il tuo turno!")
        else:
            await ctx.send("Sembra che non ci sia una partita in corso, cominciane una usando il comando $tris!")

    def checkWinner(self, winningConditions, mark):
        for condition in winningConditions:
            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                gameOver = True

    @commands.command(help="Termina la partita di tris in corsos")
    async def trisquit(self, ctx):
        global gameOver
        gameOver = True

    @tris.error
    async def tris_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Tagga 2 persone per giocare!")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Assicurati di aver taggato i giocatori! (Es: <@762715110752911400>)")
    @place.error
    async def place_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Inserisci la posizione che vorresti segnare!")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Assicurati di inserire un numero intero compreso tra 1 e 9 (inclusi)!")

def setup(client):
    client.add_cog(Game(client))
