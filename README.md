# Taskmaster

Taskmaster is an essential todo app that enables you to get ahead of your tasks

## Get started

### Prerequisites

Numbers in parentheses indicate the version used by creator. In case of any issues, first try to match the versions to debug.

* Python (3.8.5)

   It's a Django project and Python is the first requirement. You may use Python or Anaconda, they both work.

* Django (3.0.5)

   The project uses the latest iteration of Django, viz 3. There are a few breaking changes in Django 3 and Django 2, but chances are we will not see them in this project. However, I strongly recommend using Django 3 for version compatibility.

* Djongo (1.3.3)

   Instead of sqlite, the project uses MongoDB as the database. Djongo is a transpiler to convert SQL queries to mongoDB query documents.

* MongoDB (3.6.8)

   Install MongoDB for your platform from a corresponding source.

### Set up

#### 1. Install packages

   All details as mentioned above

#### 2. Clone/pull

   Perform a `git clone` or `git pull`

#### 3. Create a MongoDB

   The project uses a MongoDB named `taskmaster`

#### 4. Optional: Create a superuser

   Create one for administrative purposes by `python manage.py createsuperuser`
