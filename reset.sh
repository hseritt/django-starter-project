#!/usr/bin/env bash

DBNAME="django_starter"
DBUSER="admin"

printf '\33c\e[3J'

echo "Dropping database ..."
/Applications/Postgres.app/Contents/Versions/12/bin/dropdb $DBNAME 
echo "Re-Creating database ..."
/Applications/Postgres.app/Contents/Versions/12/bin/createdb $DBNAME -O $DBUSER

echo "Clearing directories ..."
rm -rf content

echo "Clearing migrations ..."
rm -rf apps/cases/migrations

echo "Running migrations ..."
./manage.py makemigrations
./manage.py makemigrations example 
./manage.py migrate
./manage.py migrate example 

echo "Creating superuser ..."
./manage.py createsuperuser --username "admin" --email "admin@localhost" --noinput
scripts/setadminpw.py
echo "  Done."

