# Let's Quiz


This is an online quiz organizing website project, developed using Python's web framework Django.<br>
For front-end designing I have used Twitter's front-end library Bootstrap4.


## Current Features

### Site access features:

- User must be logged in to access the Quiz.
- For signup user is required to give _username_, _first name_, _last name_, _e-mail address_ and _password_.
- For login the user will be required to enter _username_ and _password_ only.

### Features of the quiz:

- All questions are multiple choice question.
- Each question is displayed only once per user.
- Questions are displayed randomly for every user.
- If the user by-mistake presses refresh or go back to the previous page, there will be a new question for the user and the
  question he/she was on will be marked as attempted.
- A message will be displayed after every attempted question whether the answer was correct or incorrect.

### Leaderboard features:

- Leaderboard is a shorted list according to the score obtained by the users.
- If two users are having same score, the user who has signed up earlier will have good ranking than the one who joined late.
- Leaderboard is open to all. No login required.

### Administrative features:

- Only admin can add questions.
- Admin can add questions and modify them until they are not marked as _Has been published?_
- Once a question has been published, it can neither be modified nor can be accessed. Admin can only see a list of questions.
- Admin can search questions by question text or choice text.
- Admin can filter questions based on whether the questions have been published or not.

## Getting started with development

Dependencies:

- Python 3.11.6
- Django 5.0.3
- Ubuntu 17.04 or later or Linux Mint 18.2 or later

### 1. Install [Pipenv](https://pipenv.pypa.io/en/latest/)

### 2. Create the virtualenv

```bash
## run following command from `lets_quiz` directory
pipenv install django-model-utils==4.4.0
# pip install django-model-utils  if errror is coming again
pip install --upgrade pipenv
pipenv lock
pipenv --rm
pipenv --python 3.11.6
pipenv install
pipenv shell
```

### 3. Install python packages

```bash
pip install -r requirements.txt
```

### 4. Setup the database

can be done in the following way:


<!-- 
mysql -u root -p
CREATE DATABASE my_database;
GRANT ALL PRIVILEGES ON my_database.* TO 'my_user'@'localhost' IDENTIFIED BY 'my_password';
FLUSH PRIVILEGES; 
-->

<!-- set DJANGO_SETTINGS_MODULE=lets_quiz.settings -->

### 5. Run database migrations

```bash
cd lets_quiz
python manage.py makemigrations quiz
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Run development server

```bash
python manage.py runserver
```


Reference was taken from "https://github.com/akashgiricse/lets-quiz"