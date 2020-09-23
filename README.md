# Django Starter Project

This is my latest attempt at a standard Django starter project. It includes a lot of pre-installed components:

* Django Rest Framework
* Authentication (login/logout implemented)
* Npm package.json with latest versions of:
	- Bootstrap (The classic CSS module)
	- Tachyons (CSS with some effects and formatting)
	- jQuery (Still alive and kicking)
	- Vue.js (Very simple JS framework that integrates easily with Django)
* An example app that makes use of DRF and Authentication. Also has examples of bootstrap and vue use.
* NEW! Now with Docker images for testing and distro purposes.

## Install Django Starter Project

How do I install Django Starter Project as my Django project template?

Simple:

```
git clone git@github.com:hseritt/django-starter-project.git
```

This will create a folder called django-starter-project obviously but go ahead and change this folder name to something else more suitable for your project.

Next, change the project's name:

```
cd MyNewProject
chmod +x change-project.sh 
./change-project.sh MyNewProject
```

This will set your project name to MyNewProject in all the right places and delete the .git folder. You'll want to do:

```
git init
```

This will create your own git project.

## Project Structure

```
├── OLD  # Delete this.
├── README.md  # Change this.
├── change-project.sh  # Change name of project. Delete this if you wish.
├── config  # All project configuration.
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings
│   │   └── settings.py  # Effective projects settings file.
│   ├── urls.py  # Top level url routing.
│   └── wsgi.py
├── django_starter  # Where the app lives.
│   ├── __init__.py
│   ├── apps  # You can create your apps here.
│   │   └── __init__.py
│   ├── example  # An example app.
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── templates
│   │   │   ├── example
│   │   │   └── registration
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── static  # Static files
│   │   ├── admin  # For Django admin app.
│   │   │   ├── css
│   │   │   ├── fonts
│   │   │   ├── img
│   │   │   └── js
│   │   ├── css  # Project CSS files.
│   │   │   └── styles.css
│   │   ├── js  # Project JavaScript files.
│   │   │   ├── node_modules  
│   │   │   ├── package-lock.json
│   │   │   ├── package.json
│   │   │   └── script.js  # An example Vue.js script.
│   │   └── rest_framework  # DRF static files.
│   │       ├── css
│   │       ├── docs
│   │       ├── fonts
│   │       ├── img
│   │       └── js
│   └── templates  # Project templates.
│       └── registration
│           └── login.html
├── docker  # All files necessary for Docker test and distribution.
│   ├── Dockerfile
│   ├── build-docker.sh  # Script to build and run Docker images.
│   ├── dist
│   ├── docker-compose.yml
│   ├── nginx
│   │   ├── Dockerfile
│   │   └── nginx.conf
│   ├── pkg-dist.sh  # Creates a distribution of current project.
│   ├── requirements.txt
│   └── teardown-docker.sh  # Script to tear down Docker images.
├── docs
├── format.sh  # A script to remove *.pyc files and run "black".
├── manage.py
├── requirements.txt
├── reset.sh  # A script to rest the database.
├── resetdb.sh  # Same thing. Will consolidate these two eventually.
├── rmpyc.sh  # Removes *.pyc files.
├── runserver.sh  # Starts the dev server with some extra scripts.
├── runtime.txt
├── scripts
│   └── setadminpw.py  # Sets the admin password.
├── settings.py  # A sym link to settings.py
└── startup.sh  # A startup script for Docker version.
```

## Docker

How do I run the Docker containers?

It's pretty easy and should work out of the box.

```
cd docker
./build-docker.sh

and afterwards ...

./teardown-docker.sh
```

While it's running, you can point your browser to:

http://localhost/

and

http://localhost/admin

The default username and password is admin / admin.
