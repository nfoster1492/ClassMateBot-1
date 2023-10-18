# Table of Contents

* [wordfilter](#wordfilter)
  * [WordFilter](#wordfilter.WordFilter)
    * [whitelistWordTest](#wordfilter.WordFilter.whitelistWordTest)
    * [whitelistWord\_error](#wordfilter.WordFilter.whitelistWord_error)
    * [clearWhitelist](#wordfilter.WordFilter.clearWhitelist)
    * [clearWhitelist\_error](#wordfilter.WordFilter.clearWhitelist_error)
    * [loadWhitelist](#wordfilter.WordFilter.loadWhitelist)
    * [loadWhitelist\_error](#wordfilter.WordFilter.loadWhitelist_error)
  * [setup](#wordfilter.setup)

<a id="wordfilter"></a>

# wordfilter

<a id="wordfilter.WordFilter"></a>

## WordFilter Objects

```python
class WordFilter(commands.Cog)
```

<a id="wordfilter.WordFilter.whitelistWordTest"></a>

#### whitelistWordTest

```python
@commands.has_role("Instructor")
@commands.command(
    name="whitelisttest",
    help=
    'Add a word to the censor whitelist. Enclose in quotation marks. EX: $whitelist "WORD"',
)
async def whitelistWordTest(ctx, word: str = "")
```

Allows instructors to add words to censor whitelist

<a id="wordfilter.WordFilter.whitelistWord_error"></a>

#### whitelistWord\_error

```python
@whitelistWordTest.error
async def whitelistWord_error(ctx, error)
```

Error handling for whitelist command

<a id="wordfilter.WordFilter.clearWhitelist"></a>

#### clearWhitelist

```python
@commands.has_role("Instructor")
@commands.command(
    name="clearWhitelist",
    help="Clears all words from the saved whitelist. EX: $clearwhitelist",
)
async def clearWhitelist(ctx)
```

Allows instructors to clea their saved whitelist

<a id="wordfilter.WordFilter.clearWhitelist_error"></a>

#### clearWhitelist\_error

```python
@clearWhitelist.error
async def clearWhitelist_error(ctx, error)
```

Error handling for whitelist command

<a id="wordfilter.WordFilter.loadWhitelist"></a>

#### loadWhitelist

```python
@commands.has_role("Instructor")
@commands.command(
    name="loadWhitelist",
    help=
    "Adds all words in the saved whitelist to the censor whitelist. EX: $loadWhitelist",
)
async def loadWhitelist(ctx)
```

Allows instructors to load their saved whitelist

<a id="wordfilter.WordFilter.loadWhitelist_error"></a>

#### loadWhitelist\_error

```python
@loadWhitelist.error
async def loadWhitelist_error(ctx, error)
```

Error handling for loadWhitelist command

<a id="wordfilter.setup"></a>

#### setup

```python
async def setup(bot)
```

Adds the file the bot's cog system

