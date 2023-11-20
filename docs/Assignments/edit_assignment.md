# About $editAssignment _(New Project 2 Command)_
This command lets the instructor edit a new gradeable assignment
## Changes

This command was introduced by [CSC510-Group-1](https://github.com/nfoster1492/ClassMateBot-1/).

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/grades.py](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/assignments.py).

# Code Description
## Functions
editAssignment(self, ctx, assignmentname: str, categoryname: str, points: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, the name of the assignment being edited, the category it will now belong to, and the maximum amount of points now attainable on the assignment.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You are an Instructor. From the instructor commands channel, enter the command `$editAssignment <assignment_name> <category_name> <points>` with the desired assignment name, category, and weight.

```
$editAssignment ASSIGNMENT_NAME CATEGORY_NAME POINTS
$editAssignment test1 tests 100
```
Successful execution of this command will edit an assignment in the database with the given name, with the desired category, and points. The bot will report on the success or failure of the command.

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj2media/editAssignmentHelp.PNG?raw=true" width="500">

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj2media/editAssignment.PNG?raw=true" width="500">

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - editWork
 - editTask
