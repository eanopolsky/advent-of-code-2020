#!/bin/sh

# Note: this is insecure. Cookies specified on the command line will be written
# to the shell's history file and will be briefly visible to other users on the
# same machine via 'ps'.

# Generated 2020-12-04 and lasts for ~1 month according to the API documentation
# on the private leaderboard page.
SESSIONCOOKIE=$(cat my_session_cookie.txt) 

if [ $# != "1" ]
then echo "Usage: $0 daynumber "
     echo "Example: $0 5 # would download the input for day 5."
     exit 1
fi

curl -b "session=$SESSIONCOOKIE" -o "input_day$1" "https://adventofcode.com/2020/day/$1/input"

