# django 명령어 입력 방식 : django-admin <command> [options]
  # ex) django-admin help startproject
  # django-admin startproject mysite -> creates a mysite directory in the current directory.

# Django project 안의 핵심 기본 파일들
  # manage.py : A command-line utility that lets you interact with this Django project in various ways.
  # mysite/ : This directory contains the Django project.
    # mysite/__init__.py : An empty file that tells Python that this directory should be considered a Python package.
    # mysite/settings.py : Settings/configuration for this Django project.
    # mysite/urls.py : The URL declarations for this Django project; a “table of contents” of your Django-powered site.


# Django key commands
  # django-admin startproject mysite : creates a mysite directory in the current directory.
  # python manage.py runserver : starts the development server.
  # python manage.py migrate : creates those database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app.
    # migration : a pending change to a database schema. a set of instructions that tells the database how to transform itself from one state to another.
    # when migrate command is run, it checks for any changes to your models (in the mysite/polls/models.py file, in this case) and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app 
  # python manage.py startapp : creates a directory structure for a new app inside your project.

#Application 
  # A Python package that is specifically intended for use in a Django project.
  # Should be self-contained and reusable in different Django projects(in theory).
  # A Django project can contain multiple apps.
  # For Django to recognize an application, it needs to be included in the INSTALLED_APPS setting.


#Templates 
  # A template is a text file that gets processed by Django’s template engine.
  # Pages that are rendered by Django templates are called views.
  # Django templates are written in a subset of Python called Django template language(DTL).