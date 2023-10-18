# Table of Contents

* [newComer](#newComer)
  * [NewComer](#newComer.NewComer)
    * [verify](#newComer.NewComer.verify)
    * [verify\_error](#newComer.NewComer.verify_error)
  * [setup](#newComer.setup)

<a id="newComer"></a>

# newComer

<a id="newComer.NewComer"></a>

## NewComer Objects

```python
class NewComer(commands.Cog)
```

<a id="newComer.NewComer.verify"></a>

#### verify

```python
@commands.command(
    name="verify",
    pass_context=True,
    help=
    "User self-verifies by attaching their real name to their discord username in this server: "
    "$verify <FirstName LastName>",
)
async def verify(ctx, *, name: str = None)
```

Gives the user the `verified` role in the server

<a id="newComer.NewComer.verify_error"></a>

#### verify\_error

```python
@verify.error
async def verify_error(ctx, error)
```

Error handling for verify command

<a id="newComer.setup"></a>

#### setup

```python
async def setup(bot)
```

Adds the file to the bot's cog system

