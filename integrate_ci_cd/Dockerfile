# Use official Python image
FROM python:3.12-slim
# Set working directory
WORKDIR /app

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Default command
CMD ["pytest", "tests", "-v"]
