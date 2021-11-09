# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# These two environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV DEBUG "false"
ENV STATIC_ROOT "/code/files/static/"

# Make a new directory to put our code in.
RUN mkdir /code

# Change the working directory. 
# Every command after this will be run from the /code directory.
WORKDIR /code

RUN apt-get update && apt-get install -y nginx && apt-get clean

# Copy the requirements.txt file.
COPY ./requirements.txt /code/

# Upgrade pip
RUN pip install --upgrade pip

# Install the requirements.
RUN pip install -r requirements.txt

# Copy the rest of the code. 
COPY elecserve/ /code/.
COPY docker/ /code/.
RUN mv nginx.conf /etc/nginx/nginx.conf
RUN python manage.py collectstatic --noinput

CMD ["/code/start.sh"]