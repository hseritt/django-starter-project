#!/usr/bin/env bash

DBNAME="django_starter"
DBUSER="admin"
DJANGO_ADMIN_USERNAME="admin"
DJANGO_ADMIN_EMAIL="admin@localhost"
DJANGO_ADMIN_PASSWORD="admin"

# printf "\33c\e[3J"

echo "Resetting database and resetting migration ..."

echo "Clearing content directory"
rm -rf content
echo "    Done."

echo "Clearing log files."
rm -rf *.log
echo "    Done."

echo "  Dropping database: $DBNAME"
/Applications/Postgres.app/Contents/Versions/latest/bin/dropdb $DBNAME
echo "    Done."

echo "  Recreating database: $DBNAME"
/Applications/Postgres.app/Contents/Versions/latest/bin/createdb $DBNAME -O $DBUSER
echo "    Done."

echo "  Clearing old migrations"
rm -rf example/migrations
echo "    Done."

echo "  Creating new migrations ..."
./manage.py makemigrations
./manage.py makemigrations example 

echo "  Migrating new schema ..."
./manage.py migrate
./manage.py migrate example 
echo "    Done."

./manage.py createsuperuser --username $DJANGO_ADMIN_USERNAME --email $DJANGO_ADMIN_EMAIL --noinput
scripts/setadminpw.py $DJANGO_ADMIN_USERNAME $DJANGO_ADMIN_PASSWORD

# echo "Adding initial data ..."
# scripts/init_data.py
echo "    Done."
