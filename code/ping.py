import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(Helpful(bot))

class Helpful(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! My ping currently is {round(self.bot.latency * 1000)}ms")


