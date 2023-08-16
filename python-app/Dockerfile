# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory within the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages
RUN pip install Flask

# Run the hostname -I command and store the output in an environment variable
RUN export HOST_IP=$(hostname -I)

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV HOST_IP=$HOST_IP

# Run app.py when the container launches
CMD ["python", "app.py"]

