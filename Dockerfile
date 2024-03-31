FROM python:3.11-slim

RUN pip install poetry~=1.5 \
    && mkdir -p project

ENV PATH="/root/.local/bin:${PATH}"

COPY . /project
WORKDIR /project
RUN poetry env use `python3 --version | grep -Eo '[0-9]+([.][0-9]+)+([.][0-9]+)?'` \
    && poetry install --compile

EXPOSE 8000
ENTRYPOINT ["poetry", "run", "python3", "/project/learn_dj/manage.py", "runserver", "0.0.0.0:8000"]
