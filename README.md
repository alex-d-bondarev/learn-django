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

## How to run docker
```shell
# Build
docker build --platform linux/amd64 -t learn_dj .

# Run
docker run --platform linux/amd64 --rm -it -p 80:8000 learn_dj
# Links like http://127.0.0.1/app_example/links/ should start working

# Start and Debug
docker run --platform linux/amd64 --rm -it -p 80:8000 --entrypoint bash learn_dj

# Debug the running container
docker ps
docker exec -it <CONTAINER ID> bash
# update "/project/learn_dj/app_example/files" file 
# and check http://127.0.0.1/app_example/hello/ for updates
```
