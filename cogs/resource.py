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
    #    Outputs: It will add a new rosource under a topic
    # -------------------------------------------------------------------------------------------------------
    @commands.command(
        name="addResource",
        help="To use the addresource command, do: $addresource <topic_name> <resource_link>  \n \
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


    # -------------------------------------------------------------------------------------------------------
    #    Function: addResource(self, ctx):
    #    Description: This function is used to get the resources
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: Return the list of resources
    # -------------------------------------------------------------------------------------------------------
    @commands.command(
        name="getResource",
        help="To use the getResource command, do: $getResource"
    )
    async def getResource(self, ctx):
        result = db.query("SELECT * FROM resources WHERE guild_id = %s", (ctx.guild.id,))

        if not result:
            await ctx.send("No resources found.")
            return
        embed = discord.Embed(title="List of Resources", color=0x00ff00) 

        for row in result:
            topic = row[1]
            resource_link = row[2]
            embed.add_field(name=f"Topic: {topic}", value=f"Resource Link: {resource_link}", inline=False)
        await ctx.send(embed=embed)
        return

    @getResource.error
    async def getResource_error(self, ctx, error):
        """Error handling for getting resource"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send0("To use the getResource command, do: $getResource")


async def setup(bot):
    """Adds the file to the bot's cog system"""
    await bot.add_cog(Resource(bot))
   