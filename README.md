# FASTAPI WITH JWT

**FastAPI, PostgreSQL, SQLAlchemy, Alembic, JWT**

## Dependecies

* Docker
* Docker-compse
* Python >= 3.6
* Pipenv

## How to run

Add the environment variables in the `.env` file.

Start **postgres** database

```shell
docker-compose up -d
```

Start environment

```shell
pipenv shell
```

Install python dependencies

```shell
pipenv install
```

Run **alembic** migrations

```shell
alembic upgrade head 
```

Start application

```shell
uvicorn app.main:app --reload
```
