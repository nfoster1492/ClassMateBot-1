# About $addCalendarEvent _(Modified Command in Project 2)_
This command lets the user add an event to the shared Google Calendar

# Location of Code
The code that implements the above mentioned gets functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/calendar.py)

# Code Description
## Functions
addCalendarEvent(self, ctx, name, description, eventTime):: <br>
This function takes as arguments the values provided by the constructor through self, the context in which the command was called, the name and description of the event, as well as the event date and time information.

# How to run it? (Small Example)
An example of this command's usage would be when a user would like to place an item on the Google Calendar. For example, Homework 1a for CSC510 is due on 10/11/2023 at 12:00pm
enter the command '$addCalendarEvent HW1a CSC510 2023-10-11T12:00:00Z' and the bot will provide confirmation if the calendar add was successful.
```
$addCalendarEvent HW1a CSC510 2023-10-11T12:00:00Z
```
Successful execution of this command will result in an event being placed on the shared calendar for all subscribers to see and confirmation output.

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj2media/addCalendarEvent.png?raw=true" width=500>

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - addCalEvent
