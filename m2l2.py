import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'we have logged in as {bot.user}')

tips_list = [
    "normalize using refillable water bottles",
    "try separating organic and inorganic waste at home",
    "refuse any type of plastic straws when buying a drink",
    "use cloth shopping bags instead if plastic bags",
    "finish your food so that it doesn't turn into wastes"
]

@bot.command()
async def tips(ctx):
    await ctx.send(random.choice(tips_list))

@bot.command()
async def challenge(ctx):
    await ctx.send(
        "today: avoid single-use plastic\n"
        "type $done when finished"
    )

@bot.command()
async def done(ctx):
    await ctx.send("nice ! you're one step closer to a green environment")

bot.run('TOKEN')
