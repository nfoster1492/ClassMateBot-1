# Table of Contents

* [reviewQs](#reviewQs)
  * [ReviewQs](#reviewQs.ReviewQs)
    * [getQuestion](#reviewQs.ReviewQs.getQuestion)
    * [get\_question\_error](#reviewQs.ReviewQs.get_question_error)
    * [addQuestion](#reviewQs.ReviewQs.addQuestion)
    * [add\_question\_error](#reviewQs.ReviewQs.add_question_error)
  * [setup](#reviewQs.setup)

<a id="reviewQs"></a>

# reviewQs

<a id="reviewQs.ReviewQs"></a>

## ReviewQs Objects

```python
class ReviewQs(commands.Cog)
```

<a id="reviewQs.ReviewQs.getQuestion"></a>

#### getQuestion

```python
@commands.command(name="getQuestion",
                  help="Get a review question. EX: $getQuestion")
async def getQuestion(ctx)
```

Prints a random question from the database

<a id="reviewQs.ReviewQs.get_question_error"></a>

#### get\_question\_error

```python
@getQuestion.error
async def get_question_error(ctx, error)
```

Error handling for getQuestion command

<a id="reviewQs.ReviewQs.addQuestion"></a>

#### addQuestion

```python
@commands.has_role("Instructor")
@commands.command(
    name="addQuestion",
    help="Add a review question. "
    'EX: $addQuestion "What class is this?" "Software Engineering"',
)
async def addQuestion(ctx, qs: str, ans: str)
```

Allows instructors to add review questions

<a id="reviewQs.ReviewQs.add_question_error"></a>

#### add\_question\_error

```python
@addQuestion.error
async def add_question_error(ctx, error)
```

Error handling for addQuestion command

<a id="reviewQs.setup"></a>

#### setup

```python
async def setup(bot)
```

Adds the file to the bot's cog system

