# Running the Turtle Graphics Docker Container

This repository contains a Dockerfile and a Python script that utilizes Turtle Graphics. You can use Docker to run this Python script inside a Docker container without worrying about installing dependencies on your local machine.

## Prerequisites

- Docker installed on your system. You can download and install Docker from [here](https://www.docker.com/get-started).

## Instructions

1. Build the Docker image:

    ```bash
    docker build -t docker-git-tutorial .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 5000:5000 --name my-container docker-git-tutorial    
    ```

    The Turtle Graphics window should appear, displaying the graphics generated by the Python script.

3. To exit the Turtle Graphics window, simply close it. The Docker container will automatically stop and remove itself (`--rm` flag).

## Notes

- If you want to make changes to the Python script, you can edit `canvas.py` before building the Docker image.

- You can customize the Dockerfile to include additional dependencies or configurations if needed.

- Feel free to explore and experiment with the Python script and Dockerfile as you wish!
