# TODO user-specific reminder system
# This cog provides functionalities for managing user-specific reminders.
# Users can create personal reminders, view them, update, or delete them as needed.
# Additionally, there is a feature to list all reminders and send notifications for due reminders.
import asyncio
from datetime import datetime, timedelta, timezone
from dateutil import parser
import discord
from discord.ext import commands, tasks
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db


class UserReminders(commands.Cog):
    """
    A cog for managing personal and course-related reminders within a Discord guild.
    """

    def __init__(self, bot):
        self.bot = bot
        self.check_reminders.start()

    # -----------------------------------------------------------------------------------------------------------------
    # Function: add_personal_reminder(self, ctx, title: str, due_date: str, message: str = "")
    # Description: Add a new reminder to the database.
    # Inputs:
    # - ctx: The context of the command.
    # - title: The title of the reminder.
    # - due_date: The due date for the reminder.
    # - message: An optional message for the reminder.
    # Outputs: A message indicating the successful addition of a reminder.
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name="addpersonalreminder")
    async def add_personal_reminder(
        self, ctx, title: str, due_date: str, message: str = ""
    ):
        """
        Add a new personal reminder.
        """
        try:
            duedate = parser.parse(due_date)
            db.query(
                "INSERT INTO personal_reminders (user_id, title, due_date, message) VALUES (%s, %s, %s, %s)",
                (ctx.author.id, title, duedate, message),
            )
            await ctx.send(f"Personal reminder '{title}' set for {duedate}.")
        except ValueError:
            await ctx.send("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")

    # -----------------------------------------------------------------------------------------------------------------
    # Function: delete_personal_reminder(self, ctx, reminder_id: int)
    # Description: Delete a reminder from the database using its ID.
    # Inputs:
    # - ctx: The context of the command.
    # - reminder_id: The unique ID of the reminder to delete.
    # Outputs: A message indicating the successful deletion of a reminder or a warning if the reminder was not found.
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name="deletepersonalreminder")
    async def delete_personal_reminder(self, ctx, reminder_id: int):
        """
        Delete a specific personal reminder.
        """
        result = db.query(
            "DELETE FROM personal_reminders WHERE id = %s AND user_id = %s RETURNING *",
            (reminder_id, ctx.author.id),
        )
        if result:
            await ctx.send(f"Personal reminder with ID {reminder_id} deleted.")
        else:
            await ctx.send(f"No personal reminder found with ID {reminder_id}.")

    # -----------------------------------------------------------------------------------------------------------------
    # Function: list_personal_reminders(self, ctx)
    # Description: List all reminders from the database for the guild.
    # Inputs:
    # - ctx: The context of the command.
    # Outputs: An embedded message listing all reminders or a message stating that no reminders are found.
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name="listpersonalreminders")
    async def list_personal_reminders(self, ctx):
        """
        List all personal reminders.
        """
        reminders = db.query(
            "SELECT id, title, due_date, message FROM personal_reminders WHERE user_id = %s",
            (ctx.author.id,),
        )
        if reminders:
            embed = discord.Embed(title="Your Personal Reminders", color=0x00FF00)
            for reminder in reminders:
                embed.add_field(
                    name=f"ID: {reminder[0]}, Title: {reminder[1]}",
                    value=f"Due: {reminder[2]}, Message: {reminder[3]}",
                    inline=False,
                )
            await ctx.send(embed=embed)
        else:
            await ctx.send("You have no personal reminders.")

    # -----------------------------------------------------------------------------------------------------------------
    # Function: update_personal_reminder(self, ctx, reminder_id: int, new_due_date: str, new_message: str = "")
    # Description: Update an existing reminder in the database.
    # Inputs:
    # - ctx: The context of the command.
    # - reminder_id: The ID of the reminder to update.
    # - new_due_date: The new due date for the reminder.
    # - new_message: An optional new message for the reminder.
    # Outputs: A message indicating the successful update of a reminder.
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name="updatepersonalreminder")
    async def update_personal_reminder(
        self, ctx, reminder_id: int, new_due_date: str, new_message: str = ""
    ):
        """
        Update a specific personal reminder.
        """
        try:
            new_duedate = parser.parse(new_due_date)
            db.query(
                "UPDATE personal_reminders SET due_date = %s, message = %s WHERE id = %s AND user_id = %s",
                (new_duedate, new_message, reminder_id, ctx.author.id),
            )
            await ctx.send(f"Personal reminder with ID {reminder_id} updated.")
        except ValueError:
            await ctx.send("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")

    # -----------------------------------------------------------------------------------------------------------------
    # Function: send_reminders(self)
    # Description: A task that sends out reminders that are due.
    # Inputs: None.
    # Outputs: Sends messages to the 'reminders' channel in the guild for each due reminder.
    # -----------------------------------------------------------------------------------------------------------------
    @tasks.loop(minutes=30)
    async def check_reminders(self):
        """
        Periodically check and send notifications for due personal reminders.
        """
        now = datetime.now(timezone.utc)
        reminders = db.query(
            "SELECT user_id, title, message FROM personal_reminders WHERE due_date <= %s AND notified = FALSE",
            (now,),
        )
        for reminder in reminders:
            user = self.bot.get_user(reminder[0])
            if user:
                await user.send(f"**Reminder:** {reminder[1]} - {reminder[2]}")
                db.query(
                    "UPDATE personal_reminders SET notified = TRUE WHERE title = %s AND user_id = %s",
                    (reminder[1], reminder[0]),
                )

    @check_reminders.before_loop
    async def before_check_reminders(self):
        """
        Ensure the bot is ready before starting to check reminders.
        """
        await self.bot.wait_until_ready()


# -------------------------------------
# Add the cog to the bot's system and start the tasks
# -------------------------------------
async def setup(bot):
    """
    Setup the cog when the bot is started.
    """
    await bot.add_cog(UserReminders(bot))
