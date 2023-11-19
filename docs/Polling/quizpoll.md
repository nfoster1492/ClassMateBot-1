# About $quizPoll

This command allows the user to start a quiz-style reaction poll with a given title and six options or less.

## Changes

This command was introduced by [CSC510-Group-25](https://github.com/CSC510-Group-25/ClassMateBot/).

# Location of Code
The code that implements the above mentioned functionality is located in [cogs/polling.py](https://github.com/maddaicita/ClassMateBot-1.1/tree/main/cogs/polling.py).

# Code Description
## Functions
quizPoll(self, ctx, title: str, *, ops) <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called, a title string, and two to six options.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. From any channel,
 enter the command  
 `$quizPoll "TITLE" [option 1] ... [option 6]`.

 Note that you can also enter:  
`$quizPoll "TITLE" [option 1] [option 2]`  
`$quizPoll "TITLE" [option 1] [option 2] [option 3]`

You may have six options at most. At least two options are needed to run this command.


```
$quizPoll "TITLE" [option 1] ... [option 6]
$quizPoll "TITLE" [1 fish] [2 fish] [redfish] [bluefish]
```
Successful execution of this command will embed a quiz poll into the channel.

Note: BananaBot is also a ClassMateBot

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj3media/polling/quizpoll1.png?raw=true" width="500">

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj3media/polling/quizpoll2.png?raw=true" width="500">
