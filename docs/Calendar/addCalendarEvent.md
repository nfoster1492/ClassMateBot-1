# About $addCalendarEvent _(Modified Command in Project 2)_
This command lets the user add an event to the shared Google Calendar

# Location of Code
The code that implements the above mentioned gets functionality is located [here](https://github.com/nfoster1492/ClassMateBot-1/blob/main/cogs/calendar.py)

# Code Description
## Functions
addCalendarEvent(self, ctx, name, description, eventTime):: <br>
This function takes as arguments the values provided by the constructor through self, the context in which the command was called, the name and description of the event, as well as the event date and time information.

# How to run it? (Small Example)
An example of this command's usage would be when a user would like to place an item on the Google Calendar. For example, Homework 1 for CSC510 is due on 10/19
enter the command 'clearCalendar': in the instructor commands channel and the bot will let you know the success or failure of your command
```
$clearCalendar
```
Successful execution of this command will result in an event being placed on the shared calendar for all subscribers to see.

![image](https://github.com/nfoster1492/ClassMateBot-1/blob/main/data/proj2media/addCalendarEvent.png)