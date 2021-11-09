FROM python:3.8-alpine
MAINTAINER SomeDev

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache --virtual ..build-deps gcc musl-dev mariadb-dev
# for Pillow
RUN apk add jpeg-dev zlib-dev libjpeg

RUN mkdir /app
WORKDIR /app

RUN adduser -D user
USER user

ENV PATH="/home/user/.local/bin:${PATH}"
RUN python -m pip install pip==21.0.1 && pip install --user pipenv

COPY ./Pipfile* /tmp/
RUN cd /tmp && pipenv lock --pre --requirements > requirements.txt && pip install --user -r requirements.txt