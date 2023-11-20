# About $timeNow
This command lets the user get the offset needed for proper datetime reminders in UTC. 

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/deadline.py).

# Code Description
## Functions
timeNow(self, ctx, *, date: str): <br>
This function takes as arguments the values provided by the constructor through self, the context in which the command was called, and the current date and 24-hour time. 

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'timeNow' with the current date and 24-hour time:

```
$timeNow MMM DD YYYY HH:MM
$timeNow SEP 25 2024 17:02
```
Successful execution of this command will get the offset from the user's current time with UTC.

![image](https://user-images.githubusercontent.com/32313919/140256682-5d86ca22-402f-417d-b9f6-4328565cd1b4.png)

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - currTime
 - setCurrTime
