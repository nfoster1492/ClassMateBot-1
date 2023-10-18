# Table of Contents

* [ping](#ping)
  * [Helpful](#ping.Helpful)
    * [ping](#ping.Helpful.ping)
  * [setup](#ping.setup)

<a id="ping"></a>

# ping

<a id="ping.Helpful"></a>

## Helpful Objects

```python
class Helpful(commands.Cog)
```

<a id="ping.Helpful.ping"></a>

#### ping

```python
@commands.command()
async def ping(ctx)
```

Prints the current ping of the bot, used as a test function

<a id="ping.setup"></a>

#### setup

```python
async def setup(bot)
```

Adds the file to the bot's cog system

