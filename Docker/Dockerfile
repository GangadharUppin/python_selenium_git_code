# Use official Python image
FROM python:3.12-slim

# Metadata
LABEL maintainer="gangadharuppin66@gnmail.com"

# Environment variables
ENV VENV_DIR=/venv
ENV REPO_URL=https://github.com/GangadharUppin/python_selenium_git_code.git
ENV BRANCH=master

# Set working directory
WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    ca-certificates && \
    curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    google-chrome --version


# Install Chrome
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Optional: Check Chrome version (for debugging)
RUN google-chrome --version

# Print working directory
RUN echo "Working dir is: $(pwd)"

# Clone your repo
RUN git clone --branch ${BRANCH} ${REPO_URL} .

# Set up virtual environment and install dependencies
RUN python -m venv $VENV_DIR && \
    . $VENV_DIR/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Set command to run tests
CMD ["/venv/bin/pytest", "tests/", "--maxfail=1", "--disable-warnings", "--tb=short"]
