
# Use an official Python base image
FROM python:3.11

RUN echo "Setting working directory as ren_docker_app"
# Set working directory
WORKDIR /ren_docker_app

RUN echo "Installing GIT"
# Install git
RUN apt-get update && apt-get install -y git && \
rm -rf /var/lib/apt/lists/*

# RUN echo "Performing GIT Clone of the given repo"
# Clone your public Git repo
RUN git clone https://github.com/renoldjosethomas/api-automation-python.git

# Set WORKDIR to api-automation-python folder before running the entrypoint.sh
WORKDIR /ren_docker_app/api-automation-python/output

RUN echo "Installing Python Dependencies"
# Install libraries specified in requirements.txt
RUN pip install --no-cache-dir -r ../requirements.txt

RUN echo "Successfully completed the Dockerfile initialization"

# Provide privileges to executable shell script
RUN chmod +x ../docker/entrypoint.sh

# Set CMD to run the script (If multiple CMD commands are specified, only the last one will be executed)
CMD ["../docker/entrypoint.sh"]