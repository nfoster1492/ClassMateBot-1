# About $addpersonalreminder
This command allows users to add a new personal reminder to the database.


# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/userreminders.py).

# Code Description
## Functions
add_personal_reminder(self, ctx, title: str, due_date: str, message: str = ""):
This function takes the following arguments:

    ctx: The context of the command.
    title: The title of the reminder.
    due_date: The due date for the reminder.
    message (optional): An optional message for the reminder.

This function adds a new personal reminder to the database with the specified title, due date, and optional message. The reminder is associated with the user who triggered the command.


# How to run it? (Small Example)

Let's say you are in a server where the Classmate Bot is active and online. To add a personal reminder, follow these steps:

    Enter the command $addpersonalreminder.
    Provide the required parameters in the following order:
        title: The title of the reminder.
        due_date: The due date for the reminder (in the format YYYY-MM-DD HH:MM:SS).
        message (optional): An optional message for the reminder.

Example:

$addpersonalreminder MyReminder 2024-12-01 15:00 This is my reminder message.

This command will add a personal reminder with the specified details.
