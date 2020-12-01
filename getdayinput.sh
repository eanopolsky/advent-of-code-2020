#!/bin/sh

# Note: this is insecure. Cookies specified on the command line will be written
# to the shell's history file and will be briefly visible to other users on the
# same machine via 'ps'.

if [ $# != "2" ]
then echo "Usage: $0 daynumber sessioncookie."
     echo "Example: $0 5 '01234567890abcdef' # would download the input for day 5."
     exit 1
fi

curl -b "session=$2" -o "input_day$1" "https://adventofcode.com/2020/day/$1/input"

