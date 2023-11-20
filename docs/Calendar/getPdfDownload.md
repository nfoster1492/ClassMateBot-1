# About $getpdfDownload _(Modified Command in Project 2)_
This command lets students download a pdf so that they can import the class calendar into their calendar software of choice. 

# Location of Code
The code that implements the above mentioned gets functionality is located [here](https://github.com/maddaicita/ClassMateBot-1.1/blob/main/cogs/calendar.py)

# Code Description
## Functions
getpdfDownload(self, ctx):: <br>
This function takes as arguments the values provided by the constructor through self, and the context in which the command was called.

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online, and the instructor has been updating the calendar with events. All you have to do is 
enter the command 'getPdfDownload': and the bot will return a file that the student can download
```
$getPdfDownload
```
Successful execution of this command will result in a pdf being sent in the same channel

<img src="https://github.com/maddaicita/ClassMateBot-1.1/blob/main/data/proj2media/getPdfDownload.JPG?raw=true" width=500>

# Aliases

This function can also be called with one or more aliases, or different names reffering to the same function. Here are the aliases for this function:

 - getPdfDownload 
