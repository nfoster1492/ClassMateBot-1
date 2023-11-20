# Copyright (c) 2023 nfoster1492
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

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: grade(self, ctx, assignmentName)
    #    Description: This command lets a student get their grade for a certain assignment
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - assignmentName: the name of the desired assignment
    #    Outputs:
    #    - Grade of the provided assignment
    #    Aliases:
    #    - getGrade
    #    - assignmentGrade
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(
        name="grade",
        aliases=["getGrade, assignmentGrade"],
        help="get your grade for a specific assignment $grade ASSIGNMENT",
    )
    async def grade(
        self,
        ctx,
        assignmentName: str = commands.parameter(
            description="Name of assignment to get the grade for"
        ),
    ):
        """Lets a student get their grade for a certain assignment"""
        memberName = ctx.author.name

        grade = db.query(
            "SELECT grades.grade FROM grades INNER JOIN assignments ON grades.assignment_id = assignments.id WHERE grades.guild_id = %s AND grades.member_name = %s AND assignments.assignment_name = %s",
            (ctx.guild.id, memberName, assignmentName),
        )

        points = db.query(
            "SELECT assignments.points FROM assignments WHERE assignments.guild_id = %s AND assignments.assignment_name = %s",
            (ctx.guild.id, assignmentName),
        )

        if not grade:
            await ctx.author.send(f"Grade for {assignmentName} does not exist")
            return

        if not points:
            await ctx.author.send(f"{assignmentName} does not exist")
            return

        await ctx.author.send(
            f"Grade for {assignmentName}: {grade[0][0]}%, worth {points[0][0]} points"
        )

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: grade_error(self, ctx, error)
    #    Description: prints error message for grade command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @grade.error
    async def grade_error(self, ctx, error):
        """Error handling of grade function"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the grade command, do: $grade <assignmentname>\n ( For example: $grade test1 )"
            )
            await ctx.message.delete()
        else:
            await ctx.author.send(error)
            print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: gradeByCategory(self, ctx, categoryName)
    #    Description: This command lets a student get their average grade for a certain category
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - categoryName: the name of the desired category
    #    Outputs:
    #    - Average grade of all the assignments in the provided category, accounting for assignment point values
    #    Aliases:
    #    - categoryGrade
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(
        name="gradeByCategory",
        aliases=["categoryGrade"],
        help="get your grade for a specific category $gradebycategory CATEGORY",
    )
    async def gradebycategory(
        self,
        ctx,
        categoryName: str = commands.parameter(
            description="Name of category to get your grades from"
        ),
    ):
        """Lets a student get their grade for a specific grade category"""
        memberName = ctx.author.name

        grades = db.query(
            "SELECT grades.grade FROM grades INNER JOIN assignments ON grades.assignment_id = assignments.id INNER JOIN grade_categories ON assignments.category_id = grade_categories.id WHERE grades.guild_id = %s AND grades.member_name = %s AND grade_categories.category_name = %s ORDER BY grades.assignment_id",
            (ctx.guild.id, memberName, categoryName),
        )

        points = db.query(
            "SELECT assignments.points FROM assignments INNER JOIN grade_categories ON assignments.category_id = grade_categories.id WHERE assignments.guild_id = %s AND grade_categories.category_name = %s ORDER BY assignments.id",
            (ctx.guild.id, categoryName),
        )

        if not grades:
            await ctx.author.send(f"Grades for {categoryName} do not exist")
            return

        if not points:
            await ctx.author.send(f"Assignments for {categoryName} do not exist")
            return

        actualGrades = []
        for grade in grades:
            actualGrades.append(grade[0])

        actualPoints = []
        for point in points:
            actualPoints.append(point[0])

        total = 0
        pointsTotal = 0

        for i in range(len(actualGrades)):
            total = total + (actualGrades[i] / 100) * actualPoints[i]
            pointsTotal = pointsTotal + actualPoints[i]

        average = (total / pointsTotal) * 100

        await ctx.author.send(f"Grade for {categoryName}: {average:.2f}%")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: gradebycategory_error(self, ctx, error)
    #    Description: prints error message for gradeByCategory command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @gradebycategory.error
    async def gradebycategory_error(self, ctx, error):
        """Error handling of gradeByCategory function"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the gradeByCategory command, do: $gradeByCategory <categoryname>\n ( For example: $gradeByCategory tests )"
            )
            await ctx.message.delete()
        else:
            await ctx.author.send(error)
            print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: gradeforclass(self, ctx)
    #    Description: This command lets a student get their average grade for the whole class
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs:
    #    - Average grade of all the assignments in the class, weighted by category, accounting for assignment point values
    #    Aliases:
    #    - classGrade
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(
        name="gradeForClass",
        aliases=["classGrade"],
        help="get your grade for the whole class $gradeforclass",
    )
    async def gradeforclass(self, ctx):
        """Lets a student get their overall average grade for the class"""
        memberName = ctx.author.name

        categories = db.query(
            "SELECT category_name, category_weight FROM grade_categories WHERE guild_id = %s ORDER BY category_weight DESC",
            (ctx.guild.id,),
        )

        classTotal = 0

        for category_name, category_weight in categories:
            grades = db.query(
                "SELECT grades.grade FROM grades INNER JOIN assignments ON grades.assignment_id = assignments.id INNER JOIN grade_categories ON assignments.category_id = grade_categories.id WHERE grades.guild_id = %s AND grades.member_name = %s AND grade_categories.category_name = %s ORDER BY grades.assignment_id",
                (ctx.guild.id, memberName, category_name),
            )

            points = db.query(
                "SELECT assignments.points FROM assignments INNER JOIN grade_categories ON assignments.category_id = grade_categories.id WHERE assignments.guild_id = %s AND grade_categories.category_name = %s ORDER BY assignments.id",
                (ctx.guild.id, category_name),
            )

            if not grades:
                await ctx.author.send(f"Grades for {category_name} do not exist")
                return

            if not points:
                await ctx.author.send(f"Assignments for {category_name} do not exist")
                return

            actualGrades = []
            for grade in grades:
                actualGrades.append(grade[0])

            actualPoints = []
            for point in points:
                actualPoints.append(point[0])

            total = 0
            pointsTotal = 0

            for i in range(len(actualGrades)):
                total = total + (actualGrades[i] / 100) * actualPoints[i]
                pointsTotal = pointsTotal + actualPoints[i]

            average = (total / pointsTotal) * 100

            classTotal = classTotal + (average * float(category_weight))

        await ctx.author.send(f"Grade for class: {classTotal:.2f}%")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: gradeforclass_error(self, ctx, error)
    #    Description: prints error message for gradeForClass command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @gradeforclass.error
    async def gradeforclass_error(self, ctx, error):
        """Error handling of gradeForClass function"""
        await ctx.author.send(error)
        print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: gradeRequired(self, ctx, categoryName, pointValue, desiredGrade)
    #    Description: This command lets a student get the grade they need on the next assignment to keep a desired grade
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - categoryName: the name of the desired category
    #    - pointValue: the amount of points the next assignment will be worth
    #    - desiredGrade: the grade desired for the category
    #    Outputs:
    #    - The necessary grade on the next assignment to maintain a certain grade in a category
    #    Aliases:
    #    - gradereq
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(
        name="gradeRequired",
        aliases=["gradereq"],
        help="get your grade required on the next assignment for a category and a desired grade $gradeRequired CATEGORY POINTS GRADE",
    )
    async def graderequired(
        self,
        ctx,
        categoryName: str = commands.parameter(
            description="Name of the desired category"
        ),
        pointValue: str = commands.parameter(
            description="The amount of points the next assignment will be worth"
        ),
        desiredGrade: str = commands.parameter(
            description="The grade desired for the category"
        ),
    ):
        """Lets a student calculate the grade they need for a desired grade in a category"""
        memberName = ctx.author.name

        grades = db.query(
            "SELECT grades.grade FROM grades INNER JOIN assignments ON grades.assignment_id = assignments.id INNER JOIN grade_categories ON assignments.category_id = grade_categories.id WHERE grades.guild_id = %s AND grades.member_name = %s AND grade_categories.category_name = %s ORDER BY grades.assignment_id",
            (ctx.guild.id, memberName, categoryName),
        )

        points = db.query(
            "SELECT assignments.points FROM assignments INNER JOIN grade_categories ON assignments.category_id = grade_categories.id WHERE assignments.guild_id = %s AND grade_categories.category_name = %s ORDER BY assignments.id",
            (ctx.guild.id, categoryName),
        )

        if not grades:
            await ctx.author.send(f"Grades for {categoryName} do not exist")
            return

        if not points:
            await ctx.author.send(f"Assignments for {categoryName} do not exist")
            return

        actualGrades = []
        for grade in grades:
            actualGrades.append(grade[0])

        actualPoints = []
        for point in points:
            actualPoints.append(point[0])

        total = 0
        pointsTotal = 0

        for i in range(len(actualGrades)):
            total = total + (actualGrades[i] / 100) * actualPoints[i]
            pointsTotal = pointsTotal + actualPoints[i]

        pointsNeeded = (
            (int(desiredGrade) / 100) * (pointsTotal + int(pointValue))
        ) - total

        gradeNeeded = (pointsNeeded / int(pointValue)) * 100

        if gradeNeeded < 0:
            await ctx.author.send(
                f"Grade on next assignment needed to keep {desiredGrade}% in {categoryName}: 0%"
            )
            return

        await ctx.author.send(
            f"Grade on next assignment needed to keep {desiredGrade}% in {categoryName}: {gradeNeeded:.2f}%"
        )

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: graderequired_error(self, ctx, error)
    #    Description: prints error message for gradeRequired command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @graderequired.error
    async def graderequired_error(self, ctx, error):
        """Error handling of gradeRequired function"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the gradeRequired command, do: $gradeRequired <categoryname> <pointsvalue> <desiredgrade>\n ( For example: $gradeRequired tests 200 90 )"
            )
            await ctx.message.delete()
        else:
            await ctx.author.send(error)
            print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: gradeRequiredForClass(self, ctx, categoryName, pointValue, desiredGrade)
    #    Description: This command lets a student get the grade they need on the next assignment to keep a desired grade
    #    in the class
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - categoryName: the name of the category the next assignment will fall in
    #    - pointValue: the amount of points the next assignment will be worth
    #    - desiredGrade: the grade desired for the class
    #    Outputs:
    #    - The necessary grade on the next assignment to maintain a desired grade in the class
    #    Aliases:
    #    - classGradeReq
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(
        name="gradeRequiredForClass",
        aliases=["classGradeReq"],
        help="get your grade required on the next assignment to keep a desired grade $graderequiredforclass CATEGORY POINTS GRADE",
    )
    async def graderequiredforclass(
        self,
        ctx,
        categoryName: str = commands.parameter(
            description="The name of the category the next assignment will fall in"
        ),
        pointValue: str = commands.parameter(
            description="The amount of points the next assignment will be worth"
        ),
        desiredGrade: str = commands.parameter(
            description="The grade desired for the class"
        ),
    ):
        """Lets a student calculate the grade required on the next assignment to keep an overall desired class grade"""
        memberName = ctx.author.name

        categories = db.query(
            "SELECT category_name, category_weight FROM grade_categories WHERE guild_id = %s ORDER BY category_weight DESC",
            (ctx.guild.id,),
        )

        classTotal = 0

        for category_name, category_weight in categories:
            if categoryName == category_name:
                categoryWeight = category_weight
                break

            grades = db.query(
                "SELECT grades.grade FROM grades INNER JOIN assignments ON grades.assignment_id = assignments.id INNER JOIN grade_categories ON assignments.category_id = grade_categories.id WHERE grades.guild_id = %s AND grades.member_name = %s AND grade_categories.category_name = %s ORDER BY grades.assignment_id",
                (ctx.guild.id, memberName, category_name),
            )

            points = db.query(
                "SELECT assignments.points FROM assignments INNER JOIN grade_categories ON assignments.category_id = grade_categories.id WHERE assignments.guild_id = %s AND grade_categories.category_name = %s ORDER BY assignments.id",
                (ctx.guild.id, category_name),
            )

            if not grades:
                await ctx.author.send(f"Grades for {category_name} do not exist")
                return

            if not points:
                await ctx.author.send(f"Assignments for {categoryName} do not exist")
                return

            actualGrades = []
            for grade in grades:
                actualGrades.append(grade[0])

            actualPoints = []
            for point in points:
                actualPoints.append(point[0])

            total = 0
            pointsTotal = 0

            for i in range(len(actualGrades)):
                total = total + (actualGrades[i] / 100) * actualPoints[i]
                pointsTotal = pointsTotal + actualPoints[i]

            average = (total / pointsTotal) * 100

            classTotal = classTotal + average * float(category_weight)

        categoryGradeNeeded = (int(desiredGrade) - classTotal) / float(category_weight)

        if categoryGradeNeeded < 0:
            await ctx.author.send(
                f"Grade on next assignment needed to keep {int(desiredGrade)}%: 0%"
            )
            return

        grades = db.query(
            "SELECT grades.grade FROM grades INNER JOIN assignments ON grades.assignment_id = assignments.id INNER JOIN grade_categories ON assignments.category_id = grade_categories.id WHERE grades.guild_id = %s AND grades.member_name = %s AND grade_categories.category_name = %s ORDER BY grades.assignment_id",
            (ctx.guild.id, memberName, categoryName),
        )

        points = db.query(
            "SELECT assignments.points FROM assignments INNER JOIN grade_categories ON assignments.category_id = grade_categories.id WHERE assignments.guild_id = %s AND grade_categories.category_name = %s ORDER BY assignments.id",
            (ctx.guild.id, categoryName),
        )

        if not grades:
            await ctx.author.send(f"Grades for {categoryName} do not exist")
            return

        if not points:
            await ctx.author.send(f"Assignments for {categoryName} do not exist")
            return

        actualGrades = []
        for grade in grades:
            actualGrades.append(grade[0])

        actualPoints = []
        for point in points:
            actualPoints.append(point[0])

        total = 0
        pointsTotal = 0

        for i in range(len(actualGrades)):
            total = total + (actualGrades[i] / 100) * actualPoints[i]
            pointsTotal = pointsTotal + actualPoints[i]

        # pointsNeeded = ((int(desiredGrade) / 100) * (pointsTotal + int(pointValue))) - total

        pointsNeeded = (
            (categoryGradeNeeded / 100) * (pointsTotal + int(pointValue))
        ) - total

        gradeNeeded = (pointsNeeded / int(pointValue)) * 100

        if gradeNeeded < 0:
            await ctx.author.send(
                f"Grade on next assignment needed to keep {int(desiredGrade)}%: 0%"
            )
            return

        await ctx.author.send(
            f"Grade on next assignment needed to keep {int(desiredGrade)}%: {gradeNeeded:.2f}%"
        )

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: graderequiredforclass_error(self, ctx, error)
    #    Description: prints error message for gradeRequiredForClass command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @graderequiredforclass.error
    async def graderequiredforclass_error(self, ctx, error):
        """Error handling of gradeRequiredForClass function"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the gradeRequiredForClass command, do: $gradeRequiredForClass <categoryname> <pointsvalue> <desiredgrade>\n ( For example: $gradeRequiredForClass tests 200 90 )"
            )
            await ctx.message.delete()
        else:
            await ctx.author.send(error)
            print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: categories(self, ctx)
    #    Description: This command lets the user list the categories of grades that are in the system
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs:
    #    - A list of the grade categories in the system
    #    Aliases:
    #    - getbreakdown
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(
        name="categories",
        aliases=["getBreakdown"],
        help="display all grading categories and weights $categories",
    )
    async def categories(self, ctx):
        """Lets the user list the categories of grades that are in the database"""
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
    #    Description: This command allows the instructor to input grades into the system for a given assignment
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context, including the attached csv file
    #    - assignmentname: the assignment that  grades are being input for
    #    Outputs:
    #    - A report on how the grades in the system were altered
    #    Aliases:
    #    - feedGrades
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="inputGrades",
        aliases=["feedGrades"],
        help="Insert grades using a csv file",
    )
    async def input_grades(self, ctx, assignmentname: str, test="False", path=""):
        """Lets the instructor input grades into the system for a given assignment"""
        print(assignmentname)
        assignment = db.query(
            "SELECT id FROM assignments WHERE guild_id = %s AND assignment_name = %s",
            (ctx.guild.id, assignmentname),
        )

        if not assignment:
            await ctx.send(f"Assignment with name {assignmentname} does not exist")
            return
        if len(ctx.message.attachments) != 1 and test == "False":
            await ctx.send("Must have exactly one attachment")
            return
        if (
            test == "False"
            and ctx.message.attachments[0].content_type != "text/csv; charset=utf-8"
        ):
            await ctx.send("Invalid filetype")
            return
        data = None
        if test == "False":
            attachmenturl = ctx.message.attachments[0].url
            response = requests.get(attachmenturl, timeout=10)
            data = StringIO(response.text)
        if test == "TestingTrue":
            data = path
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
    #    Description: prints error message for inputGrades command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @input_grades.error
    async def input_grades_error(self, ctx, error):
        """Error handling for inputGrades command"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the inputGrades command, do: $inputGrades <assignmentname> and add your csv file attachment\n ( For example: $editGradeCategory test1 )"
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
    #    Outputs:
    #    - Whether or not the add was a success
    #    Aliases:
    #    - addCategory
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="addGradeCategory",
        aliases=["addCategory"],
        help="add a grading category and weight $addGradeCategory NAME WEIGHT",
    )
    async def add_grade_category(
        self,
        ctx,
        categoryname: str = commands.parameter(
            description="Name of the grade category"
        ),
        weight: str = commands.parameter(
            description="The weight of the category, must be greater than 0"
        ),
    ):
        """Lets the instructor add a grade category with a specified weight"""
        try:
            categoryweight = float(weight)
        except ValueError:
            await ctx.send(
                "Weight could not be parsed. Please use a float between 0.0 and 1.0"
            )
            return
        if categoryweight < 0:
            await ctx.send("Weight must be greater than 0")
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
            await ctx.send(
                "A category with this name has already been added. All categories must have unique names"
            )

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: add_grade_category_error(self, ctx, error)
    #    Description: prints error message for addGradeCategory command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @add_grade_category.error
    async def add_grade_category_error(self, ctx, error):
        """Error handling for add_grade_category command"""
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
    #    Outputs:
    #    - Whether or not the edit was a success
    #    Aliases:
    #    - editCategory
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="editGradeCategory",
        aliases=["editCategory"],
        help="edit a grading category and weight $editGradeCategory NAME WEIGHT",
    )
    async def edit_grade_category(
        self,
        ctx,
        categoryname: str = commands.parameter(
            description="Name of the grade category to edit"
        ),
        weight: str = commands.parameter(
            description="Weight of the category to edit, must be greater than 0"
        ),
    ):
        """Lets the instructor edit a grade category and weight"""
        try:
            categoryweight = float(weight)
        except ValueError:
            await ctx.send(
                "Weight could not be parsed. Please use a float between 0.0 and 1.0"
            )
            return
        if categoryweight < 0:
            await ctx.send("Weight must be greater than 0")
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
            await ctx.send(
                "This category does not exist. Check the spelling of the category name or use $addGradeCategory to add a new one"
            )

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: edit_grade_category_error(self, ctx, error)
    #    Description: prints error message for editGradeCategory command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @edit_grade_category.error
    async def edit_grade_category_error(self, ctx, error):
        """Error handling for edit_grade_category command"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the editGradeCategory command, do: $editGradeCategory <categoryname> <weight> \n ( For example: $editGradeCategory tests .5 )"
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
    #    Outputs:
    #    - Whether or not the delete was a success
    #    Aliases:
    #    - deleteCategory
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="deleteGradeCategory",
        aliases=["deleteCategory"],
        help="delete a grading category $deleteGradeCategory NAME",
    )
    async def delete_grade_category(
        self,
        ctx,
        categoryname: str = commands.parameter(
            description="Name of category to delete"
        ),
    ):
        """Lets the user delete a grade category from the database"""
        existing = db.query(
            "SELECT id FROM grade_categories WHERE guild_id = %s AND category_name = %s",
            (ctx.guild.id, categoryname),
        )
        if existing:
            db.query("DELETE FROM grade_categories WHERE id = %s", (existing[0]))
            await ctx.send(f"{categoryname} category has been deleted ")
        else:
            await ctx.send(
                "This category does not exist. Please check the spelling of the category name"
            )

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: delete_grade_category_error(self, ctx, error)
    #    Description: prints error message for deleteGradeCategory command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @delete_grade_category.error
    async def delete_grade_category_error(self, ctx, error):
        """Error handling for delete_grade_category command"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the deleteGradeCategory command, do: $deleteGradeCategory <categoryname> \n ( For example: $deleteGradeCategory tests)"
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
    #    Outputs:
    #    - A breakdown on the performance of each category
    #    Aliases:
    #    - getCategoryReport
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="gradeReportCategory",
        aliases=["getCategoryReport"],
        help="Report on the classes scores all grade categories",
    )
    async def grade_report_category(self, ctx):
        """Lets the instructor generate a report on the average, low, and high score for each category"""
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
    #    Outputs:
    #    - A breakdown on the performance of each assignment
    #    Aliases:
    #    - getAssignementReport
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="gradeReportAssignment",
        aliases=["getAssignmentReport"],
        help="Report on the classes scores all assignments",
    )
    async def grade_report_assignment(self, ctx):
        """Lets the instructor generate a report on the average, low, and high score for each assignment"""
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
    """Adds the file to the bot's cog system"""
    await bot.add_cog(Grades(bot))
