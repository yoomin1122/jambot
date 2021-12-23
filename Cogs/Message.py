import os.path

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random
import time
import pytz
from datetime import tzinfo, datetime
from webserver import keep_alive



class Message(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def 아재개그(self, ctx):
      choice = random.choice(["난잼미니여서 앚애게그 몰르는데", "와ㅇ이 너머지면 킹콩", "시름티비"])
      await ctx.send(choice)

    @commands.command()
    async def 야(self, ctx):
      choice = random.choice(["뭐", "어쩔팁의", "너나한태 반말해?"])
      await ctx.send(choice)

    @commands.command()
    async def 엄준식(self, ctx):
      choice = random.choice(["은사라이따", "엄준식", "엄.", "엄준시근사라이쓸까?"])
      await ctx.send(choice)

    @commands.command()
    async def 정상수(self, ctx):
      choice = random.choice(["정! 상! 수!", "CHECK THIS OUT 나는 정 상 수, 백발백중 하는 명 사 수, 부산진구 유명 가 수, 일취월장 하며 성 장 중", "테이저건팁이"])
      await ctx.send(choice)

    @commands.command()
    async def 잼민아(self, ctx):
      choice = random.choice(["나잼민이않인데 나 고든학교 6학년 1찐임 ㅋㅋㄹㅃㅃ", "어쩔티비", "잼민이않인데"])
      await ctx.send(choice)

    @commands.command(aliases=["옵치"])
    async def 오버워치(self, ctx):
      choice = random.choice(["옵어워치 갠지 류승룡기모ㅈ지", "ㅇㅏ 옵어어치 망갬인대;;;; 그걸 눅아하냐", "망겜티비", "비싸니까 복돌해얍지"])
      await ctx.send(choice)
    
    @commands.command(aliases=["마크"])
    async def 마인크래프트(self, ctx):
      choice = random.choice(["와 마크 앗시는군아!", "돈이업쓰니깐 복돌다운", "히로빈게멋져 ㄷㄷ"])
      await ctx.send(choice)

    @commands.command(aliases=["센즈", "언더테일"])
    async def 샌즈(self, ctx):
      choice = random.choice(["와 센즈 아시는군아! 진.짜.겁.나.어.렵.습.니.다", "샌즈!", "언더테일 아시는구나! 혹시 모르시는분들에 대해 설명해드립니다 샌즈랑 언더테일의 세가지 엔딩루트중 몰살엔딩의 최종보스로 진.짜.겁.나.어.렵.습.니.다 공격은 전부다 회피하고 만피가 92인데 샌즈의 공격은 1초당 60이 다는데다가 독뎀까지 추가로 붙어있습니다.. 하지만 이러면 절대로 게임을 깰 수 가없으니 제작진이 치명적인 약점을 만들었죠. 샌즈의 치명적인 약점이 바로 지친다는것입니다. 패턴들을 다 견디고나면 지쳐서 자신의 턴을 유지한채로 잠에듭니다. 하지만 잠이들었을때 창을옮겨서 공격을 시도하고 샌즈는 1차공격은 피하지만 그 후에 바로날아오는 2차 공격을 맞고 죽습니다.", "센즈몰으는 사람이 있냐? ㅋㅋㄹㅃㅃ", "돈업서서 언더테일모탐 복돌다운하면 받이러쓰걸려", "https://ww.namu.la/s/fa2e540dae361211e361e242679ff2c15a4f73a32be6827ed0fa0571f88817deb5ae1de9923a7e8fa29e91264d226b50537404917a47506c040054e8d4a41b47c44a4e4a3ef0fe55e86c9a1d981f29b80ae197922e1d4fa3a9a8e2a44c40ca03"])
      await ctx.send(choice)

    @commands.command()
    async def 따라해(self, ctx, *, text):
      await ctx.send(text)

def setup(bot):
    bot.add_cog(Message(bot))
