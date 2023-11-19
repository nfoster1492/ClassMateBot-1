# About $courseDue
This command lets the user display all the homeworks that are due for a specific course. 

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/deadline.py).

# Code Description
## Functions
courseDue(self, ctx, courseid: str): <br>
This function takes as arguments the values provided by the constructor through self and the context in which the command was called. It also takes course name as input.

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command '$courseDue' with coursename as a parameter:

```
$coursedue CSC505
```
Successful execution of this command will display all the homeworks that are due on that day.

![$coursedue](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/media/coursedue.gif?raw=true)