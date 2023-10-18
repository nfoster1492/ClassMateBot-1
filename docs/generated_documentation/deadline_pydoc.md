# Table of Contents

* [deadline](#deadline)
  * [Deadline](#deadline.Deadline)
    * [timenow](#deadline.Deadline.timenow)
    * [timenow\_error](#deadline.Deadline.timenow_error)
    * [duedate](#deadline.Deadline.duedate)
    * [duedate\_error](#deadline.Deadline.duedate_error)
    * [deleteReminder](#deadline.Deadline.deleteReminder)
    * [deleteReminder\_error](#deadline.Deadline.deleteReminder_error)
    * [changeduedate](#deadline.Deadline.changeduedate)
    * [changeduedate\_error](#deadline.Deadline.changeduedate_error)
    * [duethisweek](#deadline.Deadline.duethisweek)
    * [duethisweek\_error](#deadline.Deadline.duethisweek_error)
    * [duetoday](#deadline.Deadline.duetoday)
    * [duetoday\_error](#deadline.Deadline.duetoday_error)
    * [coursedue](#deadline.Deadline.coursedue)
    * [coursedue\_error](#deadline.Deadline.coursedue_error)
    * [listreminders](#deadline.Deadline.listreminders)
    * [listreminders\_error](#deadline.Deadline.listreminders_error)
    * [overdue](#deadline.Deadline.overdue)
    * [overdue\_error](#deadline.Deadline.overdue_error)
    * [clearallreminders](#deadline.Deadline.clearallreminders)
    * [clearallreminders\_error](#deadline.Deadline.clearallreminders_error)
    * [clearoverdue](#deadline.Deadline.clearoverdue)
    * [clearoverdue\_error](#deadline.Deadline.clearoverdue_error)
    * [send\_reminders\_day](#deadline.Deadline.send_reminders_day)
    * [before](#deadline.Deadline.before)
    * [send\_reminders\_hour](#deadline.Deadline.send_reminders_hour)
  * [setup](#deadline.setup)

<a id="deadline"></a>

# deadline

<a id="deadline.Deadline"></a>

## Deadline Objects

```python
class Deadline(commands.Cog)
```

<a id="deadline.Deadline.timenow"></a>

#### timenow

```python
@commands.command(
    name="timenow",
    help="put in current time to get offset needed for proper "
    "datetime notifications $timenow MMM DD YYYY HH:MM ex. $timenow SEP 25 2024 17:02",
)
async def timenow(ctx, *, date: str)
```

Gets offset for proper datetime notifications compared to UTC

<a id="deadline.Deadline.timenow_error"></a>

#### timenow\_error

```python
@timenow.error
async def timenow_error(ctx, error)
```

Error handling for timenow command

<a id="deadline.Deadline.duedate"></a>

#### duedate

```python
@commands.has_role("Instructor")
@commands.command(
    name="duedate",
    help=
    "add reminder and due-date $duedate CLASSNAME NAME MMM DD YYYY optional(HH:MM) optional(TIMEZONE)"
    "ex. $duedate CSC510 HW2 SEP 25 2024 17:02 EST",
)
async def duedate(ctx, coursename: str, hwcount: str, *, date: str)
```

Add reminder for specified course, assignment, and date

<a id="deadline.Deadline.duedate_error"></a>

#### duedate\_error

```python
@duedate.error
async def duedate_error(ctx, error)
```

Error handling for duedate command

<a id="deadline.Deadline.deleteReminder"></a>

#### deleteReminder

```python
@commands.has_role("Instructor")
@commands.command(
    name="deletereminder",
    pass_context=True,
    help="delete a specific reminder using course name and reminder name using "
    "$deletereminder CLASSNAME HW_NAME ex. $deletereminder CSC510 HW2 ",
)
async def deleteReminder(ctx, courseName: str, hwName: str)
```

Deletes a specified reminder

<a id="deadline.Deadline.deleteReminder_error"></a>

#### deleteReminder\_error

```python
@deleteReminder.error
async def deleteReminder_error(ctx, error)
```

Error handling for deleteReminder

<a id="deadline.Deadline.changeduedate"></a>

#### changeduedate

```python
@commands.has_role("Instructor")
@commands.command(
    name="changeduedate",
    pass_context=True,
    help=
    "update the assignment date. $changeduedate CLASSNAME HW_NAME MMM DD YYYY optional(HH:MM) optional(TIMEZONE)"
    "ex. $changeduedate CSC510 HW2 SEP 25 2024 17:02 EST",
)
async def changeduedate(ctx, classid: str, hwid: str, *, date: str)
```

Updates an assignment's due date in the database

<a id="deadline.Deadline.changeduedate_error"></a>

#### changeduedate\_error

```python
@changeduedate.error
async def changeduedate_error(ctx, error)
```

Error handling for changeduedate command

<a id="deadline.Deadline.duethisweek"></a>

#### duethisweek

```python
@commands.command(
    name="duethisweek",
    pass_context=True,
    help="check all the homeworks that are due this week $duethisweek",
)
async def duethisweek(ctx)
```

Checks all homeworks or assignments due this week

<a id="deadline.Deadline.duethisweek_error"></a>

#### duethisweek\_error

```python
@duethisweek.error
async def duethisweek_error(ctx, error)
```

Error handling for duethisweek command

<a id="deadline.Deadline.duetoday"></a>

#### duetoday

```python
@commands.command(
    name="duetoday",
    pass_context=True,
    help="check all the reminders that are due today $duetoday",
)
async def duetoday(ctx)
```

Checks for all reminders that are due today

<a id="deadline.Deadline.duetoday_error"></a>

#### duetoday\_error

```python
@duetoday.error
async def duetoday_error(ctx, error)
```

Error handling for duetoday command

<a id="deadline.Deadline.coursedue"></a>

#### coursedue

```python
@commands.command(
    name="coursedue",
    pass_context=True,
    help=
    "check all the reminders that are due for a specific course $coursedue coursename "
    "ex. $coursedue CSC505",
)
async def coursedue(ctx, courseid: str)
```

Displays a list of all reminders due for a specific course

<a id="deadline.Deadline.coursedue_error"></a>

#### coursedue\_error

```python
@coursedue.error
async def coursedue_error(ctx, error)
```

Error handling for coursedue command

<a id="deadline.Deadline.listreminders"></a>

#### listreminders

```python
@commands.command(name="listreminders",
                  pass_context=True,
                  help="lists all reminders")
async def listreminders(ctx)
```

Displays user with list of all reminders

<a id="deadline.Deadline.listreminders_error"></a>

#### listreminders\_error

```python
@listreminders.error
async def listreminders_error(ctx, error)
```

Error handling for listreminders command

<a id="deadline.Deadline.overdue"></a>

#### overdue

```python
@commands.command(name="overdue",
                  pass_context=True,
                  help="lists overdue reminders")
async def overdue(ctx)
```

Displays list of homeworks and assignments that are overdue

<a id="deadline.Deadline.overdue_error"></a>

#### overdue\_error

```python
@overdue.error
async def overdue_error(ctx, error)
```

Error handling for overdue command

<a id="deadline.Deadline.clearallreminders"></a>

#### clearallreminders

```python
@commands.command(name="clearreminders",
                  pass_context=True,
                  help="deletes all reminders")
async def clearallreminders(ctx)
```

Clears all reminders from database

<a id="deadline.Deadline.clearallreminders_error"></a>

#### clearallreminders\_error

```python
@clearallreminders.error
async def clearallreminders_error(ctx, error)
```

Error handling for clearreminders command

<a id="deadline.Deadline.clearoverdue"></a>

#### clearoverdue

```python
@commands.command(name="clearoverdue",
                  pass_context=True,
                  help="deletes overdue reminders")
async def clearoverdue(ctx)
```

Clears all overdue reminders from database

<a id="deadline.Deadline.clearoverdue_error"></a>

#### clearoverdue\_error

```python
@clearoverdue.error
async def clearoverdue_error(ctx, error)
```

Error handling for clearoverdue

<a id="deadline.Deadline.send_reminders_day"></a>

#### send\_reminders\_day

```python
@tasks.loop(hours=24)
async def send_reminders_day()
```

Task running once per day to send a reminder for assignments due

<a id="deadline.Deadline.before"></a>

#### before

```python
@send_reminders_day.before_loop
async def before()
```

Task that runs once per day and waits until 8am EST to send reminders via send_reminders_day function

<a id="deadline.Deadline.send_reminders_hour"></a>

#### send\_reminders\_hour

```python
@tasks.loop(hours=1)
async def send_reminders_hour()
```

Task that runs once per hour ans sends a reminder for assignments due

<a id="deadline.setup"></a>

#### setup

```python
async def setup(bot)
```

Adds the file to the bot's cog system

