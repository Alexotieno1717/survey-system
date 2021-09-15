# Django Survey


# Author

Alex Otieno

### [Checkout the demo application hosted on heroku](https:/herokuapp.com/survey/). 
Use admin/admin as credentials to login to admin page.
### Admin Login
Username: 
pass: 

## Features:
 - The polls application is extended to a survey where admin can create multiple surveys with multiple questions and choices for each question.
 - The dashboard is enriched with a statistics widget. The widget displays the popular survey among the surveys and the bar chart visualization of vote distributions among different choices for a question.

 
## Installation and Launching the application

### Requirements:

- python version > 3.6 installed
- django version > 3.1.5 installed
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






