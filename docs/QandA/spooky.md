# About $spooky _(New Project 3 Command)_

Counts the number of ghost (hidden) and zombie (deleted) questions in the channel. Just for fun, but may be useful.

```
Zombies are questions that were manually deleted from the channel. They need to be
assigned new message IDs in order to be restored--that is, they need to be reposted.
Ghosts are questions that were deleted (or hidden) with the deleteQuestion command.
Because their message IDs remain the same, their contents can just be unhidden.
```

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/qanda.py](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/cogs/qanda.py).

# Code Description
## Functions
countGhosts(self, ctx): <br>
This function takes as arguments the values provided by the constructor through self and context in which the command was called.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
the #q-and-a channel channel, enter the command `$spooky`.

```
$spooky
```
Successful execution of this command will DM the user the number of ghosts and zombies present in the channel.

`![image](SCREENSHOT)` 