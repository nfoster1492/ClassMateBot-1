# About $getiCalDownload _(Modified Command in Project 2)_
This command lets students download an .ics file so that they can import the class calendar into their calendar software of choice. 

# Location of Code
The code that implements the above mentioned gets functionality is located [here](https://github.com/nfoster1492/ClassMateBot-1/blob/main/cogs/calendar.py)

# Code Description
## Functions
getiCalDownload(self, ctx):: <br>
This function takes as arguments the values provided by the constructor through self, and the context in which the command was called.

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online, and the instructor has been updating the calendar with events. All you have to do is 
enter the command 'getiCalDownload': and the bot will return a file that the student can download
```
$getiCalDownload
```
Successful execution of this command will result in an .ics file being sent in the same channel

![image](https://user-images.githubusercontent.com/32313919/140243037-8e4c192c-5842-4fd9-85b0-6cccaf3f74ab.png)
