# About $listpersonalreminders
This command allows users to list all their personal reminders from the database.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/userreminders.py).

# Code Description
## Functions
list_personal_reminders(self, ctx):
This function takes the following argument:

    ctx (Context): The context of the command.

This function retrieves all personal reminders associated with the user who triggered the command and displays them in an embedded message.


# How to run it? (Small Example)

To list personal reminders, use the command $listpersonalreminders.

Example:

$listpersonalreminders

This command will display a list of all your personal reminders.