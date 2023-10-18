# Table of Contents

* [qanda](#qanda)
  * [Qanda](#qanda.Qanda)
    * [askQuestion](#qanda.Qanda.askQuestion)
    * [ask\_error](#qanda.Qanda.ask_error)
    * [answer](#qanda.Qanda.answer)
    * [answer\_error](#qanda.Qanda.answer_error)
    * [deleteAllAnsFor](#qanda.Qanda.deleteAllAnsFor)
    * [deleteAllAnsFor\_error](#qanda.Qanda.deleteAllAnsFor_error)
    * [getAllAnsFor](#qanda.Qanda.getAllAnsFor)
    * [getAllAnsFor\_error](#qanda.Qanda.getAllAnsFor_error)
    * [archiveQA](#qanda.Qanda.archiveQA)
    * [archiveqa\_error](#qanda.Qanda.archiveqa_error)
    * [deleteAllQAs](#qanda.Qanda.deleteAllQAs)
    * [deleteAllQAs\_error](#qanda.Qanda.deleteAllQAs_error)
    * [deleteOneQuestion](#qanda.Qanda.deleteOneQuestion)
    * [deleteOneQuestion\_error](#qanda.Qanda.deleteOneQuestion_error)
    * [channelOneGhost](#qanda.Qanda.channelOneGhost)
    * [channelOneGhost\_error](#qanda.Qanda.channelOneGhost_error)
    * [channelGhostQs](#qanda.Qanda.channelGhostQs)
    * [channelGhostQs\_error](#qanda.Qanda.channelGhostQs_error)
    * [unearthZombieQs](#qanda.Qanda.unearthZombieQs)
    * [unearthZombieQs\_error](#qanda.Qanda.unearthZombieQs_error)
    * [restoreGhost](#qanda.Qanda.restoreGhost)
    * [restoreGhost\_error](#qanda.Qanda.restoreGhost_error)
    * [countGhosts](#qanda.Qanda.countGhosts)
    * [countGhosts\_error](#qanda.Qanda.countGhosts_error)
  * [setup](#qanda.setup)

<a id="qanda"></a>

# qanda

<a id="qanda.Qanda"></a>

## Qanda Objects

```python
class Qanda(commands.Cog)
```

<a id="qanda.Qanda.askQuestion"></a>

#### askQuestion

```python
@commands.command(
    name="ask",
    help=
    "Ask question. Please put question text in quotes. Add *anonymous* or *anon* if desired."
    'EX: $ask /"When is the exam?/" anonymous',
)
async def askQuestion(ctx, qs: str, anonymous="")
```

Takes question from the user the reposts it anonymously and numbered

<a id="qanda.Qanda.ask_error"></a>

#### ask\_error

```python
@askQuestion.error
async def ask_error(ctx, error)
```

Error handling for ask command

<a id="qanda.Qanda.answer"></a>

#### answer

```python
@commands.command(
    name="answer",
    help=
    "Answer question. Please put answer text in quotes. Add *anonymous* or *anon* if desired."
    'EX: $answer 1 /"Oct 12/" anonymous',
)
async def answer(ctx, num, ans: str, anonymous="")
```

Adds user to specific question and post anonymously

<a id="qanda.Qanda.answer_error"></a>

#### answer\_error

```python
@answer.error
async def answer_error(ctx, error)
```

Error handling for answer command

<a id="qanda.Qanda.deleteAllAnsFor"></a>

#### deleteAllAnsFor

```python
@commands.has_role("Instructor")
@commands.command(
    name="DALLAF",
    help="(PLACEHOLDER NAME) Delete all answers for a question.\n"
    "EX: $DALLAF 1\n"
    "THIS ACTION IS IRREVERSIBLE.\n"
    "Before deletion, archive the question and its answers with\n"
    "$getAnswersFor QUESTION_NUMBER",
)
async def deleteAllAnsFor(ctx, num)
```

Lets instructor delete all answers for a question

<a id="qanda.Qanda.deleteAllAnsFor_error"></a>

#### deleteAllAnsFor\_error

```python
@deleteAllAnsFor.error
async def deleteAllAnsFor_error(ctx, error)
```

Error handling for deleteAllAnswersFor command

<a id="qanda.Qanda.getAllAnsFor"></a>

#### getAllAnsFor

```python
@commands.command(
    name="getAnswersFor",
    help="Get a question and all its answers\n"
    "EX: $getAnswersFor 1",
)
async def getAllAnsFor(ctx, num)
```

Gets all answers for a question and DMs them to the user

<a id="qanda.Qanda.getAllAnsFor_error"></a>

#### getAllAnsFor\_error

```python
@getAllAnsFor.error
async def getAllAnsFor_error(ctx, error)
```

Error handling for getAllAnswersFor command

<a id="qanda.Qanda.archiveQA"></a>

#### archiveQA

```python
@commands.command(
    name="archiveQA",
    help="(PLACEHOLDER NAME) DM all questions and their answers\n"
    "EX: $archiveQA",
)
async def archiveQA(ctx)
```

DM all questions and their answers to the user

<a id="qanda.Qanda.archiveqa_error"></a>

#### archiveqa\_error

```python
@archiveQA.error
async def archiveqa_error(ctx, error)
```

Error handling for archiveQA command

<a id="qanda.Qanda.deleteAllQAs"></a>

#### deleteAllQAs

```python
@commands.has_role("Instructor")
@commands.command(
    name="deleteAllQA",
    help="Delete all questions and answers from the database and channel.\n"
    "EX: $deleteAllQA\n"
    "THIS COMMAND IS IRREVERSIBLE.\n"
    "BE SURE TO ARCHIVE ALL QUESTIONS BEFORE DELETION.\n"
    "To archive, use the $unearthZombies command followed by $allChannelGhosts,"
    " and then use $archiveQA.",
)
async def deleteAllQAs(ctx)
```

Deletes all quetsions and answers from the database and channel

<a id="qanda.Qanda.deleteAllQAs_error"></a>

#### deleteAllQAs\_error

```python
@deleteAllQAs.error
async def deleteAllQAs_error(ctx, error)
```

Error handling for deleteAllQA command

<a id="qanda.Qanda.deleteOneQuestion"></a>

#### deleteOneQuestion

```python
@commands.has_role("Instructor")
@commands.command(
    name="deleteQuestion",
    help="Delete (hide) one question but leave answers untouched."
    " Leaves database ghosts.\n"
    "EX: $deleteQuestion QUESTION_NUMBER\n",
)
async def deleteOneQuestion(ctx, num)
```

Lets the instructor delete one question, but leave the answers untouched

<a id="qanda.Qanda.deleteOneQuestion_error"></a>

#### deleteOneQuestion\_error

```python
@deleteOneQuestion.error
async def deleteOneQuestion_error(ctx, error)
```

Error handling for deleteQuestion command

<a id="qanda.Qanda.channelOneGhost"></a>

#### channelOneGhost

```python
@commands.has_role("Instructor")
@commands.command(
    name="channelGhost",
    help=
    "Gets a specific ghost (question deleted with command) and all its answers.\n"
    "EX: $channelGhost 1",
)
async def channelOneGhost(ctx, num)
```

Lets the instructor get a specific ghost question

<a id="qanda.Qanda.channelOneGhost_error"></a>

#### channelOneGhost\_error

```python
@channelOneGhost.error
async def channelOneGhost_error(ctx, error)
```

Error handling for channelGhost command

<a id="qanda.Qanda.channelGhostQs"></a>

#### channelGhostQs

```python
@commands.has_role("Instructor")
@commands.command(
    name="allChannelGhosts",
    help="Get all the questions that are in the database but "
    "not in the channel. Does not detect zombies.\n"
    "EX: $allChannelGhosts\n"
    "To detect zombies and convert them to ghosts, use $unearthZombies",
)
async def channelGhostQs(ctx)
```

Lets the instructor get the questions that are in the database but not inthe channel

<a id="qanda.Qanda.channelGhostQs_error"></a>

#### channelGhostQs\_error

```python
@channelGhostQs.error
async def channelGhostQs_error(ctx, error)
```

Error handling for allChannelGhosts command

<a id="qanda.Qanda.unearthZombieQs"></a>

#### unearthZombieQs

```python
@commands.has_role("Instructor")
@commands.command(
    name="unearthZombies",
    help="Assign ghost status to all manually deleted questions "
    "in case there is a need to restore them.\n"
    "EX: $unearthZombies\n",
)
async def unearthZombieQs(ctx)
```

Assigns ghost status to all manually deleted questions in case there is a need to restore them

<a id="qanda.Qanda.unearthZombieQs_error"></a>

#### unearthZombieQs\_error

```python
@unearthZombieQs.error
async def unearthZombieQs_error(ctx, error)
```

Error handling for unearthZombies command

<a id="qanda.Qanda.restoreGhost"></a>

#### restoreGhost

```python
@commands.has_role("Instructor")
@commands.command(
    name="reviveGhost",
    help="Restores a ghost or deleted/hidden question to the channel.\n"
    "EX: $reviveGhost 1",
)
async def restoreGhost(ctx, num)
```

Restores a ghost of deleted question to the channel

<a id="qanda.Qanda.restoreGhost_error"></a>

#### restoreGhost\_error

```python
@restoreGhost.error
async def restoreGhost_error(ctx, error)
```

Error handling for reviveGhost command

<a id="qanda.Qanda.countGhosts"></a>

#### countGhosts

```python
@commands.command(name="spooky",
                  help="Is this channel haunted?\n"
                  "EX: $spooky")
async def countGhosts(ctx)
```

Counts the number of ghost and zombie questions in the channel. Mainly for fun but could be useful

<a id="qanda.Qanda.countGhosts_error"></a>

#### countGhosts\_error

```python
@countGhosts.error
async def countGhosts_error(ctx, error)
```

Error handling for spooky command

<a id="qanda.setup"></a>

#### setup

```python
async def setup(bot)
```

Adds the file to the bot's cog system

