# User instructions

The software has been deploeyd in 
[Heroku](https://semantic-tree-generator.herokuapp.com/)

## Run the application on command prompt

- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- flask run
- Open url

## Run tests

- coverage run --branch -m pytest src

## Generate coverage report

- coverage html

## Pylint

- pylint src

# Poetry (doesn't work??)

## Run the application on command prompt

In the last testing poetry install freezed and didn't worked at all. These instructions might work for you, but the instructions above hopefully to everyone.

- poetry install
- poetry run invoke start
- Open url

## Run tests 

- poetry run invoke test

## Generate coverage report

- poetry run invoke coverage-report

## PyLint

- poetry run invoke lint

