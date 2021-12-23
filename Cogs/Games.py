import os.path

import discord
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

      elif c == "가위":
        rcs = [1, 2, 3]
        rcp = random.choice(rcs)
        if rcp == 1:
          await ctx.reply("아 비겻내 ㄲㅂ")
        elif rcp == 2:
          await ctx.reply("아 게잘하내 ㄷㄷ")
        elif rcp == 3:
          await ctx.reply("아 내가 이김 ㅋ")

      elif c == "찌":
        rcs = [1, 2, 3]
        rcp = random.choice(rcs)
        if rcp == 1:
          await ctx.reply("아 비겻내 ㄲㅂ")
        elif rcp == 2:
          await ctx.reply("아 게잘하내 ㄷㄷ")
        elif rcp == 3:
          await ctx.reply("아 내가 이김 ㅋ")

      elif c == "바위":
        rcs = [1, 2, 3]
        rcp = random.choice(rcs)
        if rcp == 1:
          await ctx.reply("아 내가 이김 ㅋ")
        elif rcp == 2:
          await ctx.reply("아 비겻내 ㄲㅂ")
        elif rcp == 3:
          await ctx.reply("아 게잘하내 ㄷㄷ")

      elif c == "묵":
        rcs = [1, 2, 3]
        rcp = random.choice(rcs)
        if rcp == 1:
          await ctx.reply("아 내가 이김 ㅋ")
        elif rcp == 2:
          await ctx.reply("아 비겻내 ㄲㅂ")
        elif rcp == 3:
          await ctx.reply("아 게잘하내 ㄷㄷ")

      elif c == "보":
        rcs = [1, 2, 3]
        rcp = random.choice(rcs)
        if rcp == 1:
          await ctx.reply("아 내가 이김 ㅋ")
        elif rcp == 2:
          await ctx.reply("아 게잘하내 ㄷㄷ")
        elif rcp == 3:
          await ctx.reply("아 비겻내 ㄲㅂ")

      elif c == "빠":
        rcs = [1, 2, 3]
        rcp = random.choice(rcs)
        if rcp == 1:
          await ctx.reply("아 내가 이김 ㅋ")
        elif rcp == 2:
          await ctx.reply("아 게잘하내 ㄷㄷ")
        elif rcp == 3:
          await ctx.reply("아 비겻내 ㄲㅂ")
      else: return await ctx.reply(f"`{c}`는 얻이서 나온 말이냐")
  
    @commands.command()
    async def 주사위(self, ctx):
      ran = random.randint(1, 6)
      await ctx.reply(f":game_die: 주사위에서 {ran}나옴 ㅋㅋㄹㅃㅃ")

def setup(bot):
    bot.add_cog(Games(bot))
