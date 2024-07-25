# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Expose port 8080
EXPOSE 8080

# Command to run the HTTP server
CMD ["python", "server.py"]