from __future__ import print_function

import os.path
import datetime
import pandas
import discord
import asyncio
from discord.ext import commands, tasks

from google.auth.transport.requests import Request
from datetime import timedelta, datetime, date
from google.oauth2.credentials import Credentials
from urllib.request import urlopen
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pdfkit
import pandas as pd

class Calendar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.checkForEvents.start()
        

    def credsSetUp(self):
        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/calendar']

        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        return creds

    async def listCalendarEvents(self):
        creds = self.credsSetUp()
        try:
            service = build('calendar', 'v3', credentials=creds)

            # Call the Calendar API
            now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            print('Getting the upcoming 10 events')
            events_result = service.events().list(calendarId='primary', timeMin=now,
                                                maxResults=10, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                print('No upcoming events found.')
                return
            return events

        except HttpError as error:
            print('An error occurred: %s' % error)
    
    @commands.command(name="addCalendarEvent")
    async def addCalendarEvent(self, ctx, name, location, description):
        creds = self.credsSetUp()
        try:
            service = build('calendar', 'v3', credentials=creds)
            event = {
                "summary" : name,
                "location": location,
                "description": description,
                "colorId": 4,
                'start': {
                    'dateTime': '2023-10-28T17:00:00-07:00',
                    'timeZone': 'America/New_York',
                },
                'end': {
                    'dateTime': '2023-10-28T17:00:00-07:00',
                    'timeZone': 'America/New_York',
                },
            }
            event = service.events().insert(calendarId="primary", body=event).execute()

        except HttpError as error:
            print('An error occurred: %s' % error)
    # -----------------------------------------------------------------------------------------------------------------
    #    Function: getiCalDownload(self, ctx)
    #    Description: sends an ics file of the class calendar to the channel the command was issued in
    #    Inputs:
    #       - ctx: context of the command
    #    Outputs:
    #       - The ics file of the calendar
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name="getiCalDownload", help="Enter the command to receive an ics"
                                                " file of the calendar$getiCalDownload")
    async def getiCalDownload(self, ctx):
        # Get the calendar in ics format
        url = os.getenv("CALENDAR_ICS")
        text = urlopen(url).read().decode("iso-8859-1")
        #parse the received text to remove all \n characters
        newText = ""
        for character in text:
            if (character != "\n"):
                newText = newText + character
        #write to the ics file
        f = open(os.getenv("CALENDAR_PATH") + "ical.ics", "w")
        f.write(newText)
        f.close
        await ctx.send(file=discord.File(os.getenv("CALENDAR_PATH") + "ical.ics"))

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: getPdfDownload(self, ctx)
    #    Description: sends an pdf file of the class calendar to the channel the command was issued in
    #    Inputs:
    #       - ctx: context of the command
    #    Outputs:
    #       - The pdf file of the calendar
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command(name="getPdfDownload", help="Enter the command to receive an ics"
                                                " file of the calendar$getiCalDownload")
    async def getPdfDownload(self, ctx):
        creds = self.credsSetUp()
        try:
            service = build('calendar', 'v3', credentials=creds)
            # Call the Calendar API
            now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            events_result = service.events().list(calendarId='primary', timeMin=now,
                                                maxResults=150, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                print('No upcoming events found.')
                return
            calEvents = []
            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                end = event["end"].get("dateTime", event["end"].get("date"))
                calEvent = {
                    "Summary":event["summary"],
                    "Start": start,
                    "End":end
                }
                calEvents.append(calEvent)
            df = pd.DataFrame(calEvents)
            htmlCal = df.to_html()
            pdfkit.from_string(htmlCal, os.getenv("CALENDAR_PATH") + "calendar.pdf")
            await ctx.send(file=discord.File(os.getenv("CALENDAR_PATH") + "calendar.pdf"))

        except HttpError as error:
            print('An error occurred: %s' % error)
    
    @tasks.loop(seconds=5)
    async def checkForEvents(self):
        creds = self.credsSetUp()
        try:
            service = build('calendar', 'v3', credentials=creds)
            # Call the Calendar API
            now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            events_result = service.events().list(calendarId='primary', timeMin=now,
                                                maxResults=150, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])
            summary = ""
            for event in events:
                dt = datetime.strptime((event["start"]["dateTime"])[0:18], "%Y-%m-%dT%H:%M:%S")
                if (dt.day == date.today().day and dt.year == date.today().year):
                    summary = summary + event["summary"] + ","
            if (len(summary) != 0):
                for guild in self.bot.guilds:
                    for channel in guild.text_channels:
                        if (channel.name == "general"):
                            await channel.send("@everyone " + summary + "due TODAY!")
                            break
        except HttpError as error:
            print('An error occurred: %s' % error)

    @checkForEvents.before_loop
    async def checkForNewDay(self):
        hour = 23
        minute = 23
        await self.bot.wait_until_ready()
        now = datetime.now()
        future = datetime(now.year, now.month, now.day, hour, minute)
        if now.hour >= hour and now.minute > minute:
            future += timedelta(days=1)
        await asyncio.sleep((future-now).seconds)
    


async def setup(bot):
    n = Calendar(bot)
    await bot.add_cog(n)

