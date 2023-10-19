# About $due_date 
This command lets the user (either the TAs or professor) to add a reminder to the discord channel.

New in project two, this command now provides the runner with a command that will allow them to add the due date to the google calendar programmatically.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/SE21-Team2/ClassMateBot/blob/main/cogs/deadline.py).

# Code Description
## Functions
duedate(self, ctx, coursename: str, hwcount: str, *, date: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, name of the course, name of the deadline, and the date and time when the deadline is due. 

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'duedate' pass in all the parameters as a space seperated inputs in the following order:
coursename, deadline name, duedate (in MMM DD YYYY optional(HH:MM) optional(timezone) format)
```
$addhw CLASSNAME NAME MMM DD YYYY optional(HH:MM) optional(timezone)
$addhw CSC510 HW2 SEP 25 2024 17:02 EST
```
Successful execution of this command will add the reminder for the specified coursework on the specified time.

![$duedate CSC510 HW2 SEP 25 2024 17:02](https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/addhomework.gif)
