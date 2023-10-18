# Table of Contents

* [pinning](#pinning)
  * [Pinning](#pinning.Pinning)
    * [helpful3](#pinning.Pinning.helpful3)
    * [addMessage](#pinning.Pinning.addMessage)
    * [addMessage\_error](#pinning.Pinning.addMessage_error)
    * [deleteMessage](#pinning.Pinning.deleteMessage)
    * [deleteMessage\_error](#pinning.Pinning.deleteMessage_error)
    * [retrieveMessages](#pinning.Pinning.retrieveMessages)
    * [retrieveMessages\_error](#pinning.Pinning.retrieveMessages_error)
    * [updatePinnedMessage](#pinning.Pinning.updatePinnedMessage)
    * [updatePinnedMessage\_error](#pinning.Pinning.updatePinnedMessage_error)
  * [setup](#pinning.setup)

<a id="pinning"></a>

# pinning

<a id="pinning.Pinning"></a>

## Pinning Objects

```python
class Pinning(commands.Cog)
```

<a id="pinning.Pinning.helpful3"></a>

#### helpful3

```python
@commands.command()
async def helpful3(ctx)
```

Test command to chheck if the bot it working

<a id="pinning.Pinning.addMessage"></a>

#### addMessage

```python
@commands.command(
    name="pin",
    help="Pin a message by adding a tagname (single word) "
    "and a description(can be multi word). EX: $pin Homework Resources for HW2",
)
async def addMessage(ctx, tagname: str, *, description: str)
```

Used to pin a message by the user

<a id="pinning.Pinning.addMessage_error"></a>

#### addMessage\_error

```python
@addMessage.error
async def addMessage_error(ctx, error)
```

Error handling for pin(addMessage) command

<a id="pinning.Pinning.deleteMessage"></a>

#### deleteMessage

```python
@commands.command(name="unpin", help="Unpin a message by passing the tagname.")
async def deleteMessage(ctx, tagname: str)
```

Unpins the pinned messages with provided tagname

<a id="pinning.Pinning.deleteMessage_error"></a>

#### deleteMessage\_error

```python
@deleteMessage.error
async def deleteMessage_error(ctx, error)
```

Error handling for unpin(deleteMessage) command

<a id="pinning.Pinning.retrieveMessages"></a>

#### retrieveMessages

```python
@commands.command(
    name="pinnedmessages",
    help="Retrieve the pinned messages by a particular tag or all messages.",
)
async def retrieveMessages(ctx, tagname: str = "")
```

Retrieves all pinned messages under a given tagname by either everyone or a particular user

<a id="pinning.Pinning.retrieveMessages_error"></a>

#### retrieveMessages\_error

```python
@retrieveMessages.error
async def retrieveMessages_error(ctx, error)
```

Error handling for retrievemessages function

<a id="pinning.Pinning.updatePinnedMessage"></a>

#### updatePinnedMessage

```python
@commands.command(
    name="updatepin",
    help="Update a previously pinned message by passing the "
    "tagname and old description in the same order",
)
async def updatePinnedMessage(ctx, tagname: str, *, description: str)
```

Updates a pinned message with a given tagname, deletes old messages for the tag

<a id="pinning.Pinning.updatePinnedMessage_error"></a>

#### updatePinnedMessage\_error

```python
@updatePinnedMessage.error
async def updatePinnedMessage_error(ctx, error)
```

Error handling for updatepinnedmessage function

<a id="pinning.setup"></a>

#### setup

```python
async def setup(bot)
```

Adds the file to the bot's cog system

