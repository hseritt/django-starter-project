#!/usr/bin/env bash

PROJECT_NAME=$1

if [ "$PROJECT_NAME" == "" ]
then
    echo ""
    echo "Usage: ./change-project.sh [new project name]"
    echo ""
    exit 1
fi

BACKUP_NAME="removeme"

results=$(find . -print | egrep .${BACKUP_NAME})

if [ "${results}" ]
then
    echo "" 
    echo "Found these existing files with $BACKUP_NAME in their names: " $results
    echo "Please change this script's BACKUP_NAME parameter so that it won't do any unintentional deletions."
    echo ""
    exit 1
fi


find . -type f -exec sed -i.${BACKUP_NAME} "s/django_starter/${PROJECT_NAME}/g" {} \;
find . -print | egrep .${BACKUP_NAME}$ | xargs rm -rfv

mv django_starter ${PROJECT_NAME}

rm -rf .git
echo "You have a new project. The .git folder has been removed. Create a new one with: git init"

cat /dev/null > README.md
echo "Cleared the contents of REAME.md. Now you can make your own."

pyenv global $(cat runtime.txt|cut -d"-" -f2) 
pyenv virtualenv $PROJECT_NAME
pyenv local $PROJECT_NAME
pip install --upgrade pip
pip install --use-feature=fast-deps -r requirements.txt
pip freeze > requirements.txt
