# Table of Contents

* [polling](#polling)
  * [Poll](#polling.Poll)
    * [quizpoll](#polling.Poll.quizpoll)
    * [quizpoll\_error](#polling.Poll.quizpoll_error)
    * [poll](#polling.Poll.poll)
    * [poll\_error](#polling.Poll.poll_error)
  * [setup](#polling.setup)

<a id="polling"></a>

# polling

<a id="polling.Poll"></a>

## Poll Objects

```python
class Poll(commands.Cog)
```

<a id="polling.Poll.quizpoll"></a>

#### quizpoll

```python
@commands.command(
    name="quizpoll",
    help=
    'Create a multi reaction poll by typing \n$poll "TITLE" [option 1] ... [option 6]\n '
    "Be sure to enclose title with quotes and options with brackets!\n"
    'EX: $quizpoll "I am a poll" [Vote for me!] [I am option 2]',
)
async def quizpoll(ctx, title: str, *, ops)
```

Allows the user to begin quiz polls; that is, multi-reaction polls with listed questions

<a id="polling.Poll.quizpoll_error"></a>

#### quizpoll\_error

```python
@quizpoll.error
async def quizpoll_error(ctx, error)
```

Error handling for quizpoll command

<a id="polling.Poll.poll"></a>

#### poll

```python
@commands.command(
    name="poll",
    help="Create a reaction poll by typing $poll QUESTION\n"
    "EX: $poll What do you think about cats?",
)
async def poll(ctx, *, qs="")
```

Allows the user to create a simple reaction poll with thumbs up, thumbs down, and unsure

<a id="polling.Poll.poll_error"></a>

#### poll\_error

```python
@poll.error
async def poll_error(ctx, error)
```

Error handling for poll command

<a id="polling.setup"></a>

#### setup

```python
async def setup(bot)
```

Adds the file to the bot's cog system

