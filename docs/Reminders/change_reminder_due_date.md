# About $changeDueDate
This command lets the user update the homework due date for specific course and homework.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/deadline.py).

# Code Description
## Functions
changeDueDate(self, ctx, classid: str, hwid: str, *, date: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, name of the course, name of the homework, and the updated date and time. 

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command '$changeduedate' and pass in all the parameters as a space seperated inputs in the following order:
coursename, homeworkname, updated duedate (in MMM DD YYYY optional(HH:MM) format)
```
$changeDueDate CLASSNAME HW_NAME MMM DD YYYY optional(HH:MM)
$changeDueDate CSC510 HW2 SEP 25 2024 17:02
```
Successful execution of this command will update the reminder for the specified coursework and homework on the specified time.
 
![$changeduedate CSC510 HW2 SEP 25 2024 17:02](https://github.com/SE21-Team2/ClassMateBot/blob/main/data/media/changeduedate.gif?raw=true)

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - changeDue