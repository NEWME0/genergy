FROM python:3.8

# Install missing libs
RUN apt-get update && apt-get install -y apt-transport-https

# Creating Application Source Code Directory
RUN mkdir -p /usr/app

# Setting Home Directory for containers
WORKDIR /usr/app

# Installing python dependencies
COPY . /usr/app
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate
RUN python manage.py loaddata dumpdata.json

# Expose ports.
EXPOSE 8025
