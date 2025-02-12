#!/bin/bash

if ! hash git; then
    echo "Git is not installed on this system"
    exit 1
fi

diff=$(git diff)
if [ -z "$diff" ]; then
    echo "There are no changes to commit"
    exit 0
fi

status=$(git status)
if [ -n "$status" ]; then
    echo "There are changes to commit"
    git add .
    git commit -m "Automated commit: $(date)"
    git push
fi
