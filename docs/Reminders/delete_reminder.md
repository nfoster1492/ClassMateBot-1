# About $deleteReminder
This command lets the user delete a reminder for a specified coursename and homework. 

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/main/cogs/deadline.py).

# Code Description
## Functions
deleteReminder(self, ctx, courseName: str, hwName: str): <br>
This function takes as arguments the values provided by the constructor through self and the context in which the command was called. It also takes homework name as input.

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command '$deleteReminder' with space seperated coursename and homeworkname as a parameter:

```
$deleteReminder coursename homeworkname
$deleteReminder CSC510 HW2
```
Successful execution of this command will delete the reminder for a specified coursework and homework.

![$deleteReminder CSC510 HW2](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/media/deletereminder.gif?raw=true)

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - removeReminder
