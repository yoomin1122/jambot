import os.path

import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from discord.ext.commands import CommandNotFound
import pytz
from koreanbots.integrations.discord import DiscordpyKoreanbots
import traceback
import jishaku
from discord_slash import SlashCommand
import datetime
import asyncio



bot = commands.Bot(command_prefix="잼민아 ")
bot.remove_command("help")
bot.load_extension('jishaku')
slash = SlashCommand(bot, sync_commands=True)
kb = DiscordpyKoreanbots(bot, 'koreanlist_token', run_task=True)

for filename in os.listdir('Cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")
        print(f"{filename[:-3]}가 로드되었습니다.")


@bot.event
async def on_ready():
    status = cycle(["잼민이봇", "잼민아 명령어", f"{len(bot.guilds)} 서버에 잼민이봇이 있음!"])
    @tasks.loop(seconds=5)
    async def change_status():
        await bot.change_presence(activity=discord.Game(next(status)))

    change_status.start()
    print("ready")
    print(str(len(bot.guilds)) + "server join")

@bot.event
async def on_guild_join(guild):
        if guild.system_channel: # If it is not None
          embed = discord.Embed(color=0x000000)
          embed.set_author(name="잼민이봇을 초대해주셔서 감사합니다!", icon_url="https://t.ly/QXEv")
          embed.add_field(name="개발자", value="> Team. YooMin1122 \n<@433183785564110848>")
          embed.add_field(name="잼민이봇 서포트 서버", value="[[참여하기]](https://discord.gg/B6MjFDjz23)")
          embed.add_field(name="잼민이봇 투표해주세요!", value="[[투표하기]](https://jambot.fun/vote)", inline=False)
          embed.add_field(name="서비스 이용 약관", value="[[확인하기]](https://wadeinteractive.net/terms)")
          embed.add_field(name="개인정보 보호정책", value="[[확인하기]](https://wadeinteractive.net/privacy)")
          await guild.system_channel.send(embed=embed)
          print(f"{guild.name}({guild.id})에 추가됨 현재 {len(bot.guilds)}서버에 있음")

@bot.event
async def on_guild_remove(guild):
    print(f"{guild.name}({guild.id})에서 추방당함 현재 {len(bot.guilds)}서버에 있음")

@bot.event
async def on_command_error(ctx, error):
    tb = traceback.format_exception(type(error), error, error.__traceback__)
    err = [line.rstrip() for line in tb]
    errstr = '\n'.join(err)
    if isinstance(error, commands.NotOwner):
        await ctx.send('봇 주인만 사용 가능한 명령어입니다.')   


bot.run('token')
