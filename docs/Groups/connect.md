# About $connect
This command lets the user create private text channels for all groups with members. 
Note: Running this command will delete all current private group channels!

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/groups.py).

# Code Description
## Functions
def connect(self, ctx): <br>
This function takes as arguments the values provided by the constructor through self and context in which the command was called.

# How to run it?
In any channel of the server, you can create a private text channel for all occupied groups in the server by typing `connect`.
```
$connect
```
Successful execution of this command will create private text channels for all occupied groups for the users in the server.

![image](https://user-images.githubusercontent.com/89809302/140448623-d3cb5658-b3cc-4ffa-a984-679fc20fbc9f.png)

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - connectGroups
 