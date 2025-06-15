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
    pip install -r requirements.txt \

# Install latest Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /etc/apt/trusted.gpg.d/google.gpg \
 && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
 && apt-get update \
 && apt-get install -y google-chrome-stable

# Install Chromedriver (automatically match latest Chrome version)
RUN CHROME_VERSION=$(google-chrome --version | grep -oP '[0-9.]+' | head -1) && \
    CHROMEDRIVER_VERSION=$(curl -sS "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${CHROME_VERSION%.*}") && \
    curl -sS -o /tmp/chromedriver.zip "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip" && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver.zip /usr/local/bin/chromedriver-linux64


# Run tests
# CMD ["/bin/bash", "-c", ". /venv/bin/activate && pytest tests/ --maxfail=1 --disable-warnings --tb=short"]
CMD ["/venv/bin/pytest", "tests/", "--maxfail=1", "--disable-warnings", "--tb=short"]
