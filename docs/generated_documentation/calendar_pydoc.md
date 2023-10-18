# Table of Contents

* [calendar](#calendar)
  * [Calendar](#calendar.Calendar)
    * [credsSetUp](#calendar.Calendar.credsSetUp)
    * [addCalendarEvent](#calendar.Calendar.addCalendarEvent)
    * [clearCalendar](#calendar.Calendar.clearCalendar)
    * [getiCalDownload](#calendar.Calendar.getiCalDownload)
    * [getPdfDownload](#calendar.Calendar.getPdfDownload)
    * [checkForEvents](#calendar.Calendar.checkForEvents)
    * [subscribeCalendar](#calendar.Calendar.subscribeCalendar)
    * [removeCalendar](#calendar.Calendar.removeCalendar)
  * [setup](#calendar.setup)

<a id="calendar"></a>

# calendar

<a id="calendar.Calendar"></a>

## Calendar Objects

```python
class Calendar(commands.Cog)
```

<a id="calendar.Calendar.credsSetUp"></a>

#### credsSetUp

```python
def credsSetUp()
```

Set up Google Calendar with authentication

<a id="calendar.Calendar.addCalendarEvent"></a>

#### addCalendarEvent

```python
@commands.command(
    name="addCalendarEvent",
    help="Add an event to the course calendar using the format"
    ": $addCalendarEvent NAME DESCRIPTION DATE/TIME",
)
async def addCalendarEvent(ctx, name, description, eventTime)
```

Adds specified event to shared Google Calendar

<a id="calendar.Calendar.clearCalendar"></a>

#### clearCalendar

```python
@commands.command(name="clearCalendar", help="Clear all events from calendar")
async def clearCalendar(ctx)
```

Clears all events from shared Google Calendar

<a id="calendar.Calendar.getiCalDownload"></a>

#### getiCalDownload

```python
@commands.command(
    name="getiCalDownload",
    help="Enter the command to receive an ics"
    " file of the calendar$getiCalDownload",
)
async def getiCalDownload(ctx)
```

Generates an ICAL file of the Google Calendar

<a id="calendar.Calendar.getPdfDownload"></a>

#### getPdfDownload

```python
@commands.command(
    name="getPdfDownload",
    help="Enter the command to receive an ics"
    " file of the calendar$getiCalDownload",
)
async def getPdfDownload(ctx)
```

Sends a pdf file of the class calendar to the Discord Channel

<a id="calendar.Calendar.checkForEvents"></a>

#### checkForEvents

```python
@tasks.loop(hours=24)
async def checkForEvents()
```

Checks calendar daily for the events due that day

<a id="calendar.Calendar.subscribeCalendar"></a>

#### subscribeCalendar

```python
@commands.command(
    name="subscribeCalendar",
    help=
    "Adds user to shared Google Calendar. Ex: subscribeCalendar john.doe@gmail.com",
)
async def subscribeCalendar(ctx, userEmail)
```

Adds user to shared Google Calendar

<a id="calendar.Calendar.removeCalendar"></a>

#### removeCalendar

```python
@commands.has_role("Instructor")
@commands.command(
    name="removeCalendar",
    help=
    "Removes user from shared Google Calendar. Ex: removeCalendar john.doe@gmail.com",
)
async def removeCalendar(ctx, userEmail)
```

Removes user from shared Google Calendar

<a id="calendar.setup"></a>

#### setup

```python
async def setup(bot)
```

Adds the file to the bot's cog system

