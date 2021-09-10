# pull official base image
FROM python:3.9.7-alpine

# set work directory
WORKDIR /c/Users/rfrolov/Documents/work/digital-sign-storage

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .