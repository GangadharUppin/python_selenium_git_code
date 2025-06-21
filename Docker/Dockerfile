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

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

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
