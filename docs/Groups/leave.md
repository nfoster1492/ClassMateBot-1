# About $leave
This command lets the student leave their current group. This is used to ensure that if a member switches groups or drops the class, then they can be removed from a group.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/groups.py).

# Code Description
## Functions
leave(self, ctx): <br>
This function takes as arguments the values provided by the constructor through self and context in which the command was called. No additional arguments are needed.

# How to run it? (Small Example)
Let's say that you are in the server or bot dm that has the Classmate Bot active and online. All you have to do is 
enter the command 'leave'.
```
$leave
```
Successful execution of this command will return a message saying you have been removed from the group.

![image](https://user-images.githubusercontent.com/32313919/140252700-18d6a7bd-11ad-468c-beee-a597ed5f4d10.png)

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - leaveGroup
 