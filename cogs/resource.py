import os
import sys

import discord
from discord.ext import commands
from discord.utils import get

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db


# -----------------------------------------------------------
# This File contains commands for joining a group, Adding Deleting and retriving resource,
# -----------------------------------------------------------
class Resource(commands.Cog):
    # -----------------------------------------------------------
    # initialize
    # -----------------------------------------------------------
    def __init__(self, bot):
        self.bot = bot

    # -------------------------------------------------------------------------------------------------------
    #    Function: reset(self, ctx)
    #    Description: deletes all group roles in the server
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: confirms role deletion
    # -------------------------------------------------------------------------------------------------------
    @commands.command(
        name="addresource",
        help="To use the addresource command, do: $addresource topic_name topic_resource <Num> \n \
        ( For example: $addresource Ethical_Software_Engineering  )"
    )
    async def addresource(self, ctx, resource, resource_link):
        if resource is None :
            await ctx.send("To add resource, You must provide the resource name")
            return
        if resource_link is None :
            await ctx.send("To add resource, You must provide the resource name")
            return
        
        await ctx.send("Done")
        return

async def setup(bot):
    """Adds the file to the bot's cog system"""
    await bot.add_cog(Resource(bot))
   