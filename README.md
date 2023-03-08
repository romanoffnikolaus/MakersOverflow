# MakersOverflow
Visit our website: [MakersOverflow](https://makersoverflow.net/)

Content
* [Description](#Description)
* [Make commands](#Makecommands)
* [Installation](#Installation)
## Description
Forum for Makers students and mentors. Users may discuss/ask questions and get an answer, upvote/downvote comments and answers for getting rating point. If your rating more then 3000 you get a "fireman" status. In addition to that you can find similar questions with answers on "MakersOverflow" and use parser to find similar question on StakOverflow.

## Make commands
You can use following make commands:

```bash
make run
```
to run the server instead of using:
```bash
python manage.py runserver
```
##
```bash
make migrate
```
to make migrations instead of using:
```bash
python manage.py makemigrations
python manage.py migrate
```
There are other make commands which you can look up in Makefile. You don't have to use them, we made them just for your convenience
##
Also check .env_template to get more information about required data for .env.

## Installation
1. Install [celery]((https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)) + [redis](https://redis.io/)

2. Create virtual machine
```bash
python3 -m venv <venv_name>
```
3. Activate your virtual machine
```bash
. venv/bin/activate
```
4. Install all the dependencies
```bash
pip install -r requirements.txt
```
5. Make changes into database by making migrations
```bash
# First step
python manage.py makemigrations
# Second step
python manahe.py migrate
```
6. Create an admin-user
```bash
python manage.py createsuperuser
```
7. You're almost there!
```bash
python manage.py runserver
```
8. Run celery so your registered users will be able to get verification code on their email
```bash
# use second terminal
python3 -m celery -A core worker -l info
```
Visit our website: [MakersOverflow](https://makersoverflow.net/)
