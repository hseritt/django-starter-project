#!/usr/bin/env bash

RESET="0"
RUNTESTS="0"
NODATA="1"

OPTS=$@

RESET=$(echo $OPTS | grep "reset" | wc | cut -d' ' -f8)
RUNTESTS=$(echo $OPTS | grep "runtests" | wc | cut -d' ' -f8)
NODATA=$(echo $OPTS | grep "nodata" | wc | cut -d' ' -f8)

if [ "$RESET" == "1" ]
then
    NODATA="0"
    echo "Upgrading packages if necessary ..."
    pip-review --auto
    echo "  Done."

    echo "Recording versions of all pacakges ..."
    pip freeze > requirements.txt
    echo "  Done."
    echo "Resetting the database."
    ./reset.sh
else
    NODATA="1"
fi

if [ "$RUNTESTS" == "1" ]
then
    echo "We are running tests."
fi

if [ "$NODATA" == "0" ]
then
    echo ""
    # scripts/init_data.py
fi

cd django_starter/static/js
npm update
npm install
cd ../../..
./manage.py runserver

