import os.path

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random
import time
import datetime

class Core(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="출력") #수정
    async def printit(self, ctx): #수정
        choice = random.choice([":) Python Bot에 의해 출력됨.", "2", "3", "4"])
        await ctx.send(choice)
    
    @commands.command()
    async def 핑(self, ctx):
      embed = discord.Embed(color=0x4ACE72)
      embed.set_author(name="잼민이봇 지연시간(ping)")
      embed.add_field(name="메시지", value=f'{round(self.bot.latency * 1000)}ms')
      await ctx.reply(embed=embed, mention_author=False)

    @commands.command(name="ㅎㅇ", aliases=["안녕", "ㅎㅇㅎㅇ"]) #수정
    async def hello(self, ctx): #수정
        choice = random.choice(["않녕하새요 잼민이에요", "멀봐 ", "엊절티비"])
        await ctx.send(choice)
    
    @commands.command()
    async def hellothisisverification(self, ctx):
      await ctx.send("YooMin1122#5973 (433183785564110848)")


    @commands.command()
    async def 명령어(self, ctx, c:str=None):
      if c is None:
        embed = discord.Embed(color=0xb5fb94)
        embed.set_author(name="명령어", icon_url="https://i.ibb.co/M71ftRF/image.jpg")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=":point_right: 접두사", value="접두사는 `,(쉼표)`와 `재깨야 `입니다", inline=False)
      elif c == "접두사":
        embed = discord.Embed(color=0xb5fb94)
        embed.set_author(name="접두사", icon_url="https://i.ibb.co/M71ftRF/image.jpg")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=":point_right: 접두사", value="접두사는 `잼민아 `임!", inline=False)
      elif c == "일반":
        embed = discord.Embed(color=0xb5fb94)
        embed.set_author(name="서버관리", icon_url="https://i.ibb.co/M71ftRF/image.jpg")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=":loudspeaker: 서버관리", value="청소", inline=False)
        embed.add_field(name="청소", value="청소 : 채팅을 청소해줍니다 (최대 99)", inline=False)
      elif c == "대화":
        embed = discord.Embed(color=0xb5fb94)
        embed.set_author(name="서버관리", icon_url="https://i.ibb.co/M71ftRF/image.jpg")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=":loudspeaker: 서버관리", value="청소", inline=False)
        embed.add_field(name="청소", value="청소 : 채팅을 청소해줍니다 (최대 99)", inline=False)
      elif c == "게임":
        embed = discord.Embed(color=0xb5fb94)
        embed.set_author(name="서버관리", icon_url="https://i.ibb.co/M71ftRF/image.jpg")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=":loudspeaker: 서버관리", value="청소", inline=False)
        embed.add_field(name="청소", value="청소 : 채팅을 청소해줍니다 (최대 99)", inline=False)
      else: return await ctx.reply(f"`{c}`라는 카테고리는 존재하지 않아요")
      await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(Core(bot))
