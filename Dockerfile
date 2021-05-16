FROM ubuntu:latest

RUN apt update
RUN apt install -y python3.8 python3-pip python3.8-dev libpq-dev
RUN ln -s /usr/bin/python3.8 /usr/local/bin/python

COPY requirements.txt /home/ubuntu/requirements.txt
RUN pip install -r /home/ubuntu/requirements.txt

EXPOSE 8000

## How to build
# build an image with the Dockerfile in the current directory, and name the image 'yata'
# $ docker build . -t yata
# $ docker images

## How to run
# YATA files are on your local computer, the docker container hosts the python requirements/server
# eg you can edit yata files on your mac and the changes will be reflected in the container and vice versa
# the below does: boot the 'yata' image, start an interactive terminal, mount the current directory at /mnt, publish the port 8000
# $ docker run -it -v "$PWD:/mnt" -p 8000 yata
# root# cd /mnt
# root:/mnt# python setup.py

# When running the server
# bind to 0.0.0.0 and not 127.0.0.1 to allow access from outside the container
# $ python manage.py runserver 0.0.0.0:8000

# on your browser 
# http://localhost:8000