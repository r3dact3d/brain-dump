---
type: basic-note
---

# Morning Updates

Created simple bash script called morning_commit.sh

```
#!/bin/bash

# Add all changes to the staging area
git add .

# Commit the changes with a timestamp
git commit -m "Automated commit: $(date)"

# Push the changes to the remote repository
git push
```

Make script executable.

```
chmod +x morning_commit.sh
```

Setup a local cronjob

```
0 9 * * * {{working_dir}}/morning_commit.sh >> {{working_dir}}/cron.log 2>&1
```

## Todo List

1. test it 

Note Created: 2025-01-06
