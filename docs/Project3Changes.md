# THIS IS STILL A WORK IN PROGRESS.


# bot.py
## CHANGES TO EXISTING COMMANDS

## NEW COMMANDS

Profanity filter commands:

* $toggleFilter: toggles the profanity filter on/off, instructor/admin only
* $whitelist (word): adds a word or sentence to the whitelist, instructor/admin only
* $dewhitelist (word): removes a word or sentence from the whitelist, instructor/admin only

## OTHER CHANGES



# qanda.py
## CHANGES TO EXISTING COMMANDS

$ask:
* Users can now use anon instead of anonymous (though anonymous still works).
* Users cannot ask empty/blank/whitespace only questions.

$answer:
* Users can now use anon instead of anonymous (though anonymous still works).
* Question number must be a valid number.
* Users can't answer with empty strings.
* Users can't answer deleted or hidden questions.

## NEW COMMANDS

### New Q&A commands:

* $getAnswersFor (num) -- get all answers for a question. Ignores ghosts and zombies.
* $DALLAF (num) -- deletes all answers for a question. Instructor only.
* $archiveQA -- sends all questions and answers to the user via DM. Ignores ghosts and zombies.
* $deleteAllQA -- deletes all questions and answers from the database and channel. Also cleans up ghosts and zombies. Instructor only.
* $deleteQuestion (num) -- deletes a single question from the channel and leaves a database ghost. Instructor only.

### Database integrity commands:

* $spooky: Used to check the number of zombies and ghosts in the channel. Fun for students, useful for instructors.
* $channelGhost (num): Get the ghost question and its answers with that number. Also works for zombies and non-ghost questions. (Basically, getAnswersFor but doesn't ignore ghosts or zombies.) Instructor only.
* $allChannelGhosts: get all channel ghosts via DM. Instructor only. (Does not work with zombies.)
* $reviveGhost (num): Restores a ghost question (and answers). Instructor only.
* $unearthZombies: gets all zombies (manually deleted questions) and assigns ghost status. Instructor only.



# deadline.py

## CHANGES TO EXISTING COMMANDS
## NEW COMMANDS
## OTHER CHANGES

# groups.py

## CHANGES TO EXISTING COMMANDS
## NEW COMMANDS
## OTHER CHANGES

# newComer.py

## CHANGES TO EXISTING COMMANDS
## NEW COMMANDS
## OTHER CHANGES

# ping.py

## CHANGES TO EXISTING COMMANDS
## NEW COMMANDS
## OTHER CHANGES

# pinning.py

## CHANGES TO EXISTING COMMANDS
## NEW COMMANDS
## OTHER CHANGES

# reviewQs.py

## CHANGES TO EXISTING COMMANDS
## NEW COMMANDS
## OTHER CHANGES

# voting.py

## CHANGES TO EXISTING COMMANDS
## NEW COMMANDS
## OTHER CHANGES