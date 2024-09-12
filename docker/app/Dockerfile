FROM python:3.9.20

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /root/app

COPY requirements.txt /root/app/

WORKDIR /root/app

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install -r requirements.txt