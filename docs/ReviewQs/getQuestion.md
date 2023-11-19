# About $getQuestion
This command lets users get a random review question added by instructors. The answer to the question will be hidden as a spoiler.

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/reviewQs.py](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/reviewQs.py).

# Code Description
## Functions
getQuestion(self, ctx): <br>
This function takes as arguments the values provided by the constructor through self and context in which the command was called.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You enter the command `getQuestion`. 
```
$getQuestion
```
Successful execution of this command will print a random review question from the guild database.

![image](https://user-images.githubusercontent.com/32313919/140245925-22769537-ef22-420f-9ed2-b9153a71938e.png)

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - getReviewQuestion 
 