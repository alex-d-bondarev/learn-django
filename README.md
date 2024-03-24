# teach-pr

## How to install
### Very first time
```shell
django-admin startproject learn_dj
cd learn_dj
python3 manage.py startapp app_example
```

### All other times
```shell
poetry install
```

## How to run
```shell
cd learn_dj
python3 manage.py runserver
```

## How to add templates
```shell
cd learn_dj
python3 manage.py migrate
# After updating settings.py
python3 manage.py makemigrations app_example
python3 manage.py migrate
```
