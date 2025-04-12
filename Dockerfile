# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your app files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir flask boto3

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
