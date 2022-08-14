FROM python:3.9-slim-buster

ENV PYTHONIOENCODING utf-8
ENV TZ="Asia/Tokyo"
ENV LANG=C.UTF-8
ENV LANGUAGE=en_US:en

WORKDIR /var/www/html/backend

COPY ./docker/backend/requirements.txt /tmp/requirements.txt

RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev

RUN pip install -r /tmp/requirements.txt
