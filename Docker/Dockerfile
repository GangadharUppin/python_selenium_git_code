# Use official Python image
FROM python:3.12-slim

# Metadata
LABEL maintainer="gangadharuppin66@gnmail.com"

# Install required system packages (optional)
RUN apt-get update && apt-get install -y git && apt-get clean

# Set environment variables
ENV VENV_DIR=/venv
ENV REPO_URL=https://github.com/GangadharUppin/python_selenium_git_code.git
ENV BRANCH=master

# Set working directory
WORKDIR /app

RUN echo "Working dir is: $(pwd)"

RUN git clone --branch ${BRANCH} ${REPO_URL} .

#ARG GITHUB_TOKEN
#RUN git clone --branch master https://${GITHUB_TOKEN}@github.com/GangadharUppin/python_selenium_git_code.git .


# Set up virtual environment and install dependencies
RUN python -m venv $VENV_DIR && \
    . $VENV_DIR/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Run tests
CMD ["/bin/bash", "-c", ". /venv/bin/activate && pytest tests/ --maxfail=1 --disable-warnings --tb=short"]
