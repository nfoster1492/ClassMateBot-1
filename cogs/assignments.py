import os
import sys
import discord
from discord.ext import commands
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db

class Assignments(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="addassignment", help="add a grading assignment and points $addassignment NAME CATEGORY POINTS")
    async def add_assignment(self, ctx, assignmentname: str, categoryname: str, points: str):
        try:
            assignmentpoints = int(points)
        except ValueError:
            await ctx.send("Points could not be parsed")
            return
        
        category = db.query(
            'SELECT id FROM grade_categories WHERE guild_id = %s AND category_name = %s',
            (ctx.guild.id, categoryname)
        )

        if not category:
            await ctx.send(f"Category with name {categoryname} does not exist");
            return
        
        if assignmentpoints < 0:
            await ctx.send(f"Assignment points must be greater than zero");
            return
        
        existing = db.query(
            'SELECT id FROM assignments WHERE guild_id = %s AND assignment_name = %s',
            (ctx.guild.id, assignmentname)
        )

        if not existing:
            db.query(
                'INSERT INTO assignments (guild_id, category_id, assignment_name, points) VALUES (%s, %s, %s, %s)',
                (ctx.guild.id, category[0], assignmentname, points)
            )
            await ctx.send(
                f"A grading assignment has been added for: {assignmentname}  with points: {points} and category: {categoryname}")
        else:
            await ctx.send("This assignment has already been added..!!")


    @commands.command(name="editassignment", help="edit a grading assignment and points $editassignment NAME CATEGORY POINTS")
    async def edit_assignment(self, ctx, assignmentname: str, categoryname: str, points: str):
        try:
            assignmentpoints = int(points)
        except ValueError:
            await ctx.send("Points could not be parsed")
            return
        
        category = db.query(
            'SELECT id FROM grade_categories WHERE guild_id = %s AND category_name = %s',
            (ctx.guild.id, categoryname)
        )

        if not category:
            await ctx.send(f"Category with name {categoryname} does not exist");
            return
        
        if assignmentpoints < 0:
            await ctx.send(f"Assignment points must be greater than zero");
            return
        
        existing = db.query(
            'SELECT id FROM assignments WHERE guild_id = %s AND assignment_name = %s',
            (ctx.guild.id, assignmentname)
        )
        if existing:
            db.query(
                'UPDATE assignments SET category_id = %s, points = %s WHERE id = %s',
                (category[0], points, existing[0])
            )
            await ctx.send(
                f"{assignmentname} assignment has been updated with points:{points} and category: {categoryname}")
        else:
            await ctx.send("This assignment does not exist")

    @commands.command(name="deleteassignment", help="delete a grading assignment $deleteassignment NAME")
    async def delete_assignment(self, ctx, assignmentname: str):
        existing = db.query(
            'SELECT id FROM assignments WHERE guild_id = %s AND assignment_name = %s',
            (ctx.guild.id, assignmentname)
        )
        if existing:
            db.query(
                'DELETE FROM assignments WHERE id = %s',
                (existing[0])
            )
            await ctx.send(
                f"{assignmentname} assignment has been deleted ")
        else:
            await ctx.send("This assignment does not exist")
    
    @add_assignment.error
    async def add_assignment_error(self, ctx, error):
        await ctx.author.send(error)

    @edit_assignment.error
    async def edit_assignment_error(self, ctx, error):
        await ctx.author.send(error)
    
    @delete_assignment.error
    async def delete_assignment_error(self, ctx, error):
        await ctx.author.send(error)

async def setup(bot):
    await bot.add_cog(Assignments(bot))