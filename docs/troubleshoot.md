# Troubleshooting Guide

## Google Calendar Issues

### Invalid Authentication

Until the Google Cloud App is pushed to production, the user that is managing the bot will need to generate a new token every seven days:
1. Delete the `token.json` file from the project root directory.
2. Run one of the calendar commands specified in /docs/Calendar: this will open a browser window allowing you to reauthenticate the application and generate a new `token.json`

## Pytest/Dyptest

### Pytest VS Code issue
If you are on Windows and using VS code to edit the code and your tests are not being picked up by the editor, then follow these [steps](https://stackoverflow.com/questions/54387442/vs-code-not-finding-pytest-tests).

### Dpytest
If you are creating new tests you may find that tests fail for seemingly no reason. One aspect of dpytest that is helpful to know in debugging your failing test is that the messages returned from dpytest are put into a queue. An example of this is the following where in $command1 the bot returns two messages
```
await dpytest.message("$command1")
assert (dpytest.verify().message().content("Command one has run"))
await dpytest.message("$command2")
assert (dpytest.verify().message().content("Command two has run"))
```
Line 4 will fail because the second message from $command1 is at the head of the queue and so is returned instead of the message from $command2. 
