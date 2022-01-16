import os.path

import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
from discord.ext.commands import CommandNotFound
import pytz
from webserver import keep_alive
from koreanbots.integrations.discord import DiscordpyKoreanbots
import traceback


bot = commands.Bot(command_prefix="잼민아 ")
bot.remove_command("help")
kb = DiscordpyKoreanbots(bot, 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjkyMTQyNDcyNDcyOTM5NzMxOCIsImlhdCI6MTY0MDA5ODk2NX0.M_rzLn9UPpo0jpR2HZhs5uBLwtqWdCIHLIIF_-PXZoXbhmDPscEjrYzzCsX7w_6TG7zlKqORD4dyzUNefUXRzxPOA7tWvw8iJFqeW58hyzkR6pR2Igs-FhQ8wvcuBs1MtPdA9GqWhap5E96nSsuXCpoh6tZA9u-GjKakHwnZGc4', run_task=True)

for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")
        print(f"{filename[:-3]}가 로드되었습니다.")


@bot.event
async def on_ready():
    status = cycle(["잼민이봇", "잼민아 명령어", str(len(bot.guilds)) + "서버에 잼민이봇이 있음!"])

    @tasks.loop(seconds=8)
    async def change_status():
        await bot.change_presence(activity=discord.Game(next(status)))

    change_status.start()
    print("ready")
    print(str(len(bot.guilds)) + "server join")

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
          embed = discord.Embed(color=0x000000)
          embed.set_author(name="잼민이봇을 초대해주셔서 감사합니다!", icon_url="https://t.ly/QXEv")
          embed.add_field(name="개발자", value="> Team DM\n> <@433183785564110848>")
          embed.add_field(name="잼민이봇 서포트 서버", value="[[참여하기]](https://discord.gg/B6MjFDjz23)")
          embed.add_field(name="잼민이봇 투표해주세요!", value="[[투표하기]](https://koreanbots.dev/bots/921424724729397318/vote)", inline=False)
          embed.add_field(name="잼민이봇 초대링크", value="[[초대하기]](http://invite.jambot.kro.kr)")
          await channel.send(embed=embed)
        break

@bot.event
async def on_command_error(ctx, error):
    tb = traceback.format_exception(type(error), error, error.__traceback__)
    err = [line.rstrip() for line in tb]
    errstr = '\n'.join(err)
    if isinstance(error, commands.NotOwner):
        await ctx.send('봇 주인만 사용 가능한 명령어입니다')
    elif isinstance(error, CommandNotFound): 
      await ctx.send("멀아는걷야;; `잼민아 명령어`쳐서 좀 아라와!  \n오류가 계속된다면 `잼민아 버그`명령어를 사용해주세요!")

bot.run(TOKEN)
