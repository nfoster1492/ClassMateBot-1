# Table of Contents

* [voting](#voting)
  * [Voting](#voting.Voting)
    * [vote](#voting.Voting.vote)
    * [vote\_error](#voting.Voting.vote_error)
    * [projects](#voting.Voting.projects)
    * [project\_error](#voting.Voting.project_error)
  * [setup](#voting.setup)

<a id="voting"></a>

# voting

<a id="voting.Voting"></a>

## Voting Objects

```python
class Voting(commands.Cog)
```

<a id="voting.Voting.vote"></a>

#### vote

```python
@commands.command(
    name="vote",
    help="Used for voting for Projects, \
    To use the vote command, do: $vote <Num> \n \
    (For example: $vote 0)",
    pass_context=True,
)
async def vote(ctx, project_num: int)
```

Used for voting for projects. "Votes" for the given project by adding the user's group to it

<a id="voting.Voting.vote_error"></a>

#### vote\_error

```python
@vote.error
async def vote_error(ctx, error)
```

Error handling for vote command

<a id="voting.Voting.projects"></a>

#### projects

```python
@commands.command(
    name="projects",
    help="print projects with groups assigned to them",
    pass_context=True,
)
async def projects(ctx)
```

Prints the list of current projects

<a id="voting.Voting.project_error"></a>

#### project\_error

```python
@projects.error
async def project_error(ctx, error)
```

Error handling for projects command

<a id="voting.setup"></a>

#### setup

```python
async def setup(bot)
```

Adds the file to the bot's cog system

