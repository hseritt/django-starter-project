#!/usr/bin/env bash

dest="dist"
../format.sh
../rmpyc.sh
rm -rfv $dest/*
rm -rfv ../django_starter/django_starter/static/js/node_modules
mkdir $dest

cp -rfv ../django_starter $dest/.
cp -rfv ../config $dest/.
cp ../manage.py $dest/.
cp -rfv ../resetdb.sh $dest/.
cp -rfv ../scripts $dest/.
cp ../requirements.txt $dest/.
cd $dest/django_starter/static/js
npm install
cd ../../../..
