# Copyright (c) 2023 JacobBow
import os
import importlib
from discord.ext import commands


# ----------------------------------------------------------------------------------------------
# Returns the ping of the bot, useful for testing bot lag and as a simple functionality command
# ----------------------------------------------------------------------------------------------
class Helper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # -------------------------------------------------------------------------------------------------------
    #    Function: getCommands(self, ctx)
    #    Description: all of the commands that the bot has
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: prints the list of commands the bot has access to
    # -------------------------------------------------------------------------------------------------------
    @commands.command(
        name="showCommands", help="List all the commands the bot has access to"
    )
    async def showCommands(self, ctx):
        """Prints all the commands that the bot has"""
        # Get all of the commands
        deny_access_commands = ["helpful3", "jishaku"]
        all_commands = []
        for cog_name, cog in self.bot.cogs.items():
            for command in cog.get_commands():
                if str(command) not in deny_access_commands:
                    all_commands.append(command.name)

        await ctx.send(
            "```To run any of the listed commands run '$command_name'\n"
            "To get help with any of the commands run '$help command_name or $help to list the instructions for all commands'```"
        )
        await ctx.send(f"```All commands: {', '.join(all_commands)}```")

    # -------------------------------------------------------------------------------------------------------
    #    Function: getCategories(self, ctx)
    #    Description: all of the commands that the bot has
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: prints the list of categories for commands
    # -------------------------------------------------------------------------------------------------------
    @commands.command(
        name="showCommandCategories", help="List all the commands the bot has access to"
    )
    async def showCommandCategories(self, ctx):
        """Print all the categories for the commands"""
        all_categories = []
        for cog_name, cog in self.bot.cogs.items():
            if cog_name not in all_categories:
                all_categories.append(cog_name)

        new_line = "\n"
        await ctx.send(
            "```To learn more about these categories run $help category_name```"
        )
        await ctx.send(
            f"```Command Categories:\n{f'{new_line}'.join(all_categories)}```"
        )


# -------------------------------------
# add the file to the bot's cog system
# -------------------------------------
async def setup(bot):
    """Adds the file to the bot's cog system"""
    await bot.add_cog(Helper(bot))
