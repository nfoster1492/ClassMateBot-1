# TODO deadline reminder for all students
# Copyright (c) 2021 War-Keeper
# This functionality provides various methods to manage reminders (in the form of creation, retrieval,
# updation and deletion)
# A user can set up a reminder, check what is due this week or what is due today.
# He/She can also check all the due homeworks based on hte coursename.
# A user can also update or delete a reminder if needed.
import os
import asyncio
from datetime import datetime, timedelta, timezone, time
from dateutil import parser
import sys
from discord.ext import commands, tasks
import discord

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db


class Deadline(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.units = {
            "second": 1,
            "minute": 60,
            "hour": 3600,
            "day": 86400,
            "week": 604800,
            "month": 2592000,
        }

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: timeNow(self, ctx, *, date: str)
    #    Description: This command lets the user get the offset needed for proper datetime reminders in UTC.
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - date: current date and 24-hour time
    #    Outputs: offset from the user's current time with UTC.
    #    Aliases:
    #    - currTime
    #    - setCurrTime
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(
        name="timeNow",
        aliases=["currTime", "setCurrTime"],
        help="put in current time to get offset needed for proper "
        "datetime notifications $timeNow MMM DD YYYY HH:MM ex. $timeNow SEP 25 2024 17:02",
    )
    async def timeNow(
        self,
        ctx,
        *,
        date: str = commands.parameter(description="Current date and 24-hour time"),
    ):
        """Gets offset for proper datetime notifications compared to UTC"""
        try:
            input_time = parser.parse(date)
        except ValueError:
            await ctx.send("Due date could not be parsed")
            return

        utc_dt = datetime.utcnow()
        difference = utc_dt - input_time
        diff_in_hours = int(difference.total_seconds() / 3600)
        input_time += timedelta(hours=diff_in_hours)

        await ctx.send(
            f"Current time is {-diff_in_hours} hours from system time (UTC)."
        )

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: timeNow_error(self, ctx, error)
    #    Description: prints error message for timeNow command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @timeNow.error
    async def timeNow_error(self, ctx, error):
        """Error handling for timeNow command"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the timeNow command (with current time), do: "
                "$timeNow MMM DD YYYY HH:MM ex. $timeNow SEP 25 2024 17:02"
            )
        else:
            await ctx.author.send(error)
            # await ctx.message.delete()
            print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: dueDate(self, ctx, coursename: str, hwcount: str, *, date: str)
    #    Description: Adds the reminder to database in the specified format
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - coursename: name of the course for which reminder is to be added
    #    - hwcount: name of the reminder
    #    - date: due date of the assignment
    #    Outputs: returns either an error stating a reason for failure or returns a success message
    #          indicating that the reminder has been added
    #    Aliases:
    #    - whenDue
    #    - setDueDate
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="dueDate",
        aliases=["whenDue", "setDueDate"],
        help="add reminder and due-date $dueDate CLASSNAME NAME MMM DD YYYY optional(HH:MM) optional(TIMEZONE)"
        "ex. $dueDate CSC510 HW2 SEP 25 2024 17:02 EST",
    )
    async def dueDate(
        self,
        ctx,
        coursename: str = commands.parameter(
            description="Name of the course for which the reminder is to be added"
        ),
        hwcount: str = commands.parameter(description="Name of the reminder"),
        *,
        date: str = commands.parameter(description="Due date of the assignment"),
    ):
        """Add reminder for specified course, assignment, and date"""
        author = ctx.message.author

        try:
            dueDate = parser.parse(date)
        except ValueError:
            await ctx.send("Due date could not be parsed")
            return

        existing = db.query(
            "SELECT author_id FROM reminders WHERE guild_id = %s AND course = %s AND reminder_name = %s",
            (ctx.guild.id, coursename, hwcount),
        )
        if not existing:
            db.query(
                "INSERT INTO reminders (guild_id, author_id, course, reminder_name, due_date) VALUES (%s, %s, %s, %s, %s)",
                (ctx.guild.id, author.id, coursename, hwcount, dueDate),
            )
            caldueDate = dueDate.astimezone(timezone.utc)
            isodate = caldueDate.isoformat(timespec="seconds")[:-6]
            await ctx.send(
                f"A date has been added for: {coursename} reminder named: {hwcount} "
                f"which is due on: {dueDate} by {author}."
                f"Use this command to add the reminder to the calendar! **`$addCalendarEvent {hwcount} {coursename} {isodate}Z`**"
            )
        else:
            await ctx.send("This reminder has already been added..!!")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: dueDate_error(self, ctx, error)
    #    Description: prints error message for dueDate command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @dueDate.error
    async def dueDate_error(self, ctx, error):
        """Error handling for dueDate command"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the dueDate command, do: $dueDate CLASSNAME NAME MMM DD YYYY optional(HH:MM) optional(TIMEZONE)\n "
                "( For example: $dueDate CSC510 HW2 SEP 25 2024 17:02 EST )"
            )
        else:
            await ctx.author.send(error)
            # await ctx.message.delete()
            print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: deleteReminder(self, ctx, courseName: str, hwName: str)
    #    Description: Delete a reminder using Classname and Homework name
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - coursename: name of the course for which homework is to be added
    #    - hwName: name of the homework
    #    Outputs: returns either an error stating a reason for failure or
    #          returns a success message indicating that the reminder has been deleted
    #    Aliases:
    #    - removeReminder
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="deleteReminder",
        aliases=["removeReminder"],
        pass_context=True,
        help="Delete a specific reminder using course name and reminder name using "
        "$deleteReminder CLASSNAME HW_NAME ex. $deleteReminder CSC510 HW2",
    )
    async def deleteReminder(
        self,
        ctx,
        courseName: str = commands.parameter(
            description="Name of the course for which homework is to be added"
        ),
        hwName: str = commands.parameter(description="Name of the homework"),
    ):
        """Deletes a specified reminder"""
        reminders_deleted = db.query(
            "SELECT course, reminder_name, due_date FROM reminders WHERE guild_id = %s AND reminder_name = %s AND course = %s",
            (ctx.guild.id, hwName, courseName),
        )
        db.query(
            "DELETE FROM reminders WHERE guild_id = %s AND reminder_name = %s AND course = %s",
            (ctx.guild.id, hwName, courseName),
        )

        for course, reminder_name, due_date in reminders_deleted:
            due = due_date.strftime("%Y-%m-%d %H:%M:%S")
            await ctx.send(
                f"Following reminder has been deleted: Course: {course}, "
                f"reminder Name: {reminder_name}, Due Date: {due}"
            )

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: deleteReminder_error(self, ctx, error)
    #    Description: prints error message for deleteReminder command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @deleteReminder.error
    async def deleteReminder_error(self, ctx, error):
        """Error handling for deleteReminder"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the deleteReminder command, do: $deleteReminder CLASSNAME HW_NAME \n "
                "( For example: $deleteReminder CSC510 HW2 )"
            )
        else:
            await ctx.author.send(error)
            # await ctx.message.delete()
            print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: changeDueDate(self, ctx, classid: str, hwid: str, *, date: str)
    #    Description: Update the 'Due date' for a homework by providing the classname and homewwork name
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - classid: name of the course for which homework is to be added
    #    - hwid: name of the homework
    #    - date: due date of the assignment
    #    Outputs: returns either an error stating a reason for failure or
    #          returns a success message indicating that the reminder has been updated
    #    Aliases:
    #    - changedue
    # -----------------------------------------------------------------------------------------------------------------
    @commands.has_role("Instructor")
    @commands.command(
        name="changeDueDate",
        aliases=["changeDue"],
        pass_context=True,
        help="Update the assignment date. $changeDueDate CLASSNAME HW_NAME MMM DD YYYY optional(HH:MM) optional(TIMEZONE)"
        "ex. $changeDueDate CSC510 HW2 SEP 25 2024 17:02 EST",
    )
    async def changeDueDate(
        self,
        ctx,
        classid: str = commands.parameter(
            description="Name of the course for which homework is to be added"
        ),
        hwid: str = commands.parameter(description="Name of the homework"),
        *,
        date: str = commands.parameter(description="New due date of the assignment"),
    ):
        """Updates an assignment's due date in the database"""
        author = ctx.message.author
        try:
            dueDate = parser.parse(date)
            print(dueDate)
        except ValueError:
            await ctx.send("Due date could not be parsed")
            return

        # future = (time.time() + (dueDate - datetime.today()).total_seconds())
        db.query(
            "UPDATE reminders SET author_id = %s, due_date = %s WHERE guild_id = %s AND reminder_name = %s AND course = %s",
            (author.id, dueDate, ctx.guild.id, hwid, classid),
        )
        await ctx.send(
            f"{classid} {hwid} has been updated with following date: {dueDate}"
        )

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: changeDueDate_error(self, ctx, error)
    #    Description: prints error message for changeDueDate command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @changeDueDate.error
    async def changeDueDate_error(self, ctx, error):
        """Error handling for changeDueDate command"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "To use the changeDueDate command, do: $changeDueDate CLASSNAME HW_NAME MMM DD YYYY optional(HH:MM) optional(TIMEZONE)\n"
                " ( For example: $changeDueDate CSC510 HW2 SEP 25 2024 17:02 EST)"
            )
        else:
            await ctx.author.send(error)
            # await ctx.message.delete()
            print(error)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: dueThisWeek(self, ctx)
    #    Description: Displays all the homeworks that are due this week along with the coursename and due date
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: returns either an error stating a reason for failure
    #             or returns a list of all the assignments that are due this week
    #    Aliases:
    #    - getweeklydue
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(
        name="dueThisWeek",
        aliases=["getWeeklyDue"],
        pass_context=True,
        help="Check all the homeworks that are due this week $dueThisWeek",
    )
    async def dueThisWeek(self, ctx):
        """Checks all homeworks or assignments due this week"""
        reminders = db.query(
            "SELECT course, reminder_name, due_date "
            "FROM reminders "
            "WHERE guild_id = %s AND date_part('day', due_date - now()) <= 7 AND date_part('minute', due_date - now()) >= 0",
            (ctx.guild.id,),
        )

        curr_date = datetime.now(timezone.utc)

        for course, reminder_name, due_date in reminders:
            delta = due_date - curr_date
            formatted_due_date = due_date.strftime("%b %d %Y %H:%M:%S%z")
            await ctx.author.send(
                f"{course} {reminder_name} is due in {delta.days} days, {delta.seconds//3600}"
                f" hours and {(delta.seconds//60)%60} minutes ({formatted_due_date})"
            )
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: duethisweek_error(self, ctx, error)
    #    Description: prints error message for dueThisWeek command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @dueThisWeek.error
    async def duethisweek_error(self, ctx, error):
        """Error handling for dueThisWeek command"""
        await ctx.author.send(error)
        print(error)
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: dueToday(self, ctx)
    #    Description: Displays all the homeworks that are due today
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    # Outputs: returns either an error stating a reason for failure or
    #          returns a list of all the assignments that are due on the day the command is run
    #    Aliases:
    #    - getDailyDue
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(
        name="dueToday",
        aliases=["getDailyDue"],
        pass_context=True,
        help="Check all the reminders that are due today $dueToday",
    )
    async def dueToday(self, ctx):
        """Checks for all reminders that are due today"""
        due_today = db.query(
            "SELECT course, reminder_name, due_date "
            "FROM reminders "
            "WHERE guild_id = %s AND date_part('day', due_date - now()) <= 1 AND date_part('minute', due_date - now()) >= 0",
            (ctx.guild.id,),
        )
        for course, reminder_name, due_date in due_today:
            delta = due_date - datetime.now(timezone.utc)
            await ctx.author.send(
                f"{course} {reminder_name} is due in {delta.days} days, {delta.seconds//3600}"
                f" hours and {(delta.seconds//60)%60} minutes"
            )
        if len(due_today) == 0:
            await ctx.author.send("You have no dues today..!!")
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: duetoday_error(self, ctx, error)
    #    Description: prints error message for dueToday command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @dueToday.error
    async def dueToday_error(self, ctx, error):
        """Error handling for dueToday command"""
        await ctx.author.send(error)
        print(error)
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: courseDue(self, ctx, courseid: str)
    #    Description: Displays all the reminder_names that are due for a specific course
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - courseid: name of the course for which reminder_name is to be added
    #    Outputs: returns either an error stating a reason for failure or
    #          a list of assignments that are due for the provided courseid
    #    Aliases:
    #    - getCourseDue
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(
        name="courseDue",
        aliases=["getCourseDue"],
        pass_context=True,
        help="Check all the reminders that are due for a specific course $courseDue coursename "
        "ex. $courseDue CSC505",
    )
    async def courseDue(
        self,
        ctx,
        courseid: str = commands.parameter(
            description="Name of the course for which all reminders are checked"
        ),
    ):
        """Displays a list of all reminders due for a specific course"""
        reminders = db.query(
            "SELECT reminder_name, due_date FROM reminders WHERE guild_id = %s AND course = %s",
            (ctx.guild.id, courseid),
        )
        for reminder_name, due_date in reminders:
            formatted_due_date = due_date.strftime("%b %d %Y %H:%M:%S")
            await ctx.author.send(f"{reminder_name} is due at {formatted_due_date}")
        if len(reminders) == 0:
            await ctx.author.send(
                f"Rejoice..!! You have no pending reminders for {courseid}..!!"
            )
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: courseDue_error(self, ctx, error)
    #    Description: prints error message for courseDue command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @courseDue.error
    async def courseDue_error(self, ctx, error):
        """Error handling for courseDue command"""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(
                "To use the courseDue command, do: $courseDue CLASSNAME \n ( For example: $courseDue CSC510 )"
            )
        else:
            await ctx.author.send(error)
            print(error)
        await ctx.message.delete()

    # ---------------------------------------------------------------------------------
    #    Function: listReminders(self, ctx)
    #    Description: Print out all the reminders
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: returns either an error stating a reason for failure or
    #             returns a list of all the assignments
    #    Aliases:
    #    - getReminders
    # ---------------------------------------------------------------------------------
    @commands.command(
        name="listReminders",
        aliases=["getReminders"],
        pass_context=True,
        help="lists all reminders",
    )
    async def listReminders(self, ctx):
        """Displays user with list of all reminders"""
        author = ctx.message.author
        reminders = db.query(
            "SELECT course, reminder_name, due_date FROM reminders WHERE guild_id = %s and author_id = %s and now() < due_date",
            (ctx.guild.id, author.id),
        )

        for course, reminder_name, due_date in reminders:
            formatted_due_date = due_date.strftime("%b %d %Y %H:%M:%S%z")
            await ctx.author.send(
                f"{course} reminder named: {reminder_name} which is due on: {formatted_due_date} by {author.name}"
            )
        if not reminders:
            await ctx.author.send(
                "Mission Accomplished..!! You don't have any more dues..!!"
            )
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: listreminders_error(self, ctx, error)
    #    Description: prints error message for listReminders command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @listReminders.error
    async def listReminders_error(self, ctx, error):
        """Error handling for listReminders command"""
        await ctx.author.send(error)
        print(error)
        await ctx.message.delete()

    # ---------------------------------------------------------------------------------
    #    Function: overdue(self, ctx)
    #    Description: Print out all the reminders
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: returns either an error stating a reason for failure or
    #             returns a list of all the assignments
    #    Aliases:
    #    - getOverdue
    #    - getLateAssignments
    # ---------------------------------------------------------------------------------
    @commands.command(
        name="overdue",
        aliases=["getOverdue", "getLateAssignments"],
        pass_context=True,
        help="lists overdue reminders",
    )
    async def overdue(self, ctx):
        """Displays list of homeworks and assignments that are overdue"""
        author = ctx.message.author
        reminders = db.query(
            "SELECT course, reminder_name, due_date FROM reminders WHERE guild_id = %s and author_id = %s"
            " and now() > due_date",
            (ctx.guild.id, author.id),
        )

        for course, reminder_name, due_date in reminders:
            formatted_due_date = due_date.strftime("%b %d %Y %H:%M:%S%z")
            await ctx.author.send(
                f"{course} reminder named: {reminder_name} which was due on: {formatted_due_date} by {author.name}"
            )
        if not reminders:
            await ctx.author.send("There are no overdue reminders")
        await ctx.message.delete()

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: listreminders_error(self, ctx, error)
    #    Description: prints error message for listReminders command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @overdue.error
    async def overdue_error(self, ctx, error):
        """Error handling for overdue command"""
        await ctx.author.send(error)
        print(error)
        await ctx.message.delete()

    # ---------------------------------------------------------------------------------
    #    Function: clearallreminders(self, ctx)
    #    Description: Delete all the reminders
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: returns either an error stating a reason for failure or
    #             returns a success message stating that reminders have been deleted
    #    Aliases:
    #    - deleteallreminders
    #    - rmallreminds
    # ---------------------------------------------------------------------------------

    @commands.command(
        name="clearReminders",
        aliases=["deleteAllReminders", "rmAllReminds"],
        pass_context=True,
        help="deletes all reminders",
    )
    async def clearallreminders(self, ctx):
        """Clears all reminders from database"""
        db.query("DELETE FROM reminders WHERE guild_id = %s", (ctx.guild.id,))
        await ctx.send("All reminders have been cleared..!!")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: clearallreminders_error(self, ctx, error)
    #    Description: prints error message for clearreminders command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @clearallreminders.error
    async def clearallreminders_error(self, ctx, error):
        """Error handling for clearreminders command"""
        await ctx.author.send(error)
        print(error)

    # ---------------------------------------------------------------------------------
    #    Function: remindme(self, ctx, quantity: int, time_unit : str,*, text :str)
    #    Description: Personal remind me functionality
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - quantity - time after which the data will be erased
    #    Outputs: returns either an error stating a reason for failure or
    #             returns a success message stating that reminders have been deleted
    # ---------------------------------------------------------------------------------

    # @commands.command(name="remindme", pass_context=True, help="Request the bot to set a reminder for a due date")
    # async def remindme(self, ctx, quantity: int, time_unit: str, *, text: str):

    #     time_unit = time_unit.lower()
    #     author = ctx.message.author
    #     s = ""
    #     if time_unit.endswith("s"):
    #         time_unit = time_unit[:-1]
    #         s = "s"
    #     if not time_unit in self.units:
    #         await ctx.send("Invalid unit of time. Select from seconds/minutes/hours/days/weeks/months")
    #         return
    #     if quantity < 1:
    #         await ctx.send("Quantity must not be 0 or negative")
    #         return
    #     if len(text) > 1960:
    #         await ctx.send("Text is too long.")
    #         return

    #     seconds = self.units[time_unit] * quantity
    #     future = int(time.time() + seconds)
    #     # TODO set timestamp compatible with db

    #     db.query(
    #         'INSERT INTO reminders (guild_id, author_id, future, text) VALUES (%s, %s, %s)',
    #         (ctx.guild.id, author.id, future, text)
    #     )

    #     await ctx.send("I will remind you that in {} {}.".format(str(quantity), time_unit + s))

    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, error):
    #     await ctx.send('Unidentified command..please use $help to get the list of available commands')

    # -----------------------------------------------------------------------------------------------------
    #    Function: clearOverdue(self)
    #    Description: checks for expired reminders and cleans them.
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: context of the command
    #    Aliases:
    #    - removeoverdue
    #    - clearlate
    # -----------------------------------------------------------------------------------------------------
    @commands.command(
        name="clearOverdue",
        aliases=["removeOverdue", "clearLate"],
        pass_context=True,
        help="deletes overdue reminders",
    )
    async def clearOverdue(self, ctx):
        """Clears all overdue reminders from database"""
        db.query("DELETE FROM reminders WHERE now() > due_date")
        await ctx.send("All overdue reminders have been cleared..!!")

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: clearOverdue_error(self, ctx, error)
    #    Description: prints error message for clearOverdue command
    #    Inputs:
    #       - ctx: context of the command
    #       - error: error message
    #    Outputs:
    #       - Error details
    # -----------------------------------------------------------------------------------------------------------------
    @clearOverdue.error
    async def clearOverdue_error(self, ctx, error):
        """Error handling for clearOverdue"""
        await ctx.author.send(error)
        print(error)

    # -----------------------------------------------------------------------------------------------------
    #    Function: send_reminders_day(self)
    #    Description: task that runs once per day and sends a reminders for assignments due
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    # -----------------------------------------------------------------------------------------------------
    @tasks.loop(hours=24)
    async def send_reminders_day(self):
        """Task running once per day to send a reminder for assignments due"""
        channel = discord.utils.get(self.bot.get_all_channels(), name="reminders")
        if channel:
            reminders = db.query(
                "SELECT course, reminder_name, due_date "
                "FROM reminders "
                "WHERE due_date::date = now()::date"
            )
            for course, reminder_name, due_date in reminders:
                difference = due_date - datetime.now(timezone.utc)
                await channel.send(
                    f"{reminder_name} for {course} is due in {(difference.seconds//3600)} hours"
                )

    # -----------------------------------------------------------------------------------------------------
    #    Function: bofore(self)
    #    Description: runs once per day and waits until 8:00 AM EST to send reminders via the send
    #       reminders day function
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    # -----------------------------------------------------------------------------------------------------
    @send_reminders_day.before_loop
    async def before(self):
        """Task that runs once per day and waits until 8am EST to send reminders via send_reminders_day function"""
        WHEN = time(13, 0, 0)  # 8:00 AM eastern
        now = datetime.utcnow()
        target_time = datetime.combine(now.date(), WHEN)
        seconds_until_target = (target_time - now).total_seconds()
        if seconds_until_target < 0:
            target_time = datetime.combine(now.date() + timedelta(days=1), WHEN)
            seconds_until_target = (target_time - now).total_seconds()
        await asyncio.sleep(seconds_until_target)

    # -----------------------------------------------------------------------------------------------------
    #    Function: send_reminders_hour(self)
    #    Description: task that runs once per hours and sends a reminders for assignments due
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    # -----------------------------------------------------------------------------------------------------
    @tasks.loop(hours=1)
    async def send_reminders_hour(self):
        """Task that runs once per hour ans sends a reminder for assignments due"""
        channel = discord.utils.get(self.bot.get_all_channels(), name="reminders")
        if channel:
            reminders = db.query(
                "SELECT course, reminder_name, due_date "
                "FROM reminders "
                "WHERE due_date::date = now()::date"
            )
            for course, reminder_name, due_date in reminders:
                difference = due_date - datetime.now(timezone.utc)
                if difference.seconds // 3600 == 0:
                    await channel.send(
                        f"{reminder_name} for {course} is due within the hour"
                    )


# -------------------------------------
# add the file to the bot's cog system
# -------------------------------------
async def setup(bot):
    """Adds the file to the bot's cog system"""
    n = Deadline(bot)
    n.send_reminders_day.start()  # pylint: disable=no-member
    n.send_reminders_hour.start()  # pylint: disable=no-member
    await bot.add_cog(n)
