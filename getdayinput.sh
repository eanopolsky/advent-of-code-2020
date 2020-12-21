#!/bin/bash

# Note: this is insecure. Cookies specified on the command line will be written
# to the shell's history file and will be briefly visible to other users on the
# same machine via 'ps'.

# Generated 2020-12-04 and lasts for ~1 month according to the API documentation
# on the private leaderboard page.
SESSION_COOKIE_FILE="my_session_cookie.txt"
SESSIONCOOKIE=$(cat $SESSION_COOKIE_FILE) 

let "COOKIE_AGE_SECONDS = $(date +%s) - $(stat -c %Y $SESSION_COOKIE_FILE)"
let "TWO_WEEKS_SECONDS = 86400 * 14"
if [ $COOKIE_AGE_SECONDS -gt $TWO_WEEKS_SECONDS ]
then echo "WARNING: $SESSION_COOKIE_FILE is more than two weeks old. According to the documentation, it is good for one month. Consider refreshing it."
fi

if [ $# -gt 1 ]
then echo "Usage: $0"
     echo "or"
     echo "Usage: $0 daynumber "
     echo "Downloads the input for daynumber. If daynumber is absent, waits until the next day's input is available and gets it as soon as possible."
     echo "Example: $0 5 # would download the input for day 5."
     exit 1
fi

if [ $# == 1 ]
then curl -b "session=$SESSIONCOOKIE" -o "input_day$1" "https://adventofcode.com/2020/day/$1/input"
     exit $?
fi

CURRENT_DAY_EST=$(TZ=America/New_York date '+%d')
let "NEXT_DAY_EST = $CURRENT_DAY_EST + 1"
let "INPUT_RELEASE_TIME = $(TZ=America/New_York date -d 2020-12-${NEXT_DAY_EST}T00:00:01 '+%s')"
let "SLEEP_SECONDS = $INPUT_RELEASE_TIME - $(date +%s)"

echo "Getting input for day $NEXT_DAY_EST in $SLEEP_SECONDS seconds..."
sleep $SLEEP_SECONDS
curl -b "session=$SESSIONCOOKIE" -o "input_day${NEXT_DAY_EST}" "https://adventofcode.com/2020/day/${NEXT_DAY_EST}/input"

less "input_day${NEXT_DAY_EST}"
