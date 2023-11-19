# About $spooky

Counts the number of ghost (hidden) and zombie (deleted) questions in the channel. Just for fun, but may be useful.

```
Zombies are questions that were manually deleted from the channel. They need to be
assigned new message IDs in order to be restored--that is, they need to be reposted.
Ghosts are questions that were deleted (or hidden) with the deleteQuestion command.
Because their message IDs remain the same, their contents can just be unhidden.
```

## Changes

This command was introduced by [CSC510-Group-25](https://github.com/CSC510-Group-25/ClassMateBot/).

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/qanda.py](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/qanda.py).

# Code Description
## Functions
countGhosts(self, ctx): <br>
This function takes as arguments the values provided by the constructor through self and context in which the command was called.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
the #q-and-a channel and enter the command `$spooky`.

`$spooky`

Successful execution of this command will DM the user the number of ghosts and zombies present in the channel.


<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj3media/spooky/spooky1.png?raw=true" width="500">

<<<<<<< HEAD
<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/spooky/spooky2.png?raw=true" width="500">

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - getGhostCount
 
=======
<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj3media/spooky/spooky2.png?raw=true" width="500">
>>>>>>> 547f17274859d061ede9c9f942fa239b52de7682
