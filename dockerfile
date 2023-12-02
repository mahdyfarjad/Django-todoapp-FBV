# Use an official Python runtime as a parent image
FROM python

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./core /app/
# Copy the requirements direectory into the /app
COPY requirements.txt /app/

# update pip
RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

