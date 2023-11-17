# About $deleteAssignment _(New Project 2 Command)_
This command lets the instructor delete an existing gradeable assignment
## Changes

This command was introduced by [CSC510-Group-1](https://github.com/nfoster1492/ClassMateBot-1/).

# Location of Code
The code that implements the above mentioned functionality is located in `[cogs/grades.py](https://github.com/nfoster1492/ClassMateBot-1/tree/main/cogs/assignments.py)`.

# Code Description
## Functions
deleteAssignment(self, ctx, assignmentname: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, and the name of the assignment being deleted.
# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You are an Instructor. From the instructor commands channel, enter the command `$deleteAssignment <assignment_name>` with the desired assignment name.

```
$deleteAssignment ASSIGNMENT_NAME
$deleteAssignment test1
```
Successful execution of this command will delete an assignment from the database. The bot will report on the success or failure of the command.

<img src="https://github.com/nfoster1492/ClassMateBot-1/blob/main/data/proj2media/deleteAssignmentHelp.PNG?raw=true" width="500">

<img src="https://github.com/nfoster1492/ClassMateBot-1/blob/main/data/proj2media/deleteAssignment.PNG?raw=true" width="500">