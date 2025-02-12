---
type: idea-note
---

# Automatic Updates

Created simple bash script called automate_git.sh

```.bash
#!/bin/bash

# Add all changes to the staging area
git add .

# Commit the changes with a timestamp
git commit -m "Automated commit: $(date)"

# Push the changes to the remote repository
git push
```

Make script executable.

```.bash
chmod +x automate_git.sh
```

Setup a local cronjob

```.bash
0 9 * * * {{working_dir}}/automate_git.sh >> {{working_dir}}/brain-dump/cron.log 2>&1
0 */6 * * * {{working_dir}}/automate_git.sh >> {{working_dir}}/brain-dump/cron.log 2>&1
```

> [!NOTE]
> In the above and below examples, you will need to update the {{working_dir}} with the path to your executable and Foam/Obsidian markdown files or vault.

## Repo Sync

```.bash
30 13 * * * rsync -av --include='.foam/' --exclude='.vscode/' --exclude='private/' --exclude='Meetings/' --exclude='rsync.log' --exclude='cron.log' --exclude='_layouts/' --exclude='Journals/' --include='AI/' --include='Ansible/' --include='attachments/' --include='Demos/' --include='HAM AI/' --include='Journeys/' --include='Ideas.md' --include='Inbox.md' --include='Projects.md' --include='readme.md' --include='Todo.md' --include='Tools.md' --exclude='*' {{working_dir}}/foamy-stuff/ {{working_dir}}/brain-dump/ >> {{working_dir}}/foamy-stuff/rsync.log 2>&1
```

## Todo List

1. test it 




Note Created: 2025-01-06
