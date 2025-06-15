# Use official lightweight Python 3.12 image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# print pwd
RUN pwd

# Environment settings for cleaner Python logs and faster installs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies (add more if needed, like for Selenium)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc curl build-essential libssl-dev libffi-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy your project files
COPY . .

# Default command (can be overridden in Jenkins)
CMD ["pytest", "tests/"]
