# About $dueDate 
This command lets the user (either the TAs or professor) to add a reminder to the discord channel.

New in project two, this command now provides the runner with a command that will allow them to add the due date to the google calendar programmatically.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/deadline.py).

# Code Description
## Functions
dueDate(self, ctx, coursename: str, hwcount: str, *, date: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, name of the course, name of the deadline, and the date and time when the deadline is due. 

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'dueDate' pass in all the parameters as a space seperated inputs in the following order:
coursename, deadline name, dueDate (in MMM DD YYYY optional(HH:MM) optional(timezone) format)
```
$dueDate CLASSNAME NAME MMM DD YYYY optional(HH:MM) optional(timezone)
$dueDate CSC510 HW2 SEP 25 2024 17:02 EST
```
Successful execution of this command will add the reminder for the specified coursework on the specified time.

![$dueDate CSC510 HW2 SEP 25 2024 17:02](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/media/addhomework.gif?raw=true)
