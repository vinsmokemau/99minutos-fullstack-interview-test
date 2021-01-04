# 99minutos interview API

## Installation
You need to have python3, pip and virtualenv or virtualenv wrapper

```sh
pip install -r requirements.txt
```

## Run project

Check for issues:
```sh
python manage.py check
```

If you have to update the db because changes in models.py:
```sh
python manage.py makemigrations
```

Update db with migrations:
```sh
python manage.py migrate
```

Run server:
```sh
python manage.py runserver
```

## Contact

Vinsmoke Mau – [@vinsmokemau](https://twitter.com/vinsmokemau) – mauricio.munguia@makingmex.com


## Endpoints

localhost:8000/branches/
localhost:8000/branches/<str:branch_name>/
localhost:8000/commits/<str:commit_id>/
