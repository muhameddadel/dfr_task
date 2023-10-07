FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /task_api
WORKDIR /task_api
COPY . /task_api/
RUN pip install -r requirements.txt
