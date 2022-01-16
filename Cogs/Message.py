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
    async def 바보(self, ctx):
      choice = random.choice(["나밥오않인대;", "않인데", "너도바보임", "아님티비", "응 아니야"])
      await ctx.send(choice)

    @commands.command(aliases=["뭐해?"])
    async def 뭐해(self, ctx):
      choice = random.choice(["언더태일한느중인대외", "마크한은중", "유튜브보는대왜", "안알려줌티비", "걍잇음", "유투부잠뜰보는대외"])
      await ctx.send(choice)

    @commands.command()
    async def 유민(self, ctx):
      choice = random.choice(["닉넴 : 유민 \n 나이 : 15 \n 경력 : 잼민이봇, 재깨봇", "나만든사람임"])
      await ctx.send(choice)

    @commands.command(aliases=["민초"])
    async def 민트초코(self, ctx):
      choice = random.choice(["민초맞업는대;;", "와 치약 아시는구나!", "시름티비"])
      await ctx.send(choice)

    @commands.command(aliases=["유튭", "youtube"])
    async def 유튜브(self, ctx):
      choice = random.choice(["센즈검섹해야댐", "마플마크센즈전모참음", "브롤스타즈윹ㅠ브보고싶다", "잼민tv 구독가조아요부탁들어요"])
      await ctx.send(choice)

    @commands.command()
    async def 스티브(self, ctx):
      choice = random.choice(["스티브", "https://t.ly/D2RL", "슽티브가 무서어지면 히로비니대요"])
      await ctx.send(choice)

    @commands.command()
    async def 어벤져스(self, ctx):
      choice = random.choice(["어샘블!", "아이언맨 머싰음!", "아샌즈도 어밴져스 들어갈수이씀!"])
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
      choice = random.choice(["정! 상! 수!", "CHECK THIS OUT 나는 정 솽~ 수", "테이저건팁이"])
      await ctx.send(choice)

    @commands.command(aliases=["잼민이"])
    async def 잼민아(self, ctx):
      choice = random.choice(["나잼민이않인데 나 고든학교 6학년 1찐임 ㅋㅋㄹㅃㅃ", "어쩔티비", "잼민이않인데"])
      await ctx.send(choice)

    @commands.command(aliases=["옵치"])
    async def 오버워치(self, ctx):
      choice = random.choice(["옵어워치 갠지 류승룡기모ㅈ지", "ㅇㅏ 옵어어치 망갬인대;;;; 그걸 눅아하냐", "망겜티비", "비싸니까 복돌해얍지"])
      await ctx.send(choice)
    
    @commands.command(aliases=["마크"])
    async def 마인크래프트(self, ctx):
      choice = random.choice(["와 마크 앗시는군아!", "돈이업쓰니깐 복돌다운", "히로빈게멋져 ㄷㄷ", "히로비네괘담아라요? 극어 개무서움"])
      await ctx.send(choice)

    @commands.command(aliases=["센즈", "언더테일"])
    async def 샌즈(self, ctx):
      choice = random.choice(["와 센즈 아시는군아! 진.짜.겁.나.어.렵.습.니.다", "샌즈!", "언더테일 아시는구나! 혹시 모르시는분들에 대해 설명해드립니다 샌즈랑 언더테일의 세가지 엔딩루트중 몰살엔딩의 최종보스로 진.짜.겁.나.어.렵.습.니.다 공격은 전부다 회피하고 만피가 92인데 샌즈의 공격은 1초당 60이 다는데다가 독뎀까지 추가로 붙어있습니다.. 하지만 이러면 절대로 게임을 깰 수 가없으니 제작진이 치명적인 약점을 만들었죠. 샌즈의 치명적인 약점이 바로 지친다는것입니다. 패턴들을 다 견디고나면 지쳐서 자신의 턴을 유지한채로 잠에듭니다. 하지만 잠이들었을때 창을옮겨서 공격을 시도하고 샌즈는 1차공격은 피하지만 그 후에 바로날아오는 2차 공격을 맞고 죽습니다.", "센즈몰으는 사람이 있냐? ㅋㅋㄹㅃㅃ", "돈업서서 언더테일모탐 복돌다운하면 받이러쓰걸려", "https://i.imgur.com/OrQnRPR.jpg"])
      await ctx.send(choice)

    @commands.command()
    async def 따라해(self, ctx, *, text):
      await ctx.send(text)

    @commands.command(aliases=["디코"])
    async def 디스코드(self, ctx):
      choice = random.choice(["디슷코드애는외 샌즈업음?", "디스콛으팁이", "애드리랑통화 할떄쓴은거"])
      await ctx.send(choice)

    @commands.command()
    async def 어쩔티비(self, ctx):
      choice = random.choice(["어쩔센즈팁이", "저쩔티비", "ㅇㅉㅌㅂ!", "ㅇㅉㄺ", "어쩔냉장고", "안물티비 안궁티비~", "어쩔 콩순이 컴퓨터"])
      await ctx.send(choice)

    @commands.command(aliases=["ㅋ", "ㅋㅋㅋ", "ㅋㅋㅋㅋ", "ㅋㅋㅋㅋㅋ", "ㅋㅋㅋㅋㅋㅋ", "ㅋㅋㅋㅋㅋㅋㅋ", "ㅋㅋㅋㅋㅋㅋㅋㅋ", "ㅋㅋㅋㅋㅋㅋㅋㅋㅋ", "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ"])
    async def ㅋㅋ(self, ctx):
      choice = random.choice(["멀우서", "멀처우서!", "안웃김티비"])
      await ctx.send(choice)

    @commands.command(aliases=["쇼미"])
    async def 쇼미더머니(self, ctx):
      choice = random.choice(["조강일못참지 ㅋㅋㄹㅃㅂ", "어. 느새. 부터 힙! 하븐 안멋쪄!", "쇼미 모참지 ㅋㅋㄹㅃㅃ 게꿀젬임"])
      await ctx.send(choice)

    @commands.command(aliases=["롤"])
    async def 리그오브레전드(self, ctx):
      choice = random.choice(["내장레히망 패이커임", "롤꿀잼팁이", "롤 탑티모모참지 ㅋㅋㄹㅃㅃ"])
      await ctx.send(choice)

    @commands.command()
    async def 회전목마(self, ctx):
      choice = random.choice(["빙빙도라가는 해전목마처럼 영워니 개속 댈거처럼!!", "해전목마 노래 개조음 ㅋㅋㄹ", "해전목마 모참지 "])
      await ctx.send(choice)

    @commands.command()
    async def 리무진(self, ctx):
      choice = random.choice(["까만리무진을 봄며 꾸믈키어찌", "언잰가는 나도저걸 가께됄거야", "비오리무진개조음 ㄹㅇㅋㅋㄹㅃㅃ"])
      await ctx.send(choice)

    @commands.command(aliases=["내이버", "naver"])
    async def 네이버(self, ctx):
      choice = random.choice(["내이버에치면 다나옴", "검열이오ㅔㄹ케심해 뺴얘얘얘ㅒ얘얘얘ㅒ얭", "구글볻아 내이버지"])
      await ctx.send(choice)

    @commands.command()
    async def ㅋㅋㄹㅃㅃ(self, ctx):
      choice = random.choice(["ㅋㅋㄹㅃㅃ", "ㄹㅇㅋㅋㄹㅃㅃ", "찬구모참지 ㅋㅋㄹ", "세게간채강자드레 싸우미다"])
      await ctx.send(choice)

    @commands.command()
    async def 니얼굴(self, ctx):
      choice = random.choice(["니얼굴 팁이", "응 니얼굴", "내얼굴차은운대ㅋㅋㄹㅃㅃ**[이 발언은 제작자와 무관한 사실입니다]**"])
      await ctx.send(choice)

    @commands.command()
    async def 수학학원(self, ctx):
      choice = random.choice(["수학하건 시러!", "수학하건 지건", "하건가기싫어 다ㅏ 사라져쓰면 조케따"])
      await ctx.send(choice)

    @commands.command(aliases=["로블"])
    async def 로블록스(self, ctx):
      choice = random.choice(["로블모참지 ", "아로블하느랴바쁨", "벧으워즈모참짘ㅋ", "아로블로 오징어개임해야뎀 ㅋ"])
      await ctx.send(choice)

    @commands.command()
    async def 지건(self, ctx):
      choice = random.choice(["지건 ", "https://i.imgur.com/OBuzCVb.png", "벧으워즈모참짘ㅋ", "아로블로 오징어개임해야뎀 ㅋ"])
      await ctx.send(choice)

    @commands.command()
    async def 맞춤법(self, ctx):
      choice = random.choice(["나 마춤뻡잘지킴 ㅋ", "마춤뻡그거 글어캐 하는거않인대 왜가 아니라 외에요;", "촏잉보다 마춤법몰으시내 ㅌㅋ", "돼가 아니라 되에요 ㅋ"])
      await ctx.send(choice)

    @commands.command(name="2022", aliases=["2022년", "이천이십이년", "이공이이"])
    async def _2022년(self, ctx):
      choice = random.choice(["https://i.ibb.co/PMX6dFK/2022.png", "세해복마니바드새요.", "난평셍 9살임 ㅋ", "새뱃돈주새요ㅋㅋㄹㅃㅃ", "https://i.ibb.co/PMX6dFK/2022.png"])
      await ctx.send(choice)

    @commands.command(aliases=["ㄲㅈ"])
    async def 꺼져(self, ctx):
      choice = random.choice(["너나껒여", "꺼져팁의", "응않이야", "`ㅗㅗ`"])
      await ctx.send(choice)

    @commands.command(aliases=["한국디스코드리스트"])
    async def 한디리(self, ctx): 
      await ctx.send("업데이트중..")

    @commands.command(name="ㅋㅋㄹㅃㅃ", aliases=["크크루삥뽕"])
    async def _ㅋㅋㄹㅃㅃ(self, ctx):
      choice = random.choice(["ㅋㅋㄹㅃㅃ", "극크루삥뽕", "ㅋㅋㄹㅃㅃㅌㅂ"]) 
      await ctx.send(choice)

    @commands.command()
    async def 깝치지마(self, ctx): 
      choice = random.choice(["ㅇㅉㅌㅂ ㅈㅉㅌㅂ", "너나깦치지마팁의", "응아니야 팁의"]) 
      await ctx.send(choice)

    @commands.command(aliases=["세영이"])
    async def 세영(self, ctx): 
      choice = random.choice(["새영이보단내가 더조치 ㅋ", "젬미니보시 채곤ㄷ... 읍읍((퍽퍽", "새영팁의 노잼"]) 
      await ctx.send(choice)
    
    @commands.command()
    async def 재깨봇(self, ctx):
      choice = random.choice(["제께보시 머여떠라?", "내가 채고임 ㅋㅋㄹㅃㅃ"])
      await ctx.send(choice)
    
    @commands.command()
    async def 크시(self, ctx):
      choice = random.choice(["큿이는아직도 대게유명헤 ㄷㄷ", "큿이보다 잼보시더유명헤질꺼임", "ㅋㅅㅌㅂ"])
      await ctx.send(choice)
    
    @commands.command()
    async def 배그(self, ctx):
      choice = random.choice(["베그무료모참찌 ㅋㅋㄹㅃㅃ", "아나 ~~모바일~~베그 게고순대 ㅋㅋ", "재가 케리헤드림 ㅋ"])
      await ctx.send(choice)

    @commands.command(aliases=["훈수"])
    async def 훈수질(self, ctx):
      choice = random.choice(["오렛도ㅇ앉자면 펜텀이돌아다녀요 ", "않이 다이아몬드는 y-53애서잘나ㅇ ㅘ요.", "극어 글어캐하는거않인대;;"])
      await ctx.send(choice)

    @commands.command()
    async def 뒤질래(self, ctx):
      choice = random.choice(["응않이야팁의", "너나주거티비", "~~ㅗㅗㅗ~~", "엊쩔팁의", "나싸움1짱젬민이다 다덤버바라내가발라주마"])
      await ctx.send(choice)

    @commands.command()
    async def 김블루(self, ctx):
      choice = random.choice(["김불룩팁의!", "그사람헥아닌가", "개꿀젬틥이 진짜제미씀", "아김불루본명 머임 ㅋㅋㄹㅃㅃㅌㅂ"])
      await ctx.send(choice)

    @commands.command()
    async def 연다(self, ctx):
      choice = random.choice(["머ㄱ방ㅇ유투버", "~~간첩틥이~~", "배그게잘함 ㄷㄷ", "연두섹판다팁이"])
      await ctx.send(choice)

    @commands.command()
    async def 군림보(self, ctx):
      choice = random.choice(["돼장", "백으유투버안인가", "엄몽어스 유투버인가", "롣으호그팁의"])
      await ctx.send(choice)

    @commands.command()
    async def 브롤스타즈(self, ctx):
      choice = random.choice(["브롤게꾸ㄹ젬 팁의", "브롤팁이", "아나클오마틱다이쓰ㅁ!", "나브롤렝커임ㅋ"])
      await ctx.send(choice)

    @commands.command(aliases=["연애운"])
    async def 연애(self, ctx):
      love = random.randint(5, 101)
      if (5 >= love):
        await ctx.send(f"사라ㅁ임? 연에우니 {love}%임 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
      elif (10 >= love):
        await ctx.send(f"님연에운 {love}%임 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
      elif (50 >= love):
        await ctx.send(f"님 연에못할듯ㅋ 연애운이{love}%이며ㄴㅋㅋㅋㅋㅋㅋ")
      elif (80 >= love):
        await ctx.send(f"평범한내 연에우니{love}%정도면 머..")
      elif (90 >= love):
        await ctx.send(f"와 연에우니{love}%정도내")
      elif (100 >= love):
        await ctx.send(f"연에운니{love}%개높내 ㄷㄷ")
      elif (100 == love):
        await ctx.send(f"신이애요? 연에우니{love}%정라니엄청나내 ㄷㄷㄷㄷ")

    @commands.command()
    async def 잉앗살라말리이쿰(self, ctx):
      choice = random.choice(["잉잉이이 아쌀라말라이ㅋㅜㅁ", "아쌀라말라이큼티ㅡ비"])
      await ctx.send(choice)



#https://i.ibb.co/PMX6dFK/2022.png
def setup(bot):
    bot.add_cog(Message(bot))
