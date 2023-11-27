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
    #    Function: addResource(self, ctx, topic, resource_link):
    #    Description: This function is used to add the topic and the link the of resources of this topic
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - topic : used to provide the name of a topic
    #    - resource_link : used to provide the resource topic's link 
    #    Outputs: confirms role deletion
    # -------------------------------------------------------------------------------------------------------
    @commands.command(
        name="addResource",
        help="To use the addresource command, do: $addresource topic_name resource_link <Num> \n \
        ( For example: $addResource Ethical_Software_Engineering, https://github.com/txt/se23/blob/main/docs/ethics.md  )"
    )
    async def addResource(self, ctx, topic, resource_link):
        db.query(
            "INSERT INTO resources (guild_id, topic_name, resource_link) VALUES (%s, %s, %s)",
            (ctx.guild.id,  topic, resource_link),
        )
        await ctx.send(f"Resource successfully added to the topic {topic}")
        return
    @addResource.error
    async def addResource_error(self, ctx, error):
        """Error handling for resource add"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("To use the addresource command, do: $addresource topic_name resource_link <Num> \n \
            ( For example: $addresource Ethical_Software_Engineering, https://github.com/txt/se23/blob/main/docs/ethics.md  )"
            )



async def setup(bot):
    """Adds the file to the bot's cog system"""
    await bot.add_cog(Resource(bot))
   