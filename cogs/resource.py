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
        name="addResource",
        help="To use the addresource command, do: $addresource topic_name resource_link <Num> \n \
        ( For example: $addresource Ethical_Software_Engineering  )"
    )
    async def addResource(self, ctx, topic, resource_link):
        if topic is None :
            await ctx.send("To add resource, You must provide the topic name")
            return
        if resource_link is None :
            await ctx.send("To add resource, You must provide the resource link")
            return
        create_table_query = """
            CREATE TABLE resources (
                guild_id        BIGINT NOT NULL,
                topic_name      VARCHAR NOT NULL,
                resource_link   VARCHAR NOT NULL
            );
            """
        db.query(
            "INSERT INTO resources (guild_id, topic_name, resource_link) VALUES (%s, %s, %s)",
            (ctx.guild.id,  topic, resource_link),
        )
        await ctx.send(f"Resource successfully added to the topic {topic}")
        return
    @addResource.error
    async def addResource_error(self, ctx, error):
        """Error handling for group command"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the group command, do: $group <Num> \n ( For example: $group 0 )"
            )
        else:
            await ctx.author.send(error)
            # await ctx.message.delete()
            print(error)

async def setup(bot):
    """Adds the file to the bot's cog system"""
    await bot.add_cog(Resource(bot))
   