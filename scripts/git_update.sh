#!/bin/bash

read -p "Commit message: " msg

git add -A

if git diff --cached --quiet; then
    echo "No changes to commit."
else
    git commit -m "$msg"
    git push
fi