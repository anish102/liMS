The library management system is created to be used solely by the library administrations. I also made the assumption that the library contains only one of the particular book.

Setup:
Generally, it is recommended to do project in the python virtual environment, so did I.
First, create the python virtual environment through the command: python -m venv env_name
The environment can be activated by the command: source env_name/bin/activate
Then install the required tools and packages which I have listed on requirements.txt file which can be directly installed through the command: pip install -r requirements.txt
Then create the django project: django-admin startproject project_name
Then create the django app: python manage.py startapp app_name
Then setup the database to integrate with django.
Add the installed apps such as django rest framework and the created app as well as database properties on settings.py file.
Create a serialiers.py file to serialize output of the response.
Add your logics and data schema to views.py and models.py file.
Create the url to map the api endpoints to the respective view functions.
Make sure all the api endpoints are working as desired.
Finally, push the project in remote github repository.

Api description:
