# Standard Agentic Data Science Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables to avoid python generating .pyc and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project into the container
COPY . .

# Run the application (Change to your main script)
CMD ["python", "src/main.py"]
