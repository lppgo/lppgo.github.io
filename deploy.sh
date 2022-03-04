#!/bin/bash

echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

# Build the project.

echo -e "\033[0;32mrm-rf docs\033[0m"
rm -rf docs

echo -e "\033[0;32mhugo -d docs\033[0m"
hugo -d docs

echo -e "\033[0;32mhugo --gc --minify --cleanDestinationDir\033[0m"
hugo --gc --minify --cleanDestinationDir

# git
# Add changes to git.
echo -e "\033[0;32mgit status\033[0m"
git status
echo -e "\033[0;32mgit add -A\033[0m"
git add -A

# # Commit changes.
msg="rebuilding site $(date)"
if [ $# -eq 1 ]; then
    msg="$1"
fi
echo -e "\033[0;32mgit commit -m "$msg"\033[0m"
git commit -m "$msg"

# Push source and build repos.
echo -e "\033[0;32mgit push origin main\033[0m"
git push origin master
