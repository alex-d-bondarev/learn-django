# learn-django

> [!NOTE]  
> **Archived** since I have learned what I planned to and no longer plan to commit new changes

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

## General docker
```shell
# Build
export TAG="demo"
docker build -t alexdbondarev/learn-django:${TAG} .

# Run
docker run --rm -it -p 80:8000 alexdbondarev/learn-django:${TAG}
docker run -d -p 80:8000 alexdbondarev/learn-django:${TAG} # as daemon
# Links like http://127.0.0.1/app_example/links/ should start working

# Push
docker push alexdbondarev/learn-django:${TAG}

# Start and Debug
docker run --rm -it -p 80:8000 --entrypoint bash alexdbondarev/learn-django:${TAG}

# Debug the running container
docker ps
docker exec -it <CONTAINER ID> bash
# update "/project/learn_dj/app_example/files" file 
# and check http://127.0.0.1/app_example/hello/ for updates
```

## Raspberry Py 3 Docker demo
```shell
# Build and push
export ARM_TAG="demo-arm"
poetry export -f requirements.txt --output requirements.txt
docker build --platform linux/arm/v7 -f Dockerfile-arm -t alexdbondarev/learn-django:${ARM_TAG} .
docker run --platform linux/arm/v7 --rm -it -p 80:8000 alexdbondarev/learn-django:${ARM_TAG}
docker push alexdbondarev/learn-django:${ARM_TAG}

 

# Pull and start an image
docker pull alexdbondarev/learn-django:demo-arm
docker run -d -p 80:8000 alexdbondarev/learn-django:demo-arm

# Install ngrok
# use commands from https://dashboard.ngrok.com/get-started/setup/linux to install and set token
ngrok http http://localhost:80
```

