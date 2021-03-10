import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from InsultsApi import insults


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print("Ready")

@bot.command(name='teste')
async def testado(ctx):
    await ctx.send("testado")

@bot.command(name='insult', help='Writes a random insult')
async def insult(ctx):
    obj = insults.Insults()
    
    insult = obj.GetInsult()

    await ctx.send(insult)



bot.run(TOKEN)