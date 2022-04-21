import os.path

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random
import time
import datetime
import traceback
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_components import  create_actionrow, create_button
from discord_slash.model import ButtonStyle
from discord_slash.context import MenuContext
from discord_slash.model import ContextMenuType
from koreanbots.integrations.discord import DiscordpyKoreanbots
import requests
import json
import urllib.request


class Core(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def 투표(self, ctx):
      kb = DiscordpyKoreanbots(self.bot, 'koreanlist_token', run_task=True)
      data = await kb.is_voted(ctx.author.id, "921424724729397318")

      if data.voted == True:
        await ctx.reply(f"머야툽표헸내 ㅋㅋ")
      elif data.voted == False:
        await ctx.reply(f"머야외툽표안함? 빨리하샘 \nhttps://jambot.fun/vote")

    @commands.command(aliases=["테스트" "print"])
    async def core(self, ctx):
        await ctx.send(f"잼민이봇 출력됨 \n{round(self.bot.latency * 1000)}ms")
    @cog_ext.cog_slash(name="hellothisisverification", description="개발자를 확인해보세요!")
    async def _test(self, ctx: SlashContext):
        await ctx.send("YooMin1122#5973 (433183785564110848)")
    @cog_ext.cog_slash(name="핑", description="잼민이봇의 지연시간을 확인할수 있어요!")
    async def _ping(self, ctx):
      embed = discord.Embed(color=0x000000)
      embed.set_author(name="잼민이봇 지연시간(ping)")
      embed.add_field(name="메시지", value=f'{round(self.bot.latency * 1000)}ms')
      await ctx.send(embed=embed)
    @commands.command(aliases=["ping" "지연시간"])
    async def 핑(self, ctx):
      embed = discord.Embed(color=0x000000)
      embed.set_author(name="잼민이봇 지연시간(ping)")
      embed.add_field(name="메시지", value=f'{round(self.bot.latency * 1000)}ms')
      await ctx.reply(embed=embed, mention_author=False)

    @commands.command(name="ㅎㅇ", aliases=["안녕", "ㅎㅇㅎㅇ", "하이", "안녕하세요", "안녕?"]) #수정
    async def hello(self, ctx): #수정
        choice = random.choice(["않녕하새요 잼민이에요", "멀봐 ", "엊절티비", "ㅎㅇ", "안녕팁의", "ㅎㅇㅌㅂ", "응 ㅎㅇ"])
        await ctx.send(choice)
    
    @commands.command(aliases=["개발자", "developer"])
    async def hellothisisverification(self, ctx):
      await ctx.send("YooMin1122#5973 (433183785564110848) \n달콤한개굴이#6661 (692619473148051496)")

    @commands.command(aliases=["invite"])
    async def 초대(self, ctx):
      await ctx.send(f"**잼민이봇 초대** \n> https://discord.com/api/oauth2/authorize?client_id=921424724729397318&permissions=8&scope=bot%20applications.commands")

    @cog_ext.cog_slash(name="초대", description="잼민이봇 초대 링크를 볼수있어요! 많은 서버에 초대해주세요!")
    async def _invite(self, ctx):
      embed = discord.Embed(color=0x000000)
      embed.set_author(name="잼민이봇 초대 링크입니다!")
      embed.add_field(name="잼민이봇", value=f'[초대하기](http://invite.jambot.kro.kr)')
      embed.add_field(name="잼민이봇 서포트서버", value=f'[들어오기](https://discord.gg/B6MjFDjz23)')
      await ctx.send(embed=embed)

    @commands.command(aliases=["server"])
    async def 서버(self, ctx):
      await ctx.send(f"**잼민이봇 서버** \n> https://discord.gg/B6MjFDjz23")


    @commands.command(aliases=["도움말", "도움", "help", "commands"])
    async def 명령어(self, ctx, c:str=None):
      if c is None:
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="명령어", icon_url="https://t.ly/QXEv")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=":point_right: 접두사 (prefix)", value="> 접두사는 `잼민아 `입니다!", inline=False)
        embed.add_field(name=":loudspeaker: 일반", value="> 핑, 안녕, 초대, 서버, 버그", inline=False)
        embed.add_field(name=":speech_balloon: 대화 (chat)", value="너무 많은 관계로 [[잼민이봇 서포트서버]](https://discord.gg/B6MjFDjz23)에 #잼민이봇 명령어 채널에서 확인 부탁드려요", inline=False)
        embed.add_field(name=":video_game: 게임 (game)", value="> 가위바위보, 주사위", inline=False)
        embed.set_footer(text="제작자 : YooMin1122#5973")
      elif c == "접두사":
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="접두사", icon_url="https://t.ly/QXEv")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=":point_right: 접두사", value="> 접두사는 `잼민아 `입니다!", inline=False)
        embed.set_footer(text="제작자 : YooMin1122#5973")
      elif c == "일반":
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="일반", icon_url="https://t.ly/QXEv")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=": loudspeaker: 일반", value="핑, 안녕", inline=False)
        embed.add_field(name="핑", value="> 잼민이봇의 지연시간 확인용 입니다", inline=False)
        embed.add_field(name="안녕", value="> 잼민이 봇과 인사합니다!", inline=False)
        embed.add_field(name="초대", value="> 잼민이 봇을 초대할수있는 링크를 올립니다", inline=False)
        embed.add_field(name="서버", value="> 잼민이 봇 서포트 서버의 초대링크를 올립니다.", inline=False)
        embed.add_field(name="버그", value="> 버그신고는 잼민이봇 서버로!", inline=False)
        embed.set_footer(text="제작자 : YooMin1122#5973")
      elif c == "대화":
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="대화", icon_url="https://t.ly/QXEv")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=":speech_balloon: 대화", value="각 명령어마다 랜덤의 메세지가 나옵니다!", inline=False)
        embed.add_field(name="목록", value="너무 많은 관계로 [[잼민이봇 서포트서버]](https://discord.gg/B6MjFDjz23)에 #잼민이봇 명령어 채널에서 확인 부탁드려요", inline=False)
        embed.set_footer(text="제작자 : YooMin1122#5973")
      elif c == "게임":
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="게임", icon_url="https://t.ly/QXEv")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=":video_game: 게임", value="가위바위보, 주사위", inline=False)
        embed.add_field(name="가위바위보", value="> 안내면 진다 가위바위보!", inline=False)
        embed.add_field(name="주사위", value="> 잼민이 봇과 함께 해서 누가 이길까?", inline=False)
        embed.set_footer(text="제작자 : YooMin1122#5973")
      else: return await ctx.reply(f"`{c}`라는건 업는대")
      await ctx.reply(embed=embed, mention_author=False)


    @commands.command()
    async def 정보(self, ctx):
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="잼민이봇", icon_url="https://t.ly/QXEv")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="개발자", value="> Team DM\n> <@433183785564110848>")
        embed.add_field(name="개발언어", value="> 파이썬(discord.py 1.7.3)")
        embed.add_field(name="사이트", value="> [[홈페이지]](https://jambot.kro.kr)\n> [[Team DM]](http://teamdm.kro.kr)\n> [[깃허브]](https://github.com/yoomin1122/jambot)\n> [[초대하기]](http://invite.jambot.kro.kr) \n> [[서버 참여하기]](https://discord.gg/B6MjFDjz23)", inline=False)
        embed.add_field(name="개발일자", value="> 2021년 12월 17일")
        await ctx.reply(embed=embed, mention_author=False)





    @commands.command()
    async def 테정보(self, ctx):
        korea = "https://koreanbots.dev/api/v2/bots/921424724729397318" # 국내 코로나 발생 동향

        response = requests.get(korea)
        message = response.text
        data = json.loads(message)
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="봇 정보", icon_url="https://t.ly/QXEv")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="투표수", value = format(data["data"]["votes"], ',')+"개")
        embed.add_field(name="서버수", value = format(data["data"]["servers"], ',')+"서버")
        await ctx.reply(embed=embed, mention_author=False)






    @cog_ext.cog_slash(name="정보", description="잼민이봇이 어떤지 알수있어요!")
    async def _info(self, ctx):
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="잼민이봇", icon_url="https://t.ly/QXEv")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="개발자", value="> Team DM\n> <@433183785564110848>")
        embed.add_field(name="개발언어", value="> 파이썬(discord.py 1.7.3)")
        embed.add_field(name="사이트", value="> [[홈페이지]](https://jambot.kro.kr)\n> [[Team DM]](http://teamdm.kro.kr)\n> [[깃허브]](https://github.com/yoomin1122/jambot)\n> [[초대하기]](http://invite.jambot.kro.kr) \n> [[서버 참여하기]](https://discord.gg/B6MjFDjz23)", inline=False)
        embed.add_field(name="개발일자", value="> 2021년 12월 17일")
        await ctx.send(embed=embed)
    @commands.command(aliases=["오류", "버그제보", "bug"])
    async def 버그(self, ctx):
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="잼민이봇 버그 리포트", icon_url="https://t.ly/QXEv")
        embed.add_field(name="연락처", value="YooMin1122#5973")
        embed.add_field(name="이메일", value="ymyh1122@jambot.fun")
        embed.add_field(name="잼민이봇 서포트서버", value="https://discord.gg/B6MjFDjz23\n#건의사항 채널에 부탁드립니다!", inline=False)
        embed.add_field(name="버그 수정(예상)일", value="버그 수정은 당일 아니면 다음날에 바로 수정이 될 예정입니다.(조금 복잡할시 더 길어질수도 있으니 양해 부탁드려요)")
        await ctx.reply(embed=embed, mention_author=False)
    @cog_ext.cog_slash(name="버그", description="버그를 발견하셨나요? 그러면 해당 커멘드로 문의를 해주세요!")
    async def _error(self, ctx):
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="잼민이봇 버그 리포트", icon_url="https://t.ly/QXEv")
        embed.add_field(name="연락처", value="YooMin1122#5973")
        embed.add_field(name="이메일", value="ymyh1122@jambot.fun")
        embed.add_field(name="잼민이봇 서포트서버", value="https://discord.gg/B6MjFDjz23\n#건의사항 채널에 부탁드립니다!", inline=False)
        embed.add_field(name="버그 수정(예상)일", value="버그 수정은 당일 아니면 다음날에 바로 수정이 될 예정입니다.(조금 복잡할시 더 길어질수도 있으니 양해 부탁드려요)")
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Core(bot))

#choice = random.choice(["1", "2", "3", "4])
