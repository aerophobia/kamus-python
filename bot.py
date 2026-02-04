import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'we have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def heh(ctx,*,message):
    await ctx.send(message)

bot.run("TOKEN")
