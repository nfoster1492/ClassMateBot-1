# About $clearOverdue
Clears overdue reminders from the database. 

## Changes

This command was introduced by [CSC510-Group-25](https://github.com/CSC510-Group-25/ClassMateBot/).

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/deadline.py](https://github.com/maddaicita/ClassMateBot-1.1/tree/main/cogs/deadline.py).

# Code Description
## Functions
clearOverdue(self, ctx): <br>
This function takes as arguments the values provided by the constructor through self and context in which the command was called and deletes any 
past due reminders from the database

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
 the #reminders channel, enter the command `$clearOverdue`.

```
$clearOverdue
```
Successful execution of this command will remove overdue reminders from the database and give a success message.

<img width="607" alt="Screen Shot 2021-12-04 at 10 02 42 AM" src="https://user-images.githubusercontent.com/78971563/144714701-43a806ea-7df6-45bf-a636-8a689add876f.png">
