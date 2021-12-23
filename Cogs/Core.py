import os.path

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random
import time
import datetime
from webserver import keep_alive

class Core(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="출력") #수정
    async def printit(self, ctx): #수정
        choice = random.choice([":) Python Bot에 의해 출력됨.", "2", "3", "4"])
        await ctx.send(choice)
    
    @commands.command()
    async def 핑(self, ctx):
      embed = discord.Embed(color=0x000000)
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
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="명령어", icon_url="https://t.ly/QXEv")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=":point_right: 접두사", value="> 접두사는 `잼민아 `입니다!", inline=False)
        embed.add_field(name=":loudspeaker: 일반", value="> 핑, 안녕", inline=False)
        embed.add_field(name=":speech_balloon: 대화", value="> 야, 잼민아, 오버워치, 마인크래프트, 아재개그, 샌즈(언더테일), 정상수 \n 랜덤의 메세지가 나옵니다!", inline=False)
        embed.add_field(name=":video_game: 게임", value="> 가위바위보, 주사위", inline=False)
      elif c == "접두사":
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="접두사", icon_url="https://t.ly/QXEv")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=":point_right: 접두사", value="> 접두사는 `잼민아 `입니다!", inline=False)
      elif c == "일반":
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="일반", icon_url="https://t.ly/QXEv")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=": loudspeaker: 일반", value="핑, 안녕", inline=False)
        embed.add_field(name="핑", value="> 잼민이봇의 지연시간 확인용 입니다", inline=False)
        embed.add_field(name="안녕", value="> 잼민이 봇과 인사합니다!", inline=False)
      elif c == "대화":
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="대화", icon_url="https://t.ly/QXEv")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=":speech_balloon: 대화", value="각 명령어마다 랜덤의 메세지가 나옵니다!", inline=False)
        embed.add_field(name="목록", value="> 야, 잼민아, 오버워치, 마인크래프트, 언더테일(샌즈), 정상수", inline=False)
      elif c == "게임":
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="게임", icon_url="https://t.ly/QXEv")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=":video_game: 게임", value="가위바위보, 주사위", inline=False)
        embed.add_field(name="가위바위보", value="> 안내면 진다 가위바위보!", inline=False)
        embed.add_field(name="주사위", value="> 과연 몇이 나올까?", inline=False)
      else: return await ctx.reply(f"`{c}`라는건 업는대")
      await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(Core(bot))
