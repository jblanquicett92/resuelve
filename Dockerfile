FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip3 install -r requirements/prod.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

EXPOSE 8000

CMD gunicorn app.wsgi:application --bind 0.0.0.0:$PORT