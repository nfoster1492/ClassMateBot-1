# This functionality provides various methods to manage grades
# It allows for the inputing of grades, searching of grades, and several
# different calculations based on existing grades in the system
import os
import sys
import discord
import pandas as pd
import requests
from io import StringIO
from discord.ext import commands

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db


class Grades(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="grade", help="get your grade for a specific assignment $grade ASSIGNMENT"
    )
    async def grade(self, ctx, assignmentName: str):
        grade = db.query(
            "SELECT grades.grade FROM grades INNER JOIN assignments ON grades.assignment_id = assignments.id WHERE grades.guild_id = %s AND assignments.assignment_name = %s",
            (ctx.guild.id, assignmentName),
        )

        if not grade:
            await ctx.author.send(f"Grade for {assignmentName} does not exist")
            return

        await ctx.author.send(f"Grade for {assignmentName}: {grade}%")

    @commands.command(
        name="gradebycategory",
        help="get your grade for a specific category $grade CATEGORY",
    )
    async def gradecategory(self, ctx, categoryName: str):
        grades = db.query(
            "SELECT grades.grade FROM grades INNER JOIN assignments ON grades.assignment_id = assignments.id INNER JOIN grade_categories ON assignments.category_id = grade_categories.id WHERE grades.guild_id = %s AND grade_categories.category_name = %s",
            (ctx.guild.id, categoryName),
        )

        if not grades:
            await ctx.author.send(f"Grade for {categoryName} does not exist")
            return

        total = 0
        num = 0

        for grade in grades:
            total = total + grade
            num = num + 1

        average = total / num

        await ctx.author.send(f"Grade for {categoryName}: {average}%")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: categories(self, ctx)
    #    Description: This command lets the user list the categories of grades that are in the system
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: A list of the grade categories in the system
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(
        name="categories", help="display all grading categories and weights $categories"
    )
    async def categories(self, ctx):
        categories = db.query(
            "SELECT category_name, category_weight FROM grade_categories WHERE guild_id = %s ORDER BY category_weight DESC",
            (ctx.guild.id,),
        )

        await ctx.author.send("Category | Weight")
        await ctx.author.send("================")

        for category_name, category_weight in categories:
            await ctx.author.send(f"{category_name} | {category_weight}")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: input_grades(self, ctx, assignmentname)
    #    Description: This command lets the user list the categories of grades that are in the system
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context, including the attached csv file
    #    - assignmentname: the assignment that  grades are being input for
    #    Outputs: A report on how the grades in the system were altered
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(name="inputgrades", help="Insert grades using a csv file")
    async def input_grades(self, ctx, assignmentname: str):
        assignment = db.query(
            "SELECT id FROM assignments WHERE guild_id = %s AND assignment_name = %s",
            (ctx.guild.id, assignmentname),
        )

        if not assignment:
            await ctx.send(f"Assignment with name {assignmentname} does not exist")
            return
        if ctx.message.attachments.len() != 1:
            await ctx.send("Must have exactly one attachment")
            return
        if ctx.message.attachments[0].content_type != "text/csv; charset=utf-8":
            await ctx.send("Invalid filetype")
        attachmenturl = ctx.message.attachments[0].url

        response = requests.get(attachmenturl, timeout=10)
        data = StringIO(response.text)
        df = pd.read_csv(data)
        edited = 0
        added = 0
        for i in range(len(df)):
            name = df.loc[i, "name"]
            grade = df.loc[i, "grade"].item()

            if grade < 0 or grade > 100:
                await ctx.send(
                    f"Invalid grade value for student {name}, skipping entry"
                )
                continue
            student = db.query(
                "SELECT username FROM name_mapping WHERE username = %s", (name,)
            )

            if not student:
                await ctx.send(f"Invalid student name {name}, skipping entry")
                continue
            existing = db.query(
                "SELECT member_name FROM grades WHERE assignment_id = %s AND member_name = %s",
                (assignment[0], name),
            )

            if existing:
                edited += 1
                db.query(
                    "UPDATE grades SET grade = %s WHERE assignment_id = %s AND member_name = %s",
                    (grade, assignment[0], name),
                )
            else:
                added += 1
                db.query(
                    "INSERT INTO grades (guild_id, member_name, assignment_id, grade) VALUES (%s, %s, %s, %s)",
                    (ctx.guild.id, name, assignment[0], grade),
                )
        await ctx.send(
            f"Entered grades for {assignmentname}, {added} new grades entered, {edited} grades edited"
        )

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: input_grades_error(self, ctx, error)
    #    Description: prints error message for inputgrades command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @input_grades.error
    async def input_grades_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the inputgrades command, do: $inputgrades <assignmentname> and add your csv file attachment\n ( For example: $editgradecategory test1 )"
            )
            await ctx.message.delete()
        else:
            await ctx.author.send(error)
            print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: add_grade_category(self, ctx, categoryname, weight)
    #    Description: This command lets the instructor add a grade category, and set the weight for it
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - categoryname: the name of the grade category
    #    - weight: the weight of the category, must be greater than 0
    #    Outputs: Whether or not the add was a success
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="addgradecategory",
        help="add a grading category and weight $addgradecategory NAME WEIGHT",
    )
    async def add_grade_category(self, ctx, categoryname: str, weight: str):
        try:
            categoryweight = float(weight)
        except ValueError:
            await ctx.send("Weight could not be parsed")
            return
        if categoryweight < 0:
            await ctx.sent("Weight must be greater than 0")
            return
        existing = db.query(
            "SELECT id FROM grade_categories WHERE guild_id = %s AND category_name = %s",
            (ctx.guild.id, categoryname),
        )
        if not existing:
            db.query(
                "INSERT INTO grade_categories (guild_id, category_name, category_weight) VALUES (%s, %s, %s)",
                (ctx.guild.id, categoryname, weight),
            )
            await ctx.send(
                f"A grading category has been added for: {categoryname}  with weight: {weight} "
            )
        else:
            await ctx.send("This category has already been added..!!")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: add_grade_category_error(self, ctx, error)
    #    Description: prints error message for addgradecategory command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @add_grade_category.error
    async def add_grade_category_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the gradecategory command, do: $gradecategory <categoryname> <weight> \n ( For example: $gradecategory tests .5 )"
            )
            await ctx.message.delete()
        else:
            await ctx.author.send(error)
            print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: edit_grade_category(self, ctx, categoryname, weight)
    #    Description: This command lets the instructor edit a grade category, and set a new weight for it
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - categoryname: the name of the grade category
    #    - weight: the weight of the category, must be greater than 0
    #    Outputs: Whether or not the edit was a success
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="editgradecategory",
        help="edit a grading category and weight $editgradecategory NAME WEIGHT",
    )
    async def edit_grade_category(self, ctx, categoryname: str, weight: str):
        try:
            categoryweight = float(weight)
        except ValueError:
            await ctx.send("Weight could not be parsed")
            return
        if categoryweight < 0:
            await ctx.sent("Weight must be greater than 0")
            return
        existing = db.query(
            "SELECT id FROM grade_categories WHERE guild_id = %s AND category_name = %s",
            (ctx.guild.id, categoryname),
        )
        if existing:
            db.query(
                "UPDATE grade_categories SET category_weight = %s WHERE id = %s",
                (weight, existing[0]),
            )
            await ctx.send(
                f"{categoryname} category has been updated with weight:{weight} "
            )
        else:
            await ctx.send("This category does not exist")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: edit_grade_category_error(self, ctx, error)
    #    Description: prints error message for editgradecategory command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @edit_grade_category.error
    async def edit_grade_category_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the editgradecategory command, do: $editgradecategory <categoryname> <weight> \n ( For example: $editgradecategory tests .5 )"
            )
            await ctx.message.delete()
        else:
            await ctx.author.send(error)
            print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: delete_grade_category(self, ctx, categoryname)
    #    Description: This command lets the instructor delete a grade category
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - categoryname: the name of the grade category
    #    Outputs: Whether or not the delete was a success
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="deletegradecategory",
        help="delete a grading category $deletegradecategory NAME",
    )
    async def delete_grade_category(self, ctx, categoryname: str):
        existing = db.query(
            "SELECT id FROM grade_categories WHERE guild_id = %s AND category_name = %s",
            (ctx.guild.id, categoryname),
        )
        if existing:
            db.query("DELETE FROM grade_categories WHERE id = %s", (existing[0]))
            await ctx.send(f"{categoryname} category has been deleted ")
        else:
            await ctx.send("This category does not exist")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: delete_grade_category_error(self, ctx, error)
    #    Description: prints error message for deletegradecategory command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @delete_grade_category.error
    async def delete_grade_category_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the deletegradecategory command, do: $deletegradecategory <categoryname> \n ( For example: $deletegradecategory tests)"
            )
            await ctx.message.delete()
        else:
            await ctx.author.send(error)
            print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: grade_report_category(self, ctx)
    #    Description: This command lets the instructor generate a report on the average, low, and high score on each category
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: A breakdown on the performance of each category
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="gradereportcategory",
        help="Report on the classes scores all grade categories",
    )
    async def grade_report_category(self, ctx):
        result = db.query(
            """SELECT category_name, AVG(grade_percent), MAX(grade_percent), MIN(grade_percent) 
                    FROM (SELECT category_name, CAST(grade AS float) / CAST(points AS float) AS grade_percent 
                        FROM grade_categories AS categ JOIN 
                            (SELECT category_id, grade, points 
                                FROM grades AS grades JOIN assignments AS assign ON grades.assignment_id = assign.id) AS grades 
                        ON grades.category_id = categ.id) AS grade_percents 
                GROUP BY category_name"""
        )

        await ctx.author.send("Grade Breakdown by Category")
        for category_name, avg, maxgrade, mingrade in result:
            await ctx.author.send(
                f"{category_name} | Average: {avg:.2f}, Max: {maxgrade:.2f}, Min: {mingrade:.2f}"
            )

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: grade_report_assignment(self, ctx)
    #    Description: This command lets the instructor generate a report on the average, low, and high score on each assignment
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: A breakdown on the performance of each assignment
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="gradereportassignment",
        help="Report on the classes scores all assignments",
    )
    async def grade_report_assignment(self, ctx):
        result = db.query(
            """SELECT assignment_name, AVG(grade_percent), MAX(grade_percent), MIN(grade_percent) 
                FROM (SELECT assignment_name, CAST(grade AS float) / CAST(points AS float) AS grade_percent 
                    FROM grades AS grades JOIN assignments AS assign 
                        ON grades.assignment_id = assign.id) AS assignment_grades 
                GROUP BY assignment_name;"""
        )

        await ctx.author.send("Grade Breakdown by Assignment")
        for assignment_name, avg, maxgrade, mingrade in result:
            await ctx.author.send(
                f"{assignment_name} | Average: {avg:.2f}, Max: {maxgrade:.2f}, Min: {mingrade:.2f}"
            )


# -------------------------------------
# add the file to the bot's cog system
# -------------------------------------
async def setup(bot):
    await bot.add_cog(Grades(bot))
