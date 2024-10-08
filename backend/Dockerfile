# backend/Dockerfile
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install system dependencies for your application
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire backend code
COPY . .

# Expose the Flask port
EXPOSE 5000

# Set environment variables
ENV SQL_SERVER=${SQL_SERVER}
ENV SQL_DATABASE=${SQL_DATABASE}
ENV SQL_USERNAME=${SQL_USERNAME}
ENV SQL_PASSWORD=${SQL_PASSWORD}

# Command to run the application
CMD ["python", "-m", "backend.app"]
