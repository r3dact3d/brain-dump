#!/bin/bash

if ! hash rsync; then
    echo "Rsync is not installed on this system"
    exit 1
fi

rsync -av --exclude='*' --exclude='.foam/' --exclude='.git/' --exclude='.vscode/' --exclude='scripts/' --exclude='private/' --exclude='Companies/' --exclude='Meetings/' --exclude='rsync.log' --exclude='cron.log' --exclude='_layouts/' --exclude='Journals/' --include='AI/' --include='Ansible/' --include='attachments/' --include='Demos/' --include='HAM AI/' --include='Journeys/' -- include='Ideas/' --include='Fabric/' --include='Ideas.md' --include='Inbox.md' --include='Projects.md' --include='readme.md' --include='Todo.md' --include='Tools.md' --exclude='*' /home/brthomps/working/foamy-stuff/ /home/brthomps/working/brain-dump/ >> /home/brthomps/working/foamy-stuff/rsync.log 2>&1
cd /home/brthomps/working/brain-dump/

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
