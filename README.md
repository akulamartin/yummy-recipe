
[![Build Status](https://travis-ci.org/akulamartin/yummy-recipe.svg?branch=master)](https://travis-ci.org/akulamartin/yummy-recipe) [![Coverage Status](https://coveralls.io/repos/github/akulamartin/yummy-recipe/badge.svg?branch=master)](https://coveralls.io/github/akulamartin/yummy-recipe?branch=master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/513d3e6806a6426db8d1a6fb78953992)](https://www.codacy.com/app/akulamartin/yummy-recipe?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=akulamartin/yummy-recipe&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/abbeb0a33a588ec589c9/maintainability)](https://codeclimate.com/github/akulamartin/yummy-recipe/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/abbeb0a33a588ec589c9/test_coverage)](https://codeclimate.com/github/akulamartin/yummy-recipe/test_coverage)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/513d3e6806a6426db8d1a6fb78953992)](https://www.codacy.com/app/akulamartin/yummy-recipe?utm_source=github.com&utm_medium=referral&utm_content=akulamartin/yummy-recipe&utm_campaign=Badge_Coverage)

# Yummy Recipe

The recipe app is an application that allows users to record and share recipes they have collected.The application implements CRUD and meets the needs of keeping track of the recipes by using categories. 

## Getting started:
The following instructions will enable you to get your application up and running on your local machine
where you can develop and test the application to suite your needs. 

- To clone this repository  type: `git clone https://github.com/akulamartin/yummy-recipe.git`
  if you are using vscode it will open the repository for you
- Install project requirements using python pip.There are some prerequisites for you to do:

### Prerequisites

- Python3.5 and above
- Python virtual environment
Just type:
```
python -V
```
in your terminal to check the version.

### Installation
 
Lets set up the project environment.

1. Create your virtual environment. Usually, without any wrappers:
```
python -m venv my_venv
```
2. Start your virtual environment:
```
source my_venv/bin/activate
```
3. Install the project requirements specified in the requirements.txt file. Usually,
```
pip install -r requirements.txt
```

This is enough to get you started.
You can now run the application using:
`gunicorn runapp:app`
or
`python runapp.py`


## Running the tests

Easy, just type:
`nosetests test_run`

## Deployment

You can deploy your copy of this app by:
`heroku create <your_url_name>` (where <your_url_name> is what you want to call your app)
`git push heroku master` 

You can learn how to [Deploy Python Applications on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)

## It has been built with:
* HTML
* BOOTSTRAP
* Python Flask

## Authored by:

Martin Akula

## Acknowledgments

* Andela Kenya.
