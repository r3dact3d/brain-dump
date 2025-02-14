---
type: idea-note
---

# Automatic Updates

> Here is my pipeline to share the **public** facing part of my [[Second Brain]] and keep the **private** or **internal ruminations** to myself.

The idea here is to seperate public facing notes from my private notes and share them publicly for easy access and collaboration using these tools:

- rsync
- git
- crontab
  
These are the specific steps currently documented that create the automatic backup pipeline:

1. Write notes using VS Code, using Foam extensions.
2. The markdown files are saved in a local private github repo
3. **rsync** files designated as public to local public github repo
4. **git** local public repo to remote public repo
5. Wrap these up in a bash script and put in **crontab** to run as scheduled

## rsync

> I use this to sync public facing stuff to another local git repo to sync with a public source.

```.bash
sync -av --exclude='.foam/' --exclude='.git/' --exclude='.vscode/' --exclude='scripts/' --exclude='private/' --exclude='Meetings/' --exclude='rsync.log' --exclude='cron.log' --exclude='_layouts/' --exclude='Journals/' --include='AI/' --include='Ansible/' --include='attachments/' --include='Demos/' --include='HAM AI/' --include='Journeys/' -- include='Ideas/' --include='Fabric/' --include='Ideas.md' --include='Inbox.md' --include='Projects.md' --include='readme.md' --include='Todo.md' --include='Tools.md' --exclude='*' {{working_dir}}/foamy-stuff/ {{working_dir}}/brain-dump/ >> {{working_dir}}/foamy-stuff/rsync.log 2>&1
```

## git

> Created simple bash script called *automate_git.sh* that contains just a few git commands to commit and sync the local repository to the remote public facing repo.

```.bash
#!/bin/bash

if ! hash rsync; then
    echo "Rsync is not installed on this system"
    exit 1
fi

rsync -av --include='.foam/' --exclude='.vscode/' --exclude='private/' --exclude='Meetings/' --exclude='rsync.log' --exclude='cron.log' --exclude='_layouts/' --exclude='Journals/' --include='AI/' --include='Ansible/' --include='attachments/' --include='Demos/' --include='HAM AI/' --include='Journeys/' --include='Ideas.md' --include='Inbox.md' --include='Projects.md' --include='readme.md' --include='Todo.md' --include='Tools.md' --exclude='*' {{working_dir}}foamy-stuff/ {{working_dir}}/brain-dump/

cd {{working_dir}}/brain-dump/

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

```

Make script executable.

```.bash
chmod +x automate_git.sh
```

## crontab

Setup a local crontab to run when my laptop is most likely to be on

```.bash
30 13 * * *  {{working_dir}}/brain-dump/automate_git.sh >> {{working_dir}}/foamy-stuff/cron.log 2>&1
```

> [!NOTE]
> In the above and below examples, you will need to update the {{working_dir}} with the path to your executable and Foam/Obsidian markdown files or vault.

Note Created: 2025-01-06
