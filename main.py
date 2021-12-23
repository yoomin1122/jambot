import os.path

import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from discord.ext.commands import CommandNotFound
import pytz
from webserver import keep_alive
from koreanbots.integrations.discord import DiscordpyKoreanbots


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="잼민아 ", intents=intents)
bot.remove_command("help")
kb = DiscordpyKoreanbots(bot, 'koreanbots_TOKEN', run_task=True)

for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")
        print(f"{filename[:-3]}가 로드되었습니다.")


@bot.event
async def on_ready():
    status = cycle(["잼민이봇", "잼민아 명령어"])

    @tasks.loop(seconds=10)
    async def change_status():
        await bot.change_presence(activity=discord.Game(next(status)))

    change_status.start()
    print("ready")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound): 
      await ctx.send("멀아는걷야;; `잼민아 명령어`쳐서 좀 아라와!")
      return
    raise error

bot.run(TOKEN)
