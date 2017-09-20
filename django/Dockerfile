FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH="/"

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD handle_file_changed.py /handle_file_changed.py

ADD uwsgi.ini /uwsgi.ini

RUN mkdir webapp
WORKDIR /webapp
