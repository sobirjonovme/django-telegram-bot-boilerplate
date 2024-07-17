# django-python-telegram-bot-boilerplate

<p align="center">
    <img src="https://blog.hachther.com/wp-content/uploads/2017/12/django-telegram.png" align="center" height="350px" weight="350px">
</p>

### Inspired by [Daniil Okhlopkov](https://github.com/ohld)'s [django-telegram-bot](https://github.com/ohld/django-telegram-bot) boilerplate

Django + python-telegram-bot + Postgres + Celery + Redis + Docker template. Production-ready Telegram bot with database, admin panel and a bunch of useful built-in methods.


### <span style="color:#035c02"> If you want synchronous version of this boilerplate, check out [sync_version](https://github.com/sobirjonovme/django-telegram-bot-boilerplate/tree/sync_version) branch. </span>


## Features

* Database: PostgreSQL, Sqlite3, MySQL - you decide! (default is Postgres)
* Admin panel: [Django](https://docs.djangoproject.com)
* Background jobs: [Celery](https://docs.celeryproject.org/en/stable/)
* Production-ready deployment using [Docker](https://docs.docker.com/)
* Telegram API usage in polling or webhook mode using [python-telegram-bot](https://docs.python-telegram-bot.org/)


# How to run locally

## Quickstart:

The fastest way to run the bot is to run it in polling mode using SQLite database without all Celery workers for background jobs. This should be enough for quickstart:

``` bash
git clone https://github.com/sobirjonovme/django-telegram-bot-boilerplate.git project_name
cd project_name
```

Create virtual environment (optional)
``` bash
python3 -m venv env
source env/bin/activate
```

Install all requirements:
```
pip install -r requirements/develop.txt
```

Create `.env` file in root directory and fill it using .env.example file or just run `cp .env.example .env`,
don't forget to change telegram token:

Run migrations to setup database:
``` bash
python manage.py migrate
```

Create superuser to get access to admin panel:
``` bash
python manage.py createsuperuser
```

If you want to open Django admin panel which will be located on http://localhost:8000/admin/:
``` bash
python manage.py runserver
```

#### Now you have 2 options to run the bot:
1. Polling mode:
    ``` bash
    python manage.py run_polling
    ```
2. Webhook mode:

    In this case you need to setup your webhook URL and run the server using ngrok or any other tunneling service.
    Change `HOST` in `.env` file to your ngrok URL and run following command so that Telegram know where to send updates:
    ``` bash
    python manage.py set_webhook
    ```

## Run using docker-compose
If you want just to run all the things locally, you can use Docker-compose which will start all containers for you.

### Create .env file.
```bash
cp .env.example .env
```

### Docker-compose

To run all services (Django, Postgres, Redis, Celery) at once:
``` bash
docker-compose up --build -d
```

Check status of the containers.
``` bash
docker ps -a
```

Try visit <a href="http://0.0.0.0:8000/admin">Django-admin panel</a>.

### Enter django shell:

``` bash
docker exec -it web bash
```

### Create superuser for Django admin panel

``` bash
python manage.py createsuperuser
```

### To see logs of the container:

``` bash
docker logs -f web
```
