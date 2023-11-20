# About $gradeRequired _(New Project 2 Command)_
This command lets a student get the grade they need on the next assignment to keep a desired grade in a certain category.
## Changes

This command was introduced by [CSC510-Group-1](https://github.com/nfoster1492/ClassMateBot-1/).

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/grades.py](https://github.com/maddaicita/ClassMateBot-1.1/tree/main/cogs/grades.py).

# Code Description
## Functions
gradeRequired(self, ctx, categoryName: str, pointValue: str, desiredGrade: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, the name of the category the assignment will be part of, the amount of points the next assignment will be worth, and the overall grade desired for the category.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You are a Student. From the general channel, enter the command `$gradeRequired <categoryName> <pointValue> <desiredGrade>`.

```
$gradeRequired CATEGORY_NAME POINT_VALUE DESIRED_GRADE
$gradeRequired tests 200 90
```
Successful execution of this command will DM the student the grade required on the next hypothetical assignment.

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj2media/graderequiredHelp.png?raw=true" width="500">

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - gradeReq
