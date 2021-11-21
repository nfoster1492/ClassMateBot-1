# About $deleteAllQA _(New Project 3 Command)_

Deletes all questions and answers from the database and channel (for that server only), including ghost (hidden) and zombie (deleted) questions. Instructor only.

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
deleteAllQAs(self, ctx): <br>
This function takes as arguments the values provided by the constructor through self and the context in which the command was called.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
the #q-and-a channel channel, enter the command `$deleteAllQA`.

```
$deleteAllQA
```
Successful execution of this command will remove all questions and answers from the QA channel and database.

`![image](SCREENSHOT)` 
