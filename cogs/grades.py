import os
import sys
import discord
from discord.ext import commands
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db

class Grades(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="helloworld", help="helloworld")
    async def hello_world(self, ctx):
        await ctx.send('hello world')
        print("hello world")
    
    @hello_world.error
    async def reset_error(self, ctx, error):
        await ctx.author.send(error)

async def setup(bot):
    await bot.add_cog(Grades(bot))