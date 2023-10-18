# Table of Contents

* [assignments](#assignments)
  * [Assignments](#assignments.Assignments)
    * [add\_assignment](#assignments.Assignments.add_assignment)
    * [edit\_assignment](#assignments.Assignments.edit_assignment)
    * [delete\_assignment](#assignments.Assignments.delete_assignment)
    * [add\_assignment\_error](#assignments.Assignments.add_assignment_error)
    * [edit\_assignment\_error](#assignments.Assignments.edit_assignment_error)
    * [delete\_assignment\_error](#assignments.Assignments.delete_assignment_error)
  * [setup](#assignments.setup)

<a id="assignments"></a>

# assignments

<a id="assignments.Assignments"></a>

## Assignments Objects

```python
class Assignments(commands.Cog)
```

<a id="assignments.Assignments.add_assignment"></a>

#### add\_assignment

```python
@commands.has_role("Instructor")
@commands.command(
    name="addassignment",
    help=
    "add a grading assignment and points $addassignment NAME CATEGORY POINTS",
)
async def add_assignment(ctx, assignmentname: str, categoryname: str,
                         points: str)
```

Add a grading assignment and points

<a id="assignments.Assignments.edit_assignment"></a>

#### edit\_assignment

```python
@commands.has_role("Instructor")
@commands.command(
    name="editassignment",
    help=
    "edit a grading assignment and points $editassignment NAME CATEGORY POINTS",
)
async def edit_assignment(ctx, assignmentname: str, categoryname: str,
                          points: str)
```

edit a grading assignment and points $editassignment NAME CATEGORY POINTS

<a id="assignments.Assignments.delete_assignment"></a>

#### delete\_assignment

```python
@commands.has_role("Instructor")
@commands.command(
    name="deleteassignment",
    help="delete a grading assignment $deleteassignment NAME",
)
async def delete_assignment(ctx, assignmentname: str)
```

delete a grading assignment $deleteassignment NAME

<a id="assignments.Assignments.add_assignment_error"></a>

#### add\_assignment\_error

```python
@add_assignment.error
async def add_assignment_error(ctx, error)
```

Error handling of addassignment function

<a id="assignments.Assignments.edit_assignment_error"></a>

#### edit\_assignment\_error

```python
@edit_assignment.error
async def edit_assignment_error(ctx, error)
```

Error handling of editassignment function

<a id="assignments.Assignments.delete_assignment_error"></a>

#### delete\_assignment\_error

```python
@delete_assignment.error
async def delete_assignment_error(ctx, error)
```

Error handling of deleteassignment function

<a id="assignments.setup"></a>

#### setup

```python
async def setup(bot)
```

Adds the file to the bot's cog system

