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
    docker run -p 5000:5000 docker-git-tutorial
    ```

3. While the docker container is running, you will see the address you can access to see the code. just open your browser and go to: http://127.0.0.1:5000 or http://172.17.0.2:5000

4. You can exit by pressing control+c

## Notes

- If you want to make changes to the Python script, you can edit `Learning/Python/webpage.py` before building the Docker image.

- You can customize the Dockerfile to include additional dependencies or configurations if needed.

- Feel free to explore and experiment with the Python script and Dockerfile as you wish!

