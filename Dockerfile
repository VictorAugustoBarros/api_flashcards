FROM python:3.8

MAINTAINER Victor Augusto

WORKDIR /flashcards

COPY requirements.txt /flashcards

COPY . /flashcards/

RUN pip install pip --upgrade

RUN pip install -r requirements.txt