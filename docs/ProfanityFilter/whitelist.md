# About $whitelist

Command that adds a word or sentence to the censor whitelist. Instructor only.

## Changes

This command was introduced by [CSC510-Group-25](https://github.com/CSC510-Group-25/ClassMateBot/).

# Location of Code
The code that implements the above mentioned functionality is located in [bot.py](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/bot.py).

# Code Description
## Functions
whitelistWord(ctx, *, word=''):: <br>
This function takes as arguments the context in which the command was called, and a word or sentence to 
 add to the whitelist.

# How to run it? (Small Example)
You are in the server that has the Classmate Bot active and online. You go to
 the #instructor-commands channel and enter the command `$whitelist WORD`.

```
$whitelist WORD
$whitelist vodka
$whitelist a lot of words
```
Successful execution of this command will prevent the word or sentence from being censored.

Note: BananaBot is also a ClassMateBot

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj3media/profanity/filterdemo1.png?raw=true" width="500">

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj3media/profanity/filterdemo2?raw=true" width="500">

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj3media/profanity/vodka.png?raw=true" width="500">

<<<<<<< HEAD
<img src="https://github.com/CSC510-Group-25/ClassMateBot/blob/group25-command-docs/data/proj3media/profanity/filterdemo3.png?raw=true" width="500">

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - whitelist
 - addCensorWord
 
=======
<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj3media/profanity/filterdemo3.png?raw=true" width="500">
>>>>>>> 547f17274859d061ede9c9f942fa239b52de7682
