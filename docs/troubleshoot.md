# Troubleshooting Guide

## Google Calendar Issues

### Invalid Authentication

Until the Google Cloud App is pushed to production, the user that is managing the bot will need to generate a new token every seven days:
1. Delete the `token.json` file from the project root directory.
2. Run one of the calendar commands specified in /docs/Calendar: this will open a browser window allowing you to reauthenticate the application and generate a new `token.json`