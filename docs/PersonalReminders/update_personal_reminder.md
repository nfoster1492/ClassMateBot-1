# About $updatepersonalreminder
This command allows users to update an existing personal reminder in the database.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/userreminders.py).

# Code Description
## Functions
update_personal_reminder(self, ctx, reminder_id: int, new_due_date: str, new_message: str = ""):
This function takes the following arguments:

    ctx (Context): The context of the command.
    reminder_id (int): The ID of the reminder to update.
    new_due_date (str): The new due date for the reminder.
    new_message (optional, str): An optional new message for the reminder.

This function updates an existing personal reminder in the database with the specified due date and optional message. It ensures that the reminder being updated belongs to the user who triggered the command. 

# How to run it? (Small Example)
To update a personal reminder, use the command $updatepersonalreminder followed by the reminder ID, the new due date, and an optional new message.

Example:

$updatepersonalreminder 1 2024-12-01 15:00 New message for the reminder

This command will update the personal reminder with ID 1.
