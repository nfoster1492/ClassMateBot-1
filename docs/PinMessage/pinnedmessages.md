# About $pinnedMessages
This command lets the student to retrieve all the pinned messages from their private pinning board with an optional given tagname.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/pinning.py).

# Code Description
## Functions
retrieveMessages(self, ctx, tagname: str = ""):
This function takes as arguments the values provided by the constructor through self, context in which the command was called, the optional tag-name of the pinned message(s).

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is 
enter the command 'pinnedmessage'. You can also add the optional tagname of the messages to get all messages with the tagname.
```
$pinnedMessages TAGNAME(optional) 
$pinnedMessages HW
```
Successful execution of this command will list all the pinned messages or the ones with the given tagname.

![image](https://user-images.githubusercontent.com/32313919/140255106-07a4d952-4fb7-48c2-964e-b340fb2b0829.png)

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - getPinnedMessages
