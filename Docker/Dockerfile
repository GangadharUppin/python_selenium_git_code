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

# Install required packages and Google Chrome
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        curl \
        unzip \
        gnupg \
        ca-certificates \
        fonts-liberation \
        libappindicator3-1 \
        libasound2 \
        libatk-bridge2.0-0 \
        libatk1.0-0 \
        libc6 \
        libcairo2 \
        libcups2 \
        libdbus-1-3 \
        libexpat1 \
        libfontconfig1 \
        libgcc1 \
        libgconf-2-4 \
        libgdk-pixbuf2.0-0 \
        libglib2.0-0 \
        libgtk-3-0 \
        libnspr4 \
        libnss3 \
        libpango-1.0-0 \
        libx11-6 \
        libx11-xcb1 \
        libxcb1 \
        libxcomposite1 \
        libxcursor1 \
        libxdamage1 \
        libxext6 \
        libxfixes3 \
        libxi6 \
        libxrandr2 \
        libxrender1 \
        libxss1 \
        libxtst6 \
        lsb-release \
        xdg-utils && \
    wget -q -O google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome.deb && \
    rm google-chrome.deb && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Optional: Check Chrome version (for debugging)
RUN google-chrome --version

# Install matching Chromedriver version
RUN CHROME_VERSION=$(google-chrome --version | grep -oP "\d+\.\d+\.\d+") && \
    CHROMEDRIVER_VERSION=$(curl -sS "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION}") && \
    wget -q "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip" && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip

RUN apt-get update && apt-get install -y git && apt-get clean && rm -rf /var/lib/apt/lists/*

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
