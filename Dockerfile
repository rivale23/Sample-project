# This is used as a base image for dLearning/Python/ocker, basically, it downloads a docker image from internet, in this case it has python, but you can download linux and then put python or whatever you want
FROM python:3.7-slim


# now, this is a folder inside docker container
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the Docker image
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the Python script from your computer to  into the docker image
COPY Learning/Python/canvas.py .
COPY Learning/Python/templates/index.html ./templates/
COPY Learning/Python/webpage.py .

# Expose port 5000 to the outside world
EXPOSE 5000

CMD [ "python3", "webpage.py" ]
