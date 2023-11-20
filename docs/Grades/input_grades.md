# About $inputGrades _(New Project 2 Command)_
This command allows the instructor to input grades into the system for a given assignment.

## Changes

This command was introduced by [CSC510-Group-1](https://github.com/nfoster1492/ClassMateBot-1/).

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/grades.py](https://github.com/maddaicita/ClassMateBot-1.1/tree/main/cogs/grades.py).

# Code Description
## Functions
inputGrades(self, ctx, assignmentname: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, the assignment that the grades are being input for, and a csv file that is attached with a mappin gof the student names to the grades.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You are an Instructor. From the instructor commands channel, enter the command `$inputGrades <assignment_name>` and attach a csv file with two columns, the first being student names and the second being the grades for the assignment

```
$inputGrades ASSIGNMENT_NAME
$inputGrades HW1
```
Successful execution of this command will update the grades in the database and report to the instructor the amount that were added, if any were skipped over, and the amount of grades that were edited.

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj2media/inputGradesHelp.PNG?raw=true" width="500">

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj2media/inputGrades.PNG?raw=true" width="500">

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - feedGrades
