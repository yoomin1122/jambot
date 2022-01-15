import os.path

import discord, asyncio
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random
import time
import datetime
from webserver import keep_alive

class Games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def 가위바위보(self, ctx, c:str=None):
      if c is None:
        await ctx.send("뒤에 가위(찌), 바위(묵), 보(빠)를 쳐야지 이 바보야  `예시) 잼민아 가위바위보 바위`")

      elif c == "가위" or c == "찌":
        rcs = [1, 2, 3]
        rcp = random.choice(rcs)
        if rcp == 1:
          await ctx.reply("아 비겻내 ㄲㅂ")
        elif rcp == 2:
          await ctx.reply("아 게잘하내 ㄷㄷ")
        elif rcp == 3:
          await ctx.reply("아 내가 이김 ㅋ")

      elif c == "바위" or c == "묵":
        rcs = [1, 2, 3]
        rcp = random.choice(rcs)
        if rcp == 1:
          await ctx.reply("아 내가 이김 ㅋ")
        elif rcp == 2:
          await ctx.reply("아 비겻내 ㄲㅂ")
        elif rcp == 3:
          await ctx.reply("아 게잘하내 ㄷㄷ")

      elif c == "보" or c == "빠":
        rcs = [1, 2, 3]
        rcp = random.choice(rcs)
        if rcp == 1:
          await ctx.reply("아 내가 이김 ㅋ")
        elif rcp == 2:
          await ctx.reply("아 게잘하내 ㄷㄷ")
        elif rcp == 3:
          await ctx.reply("아 비겻내 ㄲㅂ")

    @commands.command(aliases=["주사위"])
    async def 주사위게임(self, ctx):
      r = random.randint(1, 6)
      a = random.randint(1, 6)

      if(r>a):
        await ctx.reply(f"아내가이김 ㅋㅋㄹㅃㅃ \n> 잼민이봇 : {r} vs {ctx.author.mention} : {a}")
      elif(r<a):
        await ctx.reply(f"아ㄲㅂ 노잼티비! \n> 잼민이봇 : {r} vs {ctx.author.mention} : {a}")
      elif(r==a):
        await ctx.reply(f"아 동점임 노잼 ㅋㅋㄹㅃㅃ \n> 잼민이봇 : {r} vs {ctx.author.mention} : {a}")

def setup(bot):
    bot.add_cog(Games(bot))
