import os
import sys
import discord
from discord.ext import commands
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db

class Grades(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="grade", help="get your grade for a specific assignment $grade ASSIGNMENT")
    async def grade(self, ctx, assignmentName: str):

        grade = db.query(
            "SELECT g.grade FROM grades g INNER JOIN assignments a ON g.assignment_id = a.assignment_id WHERE guild_id = %s AND a.assignment_name = %s", 
            (ctx.guild.id, assignmentName)
        )

        if not grade:
            await ctx.send("Grade for {assignmentName} does not exist")

        await ctx.send("Grade for {assignmentName}: {grade}%")

    @commands.command(name="gradebycategory", help="get your grade for a specific category $grade CATEGORY")
    async def grade(self, ctx, categoryName: str):

        grades = db.query(
            "SELECT g.grade FROM grades g INNER JOIN assignments a ON g.assignment_id = a.assignment_id INNER JOIN categories c ON a.assignment_id WHERE guild_id = %s AND c.category_name = %s", 
            (ctx.guild.id, categoryName)
        )

        if not grades:
            await ctx.send("Grade for {categoryName} does not exist")

        total = 0
        num = 0

        for grade in grades:
            total = total + grade
            num = num + 1

        average = total/num

        await ctx.send("Grade for {categoryName}: {average}%")

    @commands.command(name="gradetopasscategory", help="get your required grade on the next assignment to maintain a certain grade in a category $gradetopass CATEGORY DESIRED_GRADE")
    async def grade(self, ctx, categoryName: str, desiredGrade: str):

        try:
            desiredGrade = int(desiredGrade)
        except:
            await ctx.send("Grade could not be parsed")
            return

        grades = db.query(
            "SELECT g.grade FROM grades g INNER JOIN assignments a ON g.assignment_id = a.assignment_id INNER JOIN categories c ON a.assignment_id WHERE guild_id = %s AND c.category_name = %s", 
            (ctx.guild.id, categoryName)
        )

        if not grades:
            await ctx.send("Grade for {categoryName} does not exist")

        total = 0
        num = 0

        for grade in grades:
            total = total + grade
            num = num + 1

        totalNeeded = desiredGrade * (num + 1)
        gradeNeeded = totalNeeded - total
        if gradeNeeded > 0:
            await ctx.send("Next assignment must be at least {gradeNeeded}% to maintain a {desiredGrade}% in {categoryName}")
        else:
            await ctx.send("You can get any grade on the next assignment and maintain a {desiredGrade}% in {categoryName}")

    @commands.command(name="categories", help="display all grading categories and weights $categories")
    async def categories(self, ctx):

        categories = db.query(
            'SELECT category_name, category_weight FROM grade_categories WHERE guild_id = %s ORDER BY category_weight DESC',
            (ctx.guild.id,)
        )


        await ctx.send("Category | Weight")
        await ctx.send("================")

        for category_name, category_weight in categories:
            await ctx.send(f"{category_name} | {category_weight}")
        
    @commands.command(name="addgradecategory", help="add a grading category and weight $addgradecategory NAME WEIGHT")
    async def add_grade_category(self, ctx, categoryname: str, weight: str):
        try:
            categoryweight = float(weight)
        except ValueError:
            await ctx.send("Weight could not be parsed")
            return
        existing = db.query(
            'SELECT id FROM grade_categories WHERE guild_id = %s AND category_name = %s',
            (ctx.guild.id, categoryname)
        )
        if not existing:
            db.query(
                'INSERT INTO grade_categories (guild_id, category_name, category_weight) VALUES (%s, %s, %s)',
                (ctx.guild.id, categoryname, weight)
            )
            await ctx.send(
                f"A grading category has been added for: {categoryname}  with weight: {weight} ")
        else:
            await ctx.send("This category has already been added..!!")


    @commands.command(name="editgradecategory", help="edit a grading category and weight $editgradecategory NAME WEIGHT")
    async def edit_grade_category(self, ctx, categoryname: str, weight: str):
        try:
            categoryweight = float(weight)
        except ValueError:
            await ctx.send("Weight could not be parsed")
            return
        existing = db.query(
            'SELECT id FROM grade_categories WHERE guild_id = %s AND category_name = %s',
            (ctx.guild.id, categoryname)
        )
        if existing:
            db.query(
                'UPDATE grade_categories SET category_weight = %s WHERE id = %s',
                (weight, existing[0])
            )
            await ctx.send(
                f"{categoryname} category has been updated with weight:{weight} ")
        else:
            await ctx.send("This category does not exist")

    @commands.command(name="deletegradecategory", help="delete a grading category $deletegradecategory NAME")
    async def delete_grade_category(self, ctx, categoryname: str):
        existing = db.query(
            'SELECT id FROM grade_categories WHERE guild_id = %s AND category_name = %s',
            (ctx.guild.id, categoryname)
        )
        if existing:
            db.query(
                'DELETE FROM grade_categories WHERE id = %s',
                (existing[0])
            )
            await ctx.send(
                f"{categoryname} category has been deleted ")
        else:
            await ctx.send("This category does not exist")
    
    @add_grade_category.error
    async def add_grade_category_error(self, ctx, error):
        await ctx.author.send(error)

    @edit_grade_category.error
    async def edit_grade_category_error(self, ctx, error):
        await ctx.author.send(error)
    
    @delete_grade_category.error
    async def delete_grade_category_error(self, ctx, error):
        await ctx.author.send(error)

async def setup(bot):
    await bot.add_cog(Grades(bot))