# Use an official Python runtime as a parent image
FROM python:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY . /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt