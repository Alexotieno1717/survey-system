# Django Survey


# Author

Alex Otieno

### [Checkout the demo application hosted on heroku](https://surveyapp001.herokuapp.com/survey/). 

### Admin Login
Username: admin <br/>
pass: admin

## Features:
  - Admins need to be able to log in to the backend.
  - Admins should be able to create surveys, together with the survey questions.
  - The questions need to have 2 options each.
  - Admins need to be able to access survey reports;
  - Participants details reports
  - The public need to be able to access the created surveys and fill out their options.

 
## Installation and Launching the application

### Requirements:

- python version > 3.9.5 installed

```cmd
python -m pip install django
```
- nested-admin > 3.3.3 installed
```cmd
pip install django-nested-admin 
```

### Run
#### Check for possible schema changes while using the version control as well as for the first run. 
Navigate to the project directory (where manage.py is located) and run
  ```cmd
  python manage.py makemigrations survey
  ```

#### Commit  all changes to the databases. This also creates necessary tables in the database.
  ```cmd
  python manage.py migrate
  ```
#### Collect all static assets and add to build/root folder in main application scope
  ```cmd
  python manage.py collectstatic
  ```
#### Create an admin user for the application
  ```cmd
  python manage.py createsuperuser
  ```
#### Run the development server
  ```cmd
  python manage.py runserver
  ```



## Languages Used
 - [django](https://www.djangoproject.com/)
 - [nested-admin](https://github.com/django/django/tree/master/django/contrib/admin)
 - python
 - [JQuery](https://jquery.com/)
 - [db Bootstrap](https://mdbootstrap.com/)
 - [chart.js](https://www.chartjs.org/)


License
 - MIT License
 - Copyright © 2020 | Alex Otieno