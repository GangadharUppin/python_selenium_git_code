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

# Install required system packages
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    ca-certificates \
    git \
    psmisc \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Optional: Check Chrome version (for debugging)
RUN google-chrome --version

# Clone your repo into a temporary directory and move it to /app
RUN git clone --branch ${BRANCH} ${REPO_URL} /tmp/repo && \
    cp -r /tmp/repo/* /app/ && \
    rm -rf /tmp/repo

# Copy requirements.txt only if it's not already in the repo
# COPY requirements.txt .  # Skip this if it's already present in the repo

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set up virtual environment and install dependencies
RUN python -m venv $VENV_DIR && \
    . $VENV_DIR/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Optional: Print working directory
RUN echo "Working dir is: $(pwd)"

RUN echo "Files in /app/tests:" && ls -la /app/tests

# Default command to run tests
CMD ["/venv/bin/pytest", "-v", "tests", "--maxfail=1", "--disable-warnings", "--tb=short"]