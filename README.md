# Rebbit

First version of **[Erebbit](https://github.com/thetruefuss/erebbit/)** stating "A Socially-Oriented Platform to help developers connect with other developers and share what they know" built with [Python](https://www.python.org/) using the [Django Web Framework](https://www.djangoproject.com/).

### Demo

Check the website at [http://rebbit.pythonanywhere.com](http://rebbit.pythonanywhere.com/)

![Rebbit Screenshot](https://image.ibb.co/ktafvT/rebbit_screenshot.jpg "Rebbit Screenshot")

### Installation Guide

Clone this repository:

```shell
$ git clone https://github.com/thetruefuss/rebbit.git
```

Install requirements:

```shell
$ pip install -r requirements.txt
```

Copy `.env.example` file content to new `.env` file and update the credentials if any i.e Gmail account etc.

Run Django migrations to create database tables:

```shell
$ python manage.py migrate
```

Run the development server:

```shell
$ python manage.py runserver
```

Verify the deployment by navigating to [http://127.0.0.1:8000](http://127.0.0.1:8000) in your preferred browser.
