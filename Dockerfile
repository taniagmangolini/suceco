FROM python:3.7

ENV PYTHONUNBUFFERED=1

RUN mkdir /suceco

WORKDIR /suceco

ADD . /suceco

RUN pip install -r requirements.txt