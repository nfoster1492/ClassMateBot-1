# About $deletepersonalreminder

This command allows users to delete a specific personal reminder from the database using its ID.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/userreminders.py).

# Code Description
## Functions
delete_personal_reminder(self, ctx, reminder_id: int):
This function takes the following arguments:

    ctx (Context): The context of the command.
    reminder_id (int): The unique ID of the reminder to delete.

This function deletes a specific personal reminder from the database if it exists and is associated with the user who triggered the command.


# How to run it? (Small Example)
To delete a personal reminder, follow these steps:

    Enter the command $deletepersonalreminder.
    Provide the reminder_id as an argument to specify which reminder to delete.

Example:

$deletepersonalreminder 1

This command will delete the personal reminder with ID 1 if it exists.
