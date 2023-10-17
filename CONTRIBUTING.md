# Contributing to ClassMateBot

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to   ClassMate Bot. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

#### Table Of Contents

[Code of Conduct](#code-of-conduct)

[Quick Support](#quick-support)

[How Can I Contribute?](#how-can-i-contribute)
  * [Pull Requests](#pull-requests)
  * [Adding Commands](#adding-commands)
  * [Reporting Bugs](#reporting-bugs)

[Style Guides](#style-guides)
  * [Git Commit Messages](#git-commit-messages)
  * [Python Style Guide](#python-style-guide)

[Governal Policies](#governal-policies)

## Code of Conduct

This project and everyone participating in it is governed by the [ClassMate Bot Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to any of the original team members listed at the bottom of [README.md](README.md).

## Quick Support

Support Email:
* *classmatebot5@gmail.com*

Reach out to one of the main contributors:
* Robert Kenney: *rpkenney@ncsu.edu*
* Brandon Walia: *bswalia@ncsu.edu*
* Nathan Kohen: *nrkohen@ncsu.edu*
* Nicholas Foster: *nsfoster@ncsu.edu*

We would love to help with whatever issues you have or questions about contributing to ClassMateBot!

## How Can I Contribute?

### Pull Requests

The process described here has several goals:

- Maintain the project's quality

- Fix problems that are important to users

- Enable a sustainable system for the projects maintainers' to review contributions

Please follow these steps to have your contribution reviewed by the maintainers:

1. Include a clear and descriptive title.
2. Include a detailed description of the change.

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

### Adding Commands
Commands can be added in the form of Cogs. View hello.py as a simple example of how a Cog can be added.

The basic structure is as follows:

```
class <NAME>(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    <COMMANDS RELATED TO THIS FILE>
    
def setup(bot):
    bot.add_cog(<NAME>(bot))
```
For more information on how to use cogs, refer to the [Cogs Page](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html)

For more information on the API of discord.py you can use the [API Reference Page](https://discordpy.readthedocs.io/en/stable/api.html)

For general knowledge of discord.py use the [Documentation Page](https://discordpy.readthedocs.io/en/latest/index.html)
## Reporting Bugs

This section guides you through submitting a bug report for ClassMateBot. 
Following these guidelines helps maintainers and the community understand your report, reproduce the behavior and find related reports.

### How Do I Submit A (Good) Bug Report?

- Use a clear and descriptive title for the issue to identify the problem.

- Describe the exact steps which reproduce the problem in as many details as possible.

- Provide specific examples to demonstrate the steps. 

- Describe the behavior you observed after following the steps and point out what exactly is the problem with that behavior.

- Explain which behavior you expected to see instead and why.

- Include screenshots and animated GIFs which show you following the described steps and clearly demonstrate the problem. 

- If the problem is related to performance or memory, include a CPU profile capture with your report.

## Style Guides

### Git Commit Messages

- Describe why a change is being made.

- Describe any limitations of the current code.

- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")

- Limit the first line to 72 characters or less

- Link an issue to the change

### Python Styleguide

Changes to ClassMateBot Python code should conform to [Google Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md).

All Python code is linted with Pylint. Ensure that before you commit any changes, your code passes all default pylint checks. Pylint can be installed with
`pip install pylint`.

All Python code is formatted using Black. Ensure that before you commit any changes, you run Black on all updated files and ensure that the code passes the Black checks.

### Governal Policies

All contributions will be carefully reviewed by our entire development team. We will discuss the advantages and disadvantages of adding the change, and a final decision will be decided based on a vote, with all members' votes having equal weight.

*This document is adapted from the [Atom Code of Conduct](https://github.com/atom/atom/blob/master/CONTRIBUTING.md#code-of-conduct)*
