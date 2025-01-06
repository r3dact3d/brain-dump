#!/bin/bash

# Add all changes to the staging area
git add .

# Commit the changes with a timestamp
git commit -m "Automated commit: $(date)"

# Push the changes to the remote repository
git push
