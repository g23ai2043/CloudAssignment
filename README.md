# Create a web application using Docker from scratch

## Author
Name : Abhinandan K R
Roll No: G23AI2043

## Description
This repository contains a simple HTTP server implemented in Python using the http.server module. The server serves static HTML and CSS files and is Dockerized for easy deployment and consistent environments.

### Prerequisites

- Docker installed on your system. [Download Docker](https://www.docker.com/get-started) if not already installed.

## How It Works

### Python HTTP Server Setup

- **Server Script**: The `server.py` script starts a simple HTTP server using the `http.server` module.
- **Listening Port**: The server listens on port 8000 .
- **Request Handling**: When a request is made, the server translates the path to the `static` and `templates` directory and serves the appropriate file.

### Dockerization

- **Dockerfile**: The `Dockerfile` builds an image that sets up the Python environment and copies the server script and static files into the container.
- **Container Setup**: When the container is run, it starts the HTTP server inside the container environment.
- **Port Mapping**: The container maps port 8000 on the host to port 8000 on the container, making the server accessible via [http://localhost:8000](http://localhost:8000).

### Running the Container

- **Starting the Container**: After building the Docker image, the container can be started using `docker run`.
- **Accessing the Server**: The server can then be accessed from a web browser or HTTP client by navigating to [http://localhost:8000](http://localhost:8000).

## Setup

Follow these steps to set up and run the static web server and Dockerized webpage:

### 1. Set Up the Python Web Server

First, set up the Python web server using `server.py` to serve static files:

```
# Clone the repository
git clone https://github.com/g23ai2043/CloudAssignment.git
cd Docker/

```

### 2. Run docker build command

```
# Run the docker build image command 
docker build -t web_app .
```
<p align="center">
  <img src="images/docker-build.jpg">
</p>

### 3. Run docker image

```
# Run the docker image exposing mapping port 8080 to 8080
docker run -p 8080:8080 web_app
```
<p align="center">
  <img src="images/docker-run.jpg">
</p>
We can see that the image and container has been created in docker desktop.
<p align="center">
  <img src="images/docker-image.jpg">
</p>

<p align="center">
  <img src="images/docker-container.jpg">
</p>

### 4. Open localhost on port 8080 in the browser
```
# Open browser and search for localhost
http://localhost:8080
```
<p align="center">
  <img src="images/webpage.jpg">
</p>
