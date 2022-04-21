import os.path

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random
import time
import datetime
import traceback

#현재 인첸트 신청을 안해서 사용 불가능

class Notice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    @commands.is_owner()
    async def 긴급공지(self, ctx, *, text):
      for guild in self.bot.guilds:
        for channel in guild.text_channels:
          if channel:
              embed = discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
              embed.set_author(name="긴급공지", icon_url=self.bot.user.avatar_url)
              embed.add_field(name=f"긴급공지 입니다.", value=str(text), inline=False)
              embed.set_thumbnail(url=self.bot.user.avatar_url)
              embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
              await ctx.message.add_reaction(emoji="✅")
              await channel.send(embed=embed)
              break

    @commands.command()
    @commands.is_owner()
    async def 공지사항(self, ctx, *, text):
      for guild in self.bot.guilds:
        for channel in guild.text_channels:
          if channel:
            embed = discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
            embed.set_author(name="공지사항", icon_url=self.bot.user.avatar_url)
            embed.add_field(name=f"공지사항 입니다.", value=str(text), inline=False)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=f"Sent by {ctx.message.author}", icon_url=self.bot.user.avatar_url)
            await ctx.message.add_reaction(emoji="✅")
            await channel.send(embed=embed)
            break

    @commands.command()
    @commands.is_owner()
    async def 업데이트(self, ctx, *, text):
      for guild in self.bot.guilds:
        for channel in guild.text_channels:
          if channel.permissions_for(guild.me).send_messages:
            if channel:
              embed = discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
              embed.set_author(name="공지사항", icon_url=self.bot.user.avatar_url)
              embed.add_field(name=f"업데이트 내역 입니다.", value=str(text), inline=False)
              embed.set_thumbnail(url=self.bot.user.avatar_url)
              embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
              await ctx.message.add_reaction(emoji="✅")
              await channel.send(embed=embed)
              break


def setup(bot):
    bot.add_cog(Notice(bot))
