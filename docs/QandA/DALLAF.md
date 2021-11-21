# About $DALLAF (deleteAllAnswersFor) _(New Project 3 Command)_

This command lets instructors remove all answers for a question in the #q-and-a channel.
Deletes all answers for a question. Instructor only.

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/qanda.py](https://github.com/CSC510-Group-25/ClassMateBot/blob/main/cogs/qanda.py).

# Code Description
## Functions
deleteAllAnsFor(self, ctx, num): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, and the number of the question to delete answers for.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
the #q-and-a channel and enter the command `$DALLAF <q_num>`.

Before deletion, archive the question and its answers with
`$getAnswersFor QUESTION_NUMBER`

Or, if it's a ghost or zombie:
`$channelGhost QUESTION_NUMBER` 

```
$DALLAF <q_num>
$DALLAF 7
```
Successful execution of this command will delete all answers for the question on the channel and in the database, and DM the user the number of answers that were deleted.

`![image](SCREENSHOTS IN data/proj3media/dallaf/)` 
