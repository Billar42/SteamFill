FROM python:3.10-slim

# Работа с файами

RUN mkdir app
WORKDIR app

ADD . /app/

# Установка приложений

RUN pip install -r requirements.txt

# Уствановка команд

CMD uvicorn main:app --host 0.0.0.0 --port 80
