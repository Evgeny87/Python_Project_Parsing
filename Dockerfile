# собрать билд докера командой docker build . -t var-app
# запустить докер контейнер командой docker run var-app
FROM python:3.10.6-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip install --upgrade pip && \
    pip install poetry==1.3.2

RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./

RUN poetry install --only main

COPY . .

# EXPOSE 8000

# CMD uvicorn main:app --host 0.0.0.0 --port=8000
