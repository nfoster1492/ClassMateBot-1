# ClassMateBot Project 3 Changes
## Project 2 vs Project 3

## New Additions

### AI moderator
We implemented an AI moderator that will remove toxic, insulting and racist messages.

### New commands and tasks
We added various new commands. These are mentioned below along with their description.

#### Profanity filter commands:

* $toggleFilter: toggles the profanity filter on/off, instructor/admin only
* $whitelist (word): adds a word or sentence to the whitelist, instructor/admin only
* $dewhitelist (word): removes a word or sentence from the whitelist, instructor/admin only

#### New Q&A commands:

* $getAnswersFor (num) -- get all answers for a question. Ignores ghosts and zombies.
* $DALLAF (num) -- deletes all answers for a question. Instructor only.
* $archiveQA -- sends all questions and answers to the user via DM. Ignores ghosts and zombies.
* $deleteAllQA -- deletes all questions and answers from the database and channel. Also cleans up ghosts and zombies. Instructor only.
* $deleteQuestion (num) -- deletes a single question from the channel and leaves a database ghost. Instructor only.

#### Database integrity commands:

* $spooky: Used to check the number of zombies and ghosts in the channel. Fun for students, useful for instructors.
* $channelGhost (num): Get the ghost question and its answers with that number. Also works for zombies and non-ghost questions. (Basically, getAnswersFor but doesn't ignore ghosts or zombies.) Instructor only.
* $allChannelGhosts: get all channel ghosts via DM. Instructor only. (Does not work with zombies.)
* $reviveGhost (num): Restores a ghost question (and answers). Instructor only.
* $unearthZombies: gets all zombies (manually deleted questions) and assigns ghost status. Instructor only.

### Reminder Commands
* $overdue: lists all overdue reminders
* $clearoverdue: deletes overdue reminders

### Reminder Tasks
* Reminder task that runs once per day at 8am to give reminders of anything due that day
* Reminder task that runs once per hour to give reminder of anything due that hour

## Improvements

We also modified some existing commands to allow easier input for user and handle corner cases. These improvements are mentioned below.

### $ask:
* Users can now use anon instead of anonymous (though anonymous still works).
* Users cannot ask empty/blank/whitespace only questions.

### $answer:
* Users can now use anon instead of anonymous (though anonymous still works).
* Question number must be a valid number.
* Users can't answer with empty strings.
* Users can't answer deleted or hidden questions.

### $addhw and $changeduedate
* Now instuctor only.
* Date input is more flexible. (ie both of these are now valid - NOV 30 2050, 11/30/2050)
* Users can add a timezone to the time as well

### $duetoday and $duethisweek
* Shows time delta between now and duedate so users don't have to manually covert systen time to local
* Dates are formatted with timezome (ie NOV 11 2050 12:00+0000)
