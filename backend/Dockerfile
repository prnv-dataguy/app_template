# Use the official Python image from Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requrements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code into the container
COPY . .

# Expose the port Uvicorn will run on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "main:app", "--reload", "--reload-include", "page_content.yml", "--host", "0.0.0.0", "--port", "8000"]