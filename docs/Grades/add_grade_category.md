# About $addGradeCategory _(New Project 2 Command)_
This command allows the instructor to add a new grade category with a designated weight
## Changes

This command was introduced by [CSC510-Group-1](https://github.com/nfoster1492/ClassMateBot-1/).

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/grades.py](https://github.com/maddaicita/ClassMateBot-1.1/tree/main/cogs/grades.py).

# Code Description
## Functions
addGradeCategory(self, ctx, categoryname: str, weight: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, the name of the category being added, and the weight of the category being added.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You are an Instructor. From the instructor commands channel, enter the command `$addGradeCategory <category_name> <weight>` with the desired category name and weight.

```
$addGradeCategory CATEGORY_NAME, WEIGHT
$addGradeCategory Tests .5
```
Successful execution of this command will add a grade category into the database with the desired weight. The bot will report on the success or failure of the command.

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj2media/addGradeCategoryHelp.PNG?raw=true" width="500">

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj2media/addGradeCategory.PNG?raw=true" width="500">

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - addCategory
