# About $check_reminders

This background task periodically sends notifications for due personal reminders.


# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/userreminders.py).

# Code Description
## Functions

check_reminders(self):
This function runs periodically as a background task and sends notifications for due personal reminders. It checks the due date of each reminder in the database and sends a notification to the user if the reminder is due and has not been notified before.

# How to run it? (Small Example)

This background task runs automatically as part of the cog's functionality when the bot is running. Users do not need to trigger it manually.