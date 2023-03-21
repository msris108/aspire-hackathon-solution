FROM python:3.10-alpine

RUN apk update && apk add python3-dev gcc libc-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY . /app

WORKDIR /app

RUN python ./manage.py migrate
RUN echo "Backend Docker Image Built Successfully"