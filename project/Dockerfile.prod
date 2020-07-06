# pull official python image
FROM python:3.8.3-slim-buster

# set the working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set the environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install the system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

# install the python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

