# Table of Contents

* [grades](#grades)
  * [Grades](#grades.Grades)
    * [grade](#grades.Grades.grade)
    * [gradebycategory](#grades.Grades.gradebycategory)
    * [gradeforclass](#grades.Grades.gradeforclass)
    * [graderequired](#grades.Grades.graderequired)
    * [graderequiredforclass](#grades.Grades.graderequiredforclass)
    * [categories](#grades.Grades.categories)
    * [input\_grades](#grades.Grades.input_grades)
    * [input\_grades\_error](#grades.Grades.input_grades_error)
    * [add\_grade\_category](#grades.Grades.add_grade_category)
    * [add\_grade\_category\_error](#grades.Grades.add_grade_category_error)
    * [edit\_grade\_category](#grades.Grades.edit_grade_category)
    * [edit\_grade\_category\_error](#grades.Grades.edit_grade_category_error)
    * [delete\_grade\_category](#grades.Grades.delete_grade_category)
    * [delete\_grade\_category\_error](#grades.Grades.delete_grade_category_error)
    * [grade\_report\_category](#grades.Grades.grade_report_category)
    * [grade\_report\_assignment](#grades.Grades.grade_report_assignment)
  * [setup](#grades.setup)

<a id="grades"></a>

# grades

<a id="grades.Grades"></a>

## Grades Objects

```python
class Grades(commands.Cog)
```

<a id="grades.Grades.grade"></a>

#### grade

```python
@commands.command(
    name="grade",
    help="get your grade for a specific assignment $grade ASSIGNMENT")
async def grade(ctx, assignmentName: str)
```

Lets a student get their grade for a certain assignment

<a id="grades.Grades.gradebycategory"></a>

#### gradebycategory

```python
@commands.command(
    name="gradebycategory",
    help="get your grade for a specific category $gradebycategory CATEGORY",
)
async def gradebycategory(ctx, categoryName: str)
```

Lets a student get their grade for a specific grade category

<a id="grades.Grades.gradeforclass"></a>

#### gradeforclass

```python
@commands.command(
    name="gradeforclass",
    help="get your grade for the whole class $gradeforclass",
)
async def gradeforclass(ctx)
```

Lets a student get their overall average grade for the class

<a id="grades.Grades.graderequired"></a>

#### graderequired

```python
@commands.command(
    name="graderequired",
    help=
    "get your grade required on the next assignment for a category and a desired grade $graderequired CATEGORY POINTS GRADE",
)
async def graderequired(ctx, categoryName: str, pointValue: str,
                        desiredGrade: str)
```

Lets a student calculate the grade they need for a desired grade in a category

<a id="grades.Grades.graderequiredforclass"></a>

#### graderequiredforclass

```python
@commands.command(
    name="graderequiredforclass",
    help=
    "get your grade required on the next assignment to keep a desired grade $graderequiredforclass CATEGORY POINTS GRADE",
)
async def graderequiredforclass(ctx, categoryName: str, pointValue: str,
                                desiredGrade: str)
```

Lets a student calculate the grade required on the next assignment to keep an overall desired class grade

<a id="grades.Grades.categories"></a>

#### categories

```python
@commands.command(name="categories",
                  help="display all grading categories and weights $categories"
                  )
async def categories(ctx)
```

Lets the user list the categories of grades that are in the database

<a id="grades.Grades.input_grades"></a>

#### input\_grades

```python
@commands.has_role("Instructor")
@commands.command(name="inputgrades", help="Insert grades using a csv file")
async def input_grades(ctx, assignmentname: str)
```

Lets the instructor input grades into the system for a given assignment

<a id="grades.Grades.input_grades_error"></a>

#### input\_grades\_error

```python
@input_grades.error
async def input_grades_error(ctx, error)
```

Error handling for inputgrades command

<a id="grades.Grades.add_grade_category"></a>

#### add\_grade\_category

```python
@commands.has_role("Instructor")
@commands.command(
    name="addgradecategory",
    help="add a grading category and weight $addgradecategory NAME WEIGHT",
)
async def add_grade_category(ctx, categoryname: str, weight: str)
```

Lets the instructor add a grade category with a specified weight

<a id="grades.Grades.add_grade_category_error"></a>

#### add\_grade\_category\_error

```python
@add_grade_category.error
async def add_grade_category_error(ctx, error)
```

Error handling for add_grade_category command

<a id="grades.Grades.edit_grade_category"></a>

#### edit\_grade\_category

```python
@commands.has_role("Instructor")
@commands.command(
    name="editgradecategory",
    help="edit a grading category and weight $editgradecategory NAME WEIGHT",
)
async def edit_grade_category(ctx, categoryname: str, weight: str)
```

Lets the instructor edit a grade category and weight

<a id="grades.Grades.edit_grade_category_error"></a>

#### edit\_grade\_category\_error

```python
@edit_grade_category.error
async def edit_grade_category_error(ctx, error)
```

Error handling for edit_grade_category command

<a id="grades.Grades.delete_grade_category"></a>

#### delete\_grade\_category

```python
@commands.has_role("Instructor")
@commands.command(
    name="deletegradecategory",
    help="delete a grading category $deletegradecategory NAME",
)
async def delete_grade_category(ctx, categoryname: str)
```

Lets the user delete a grade category from the database

<a id="grades.Grades.delete_grade_category_error"></a>

#### delete\_grade\_category\_error

```python
@delete_grade_category.error
async def delete_grade_category_error(ctx, error)
```

Error handling for delete_grade_category command

<a id="grades.Grades.grade_report_category"></a>

#### grade\_report\_category

```python
@commands.has_role("Instructor")
@commands.command(
    name="gradereportcategory",
    help="Report on the classes scores all grade categories",
)
async def grade_report_category(ctx)
```

Lets the instructor generate a report on the average, low, and high score for each category

<a id="grades.Grades.grade_report_assignment"></a>

#### grade\_report\_assignment

```python
@commands.has_role("Instructor")
@commands.command(
    name="gradereportassignment",
    help="Report on the classes scores all assignments",
)
async def grade_report_assignment(ctx)
```

Lets the instructor generate a report on the average, low, and high score for each assignment

<a id="grades.setup"></a>

#### setup

```python
async def setup(bot)
```

Adds the file to the bot's cog system

