# Table of Contents

* [groups](#groups)
  * [Groups](#groups.Groups)
    * [reset](#groups.Groups.reset)
    * [reset\_error](#groups.Groups.reset_error)
    * [startupgroups](#groups.Groups.startupgroups)
    * [startupgroups\_error](#groups.Groups.startupgroups_error)
    * [connect](#groups.Groups.connect)
    * [connect\_error](#groups.Groups.connect_error)
    * [join](#groups.Groups.join)
    * [join\_error](#groups.Groups.join_error)
    * [leave](#groups.Groups.leave)
    * [leave\_error](#groups.Groups.leave_error)
    * [groups](#groups.Groups.groups)
    * [groups\_error](#groups.Groups.groups_error)
    * [group](#groups.Groups.group)
    * [group\_error](#groups.Groups.group_error)
  * [setup](#groups.setup)

<a id="groups"></a>

# groups

<a id="groups.Groups"></a>

## Groups Objects

```python
class Groups(commands.Cog)
```

<a id="groups.Groups.reset"></a>

#### reset

```python
@commands.command(
    name="reset",
    help="Resets group channels and roles. DO NOT USE IN PRODUCTION!")
async def reset(ctx)
```

Deletes all group roles in the server

<a id="groups.Groups.reset_error"></a>

#### reset\_error

```python
@reset.error
async def reset_error(ctx, error)
```

Error handling for reset command

<a id="groups.Groups.startupgroups"></a>

#### startupgroups

```python
@commands.command(name="startupgroups", help="Creates group roles for members")
async def startupgroups(ctx)
```

Creates roles for the groups

<a id="groups.Groups.startupgroups_error"></a>

#### startupgroups\_error

```python
@startupgroups.error
async def startupgroups_error(ctx, error)
```

Error handling for startupgroups command

<a id="groups.Groups.connect"></a>

#### connect

```python
@commands.command(name="connect", help="Creates group roles for members")
async def connect(ctx)
```

Connects all users with their groups

<a id="groups.Groups.connect_error"></a>

#### connect\_error

```python
@connect.error
async def connect_error(ctx, error)
```

Error handling for connect command

<a id="groups.Groups.join"></a>

#### join

```python
@commands.command(
    name="join",
    help="To use the join command, do: $join <Num> \n \
    ( For example: $join 0 )",
    pass_context=True,
)
async def join(ctx, group_num: int)
```

Joins the user to given group

<a id="groups.Groups.join_error"></a>

#### join\_error

```python
@join.error
async def join_error(ctx, error)
```

Error handling for join command

<a id="groups.Groups.leave"></a>

#### leave

```python
@commands.command(
    name="leave",
    help="To use the leave command, do: $leave \n \
    ( For example: $leave )",
    pass_context=True,
)
async def leave(ctx)
```

Removes the user from the given group

<a id="groups.Groups.leave_error"></a>

#### leave\_error

```python
@leave.error
async def leave_error(ctx, error)
```

Error handling for leave command

<a id="groups.Groups.groups"></a>

#### groups

```python
@commands.command(name="groups", help="prints group counts", pass_context=True)
async def groups(ctx)
```

Prints the list of groups

<a id="groups.Groups.groups_error"></a>

#### groups\_error

```python
@groups.error
async def groups_error(ctx, error)
```

Error handling for groups command

<a id="groups.Groups.group"></a>

#### group

```python
@commands.command(
    name="group",
    help="print names of members in a group, or current groups members \n \
    ( For example: $group or $group 8 )",
    pass_context=True,
)
async def group(ctx, group_num: int = -1)
```

Prints the members of the group, or the current member's group if they have joined one

<a id="groups.Groups.group_error"></a>

#### group\_error

```python
@group.error
async def group_error(ctx, error)
```

Error handling for group command

<a id="groups.setup"></a>

#### setup

```python
async def setup(bot)
```

Adds the file to the bot's cog system

