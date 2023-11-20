# About $startupGroups
This command lets the user set up the roles required for the grouping. This is required as a part of the group making/joining/leaving functionality.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/groups.py).

# Code Description
## Functions
def startupGroups(self, ctx): <br>
This function takes as arguments the values provided by the constructor through self and context in which the command was called.

# How to run it?
In any channel of the server, you can set upp the roles for the group by typing `startupGroups`. This needs to be done only ONCE!
```
$startupGroups
```
Successful execution of this command will create 100 unassigned group roles for the users in the server.

![image](https://user-images.githubusercontent.com/89809302/140447594-468f1c7b-feaf-449a-bdcb-ac70a5bf066e.png)

![image](https://user-images.githubusercontent.com/89809302/140447634-2ba168bf-9b27-4b6a-9a8a-af5ca3da9182.png)

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - makeGroupRoles
