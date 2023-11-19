# About $deleteGradeCategory _(New Project 2 Command)_
This command allows the instructor to delete an existing grade category with a designated weight
## Changes

This command was introduced by [CSC510-Group-1](https://github.com/nfoster1492/ClassMateBot-1/).

# Location of Code
The code that implements the above mentioned functionality is located in `[cogs/grades.py](https://github.com/maddaicita/ClassMateBot-1.1/tree/main/cogs/grades.py)`.

# Code Description
## Functions
deleteGradeCategory(self, ctx, categoryname: str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, and the name of the category being deleted

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You are an Instructor. From the instructor commands channel, enter the command `$deleteGradeCategory <category_name>` with the desired category to delete.

```
$deleteGradeCategory CATEGORY_NAME
$deleteGradeCategory Tests
```
Successful execution of this command will delete a grade category in the database. The bot will report on the success or failure of the command.

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj2media/deleteGradeCategoryHelp.PNG?raw=true" width="500">

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj2media/deleteGradeCategory.PNG?raw=true" width="500">