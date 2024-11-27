# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies for Hugging Face
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the AI service code into the container
COPY ./ /app

# Expose the port for the AI service
EXPOSE 5000

# Command to start the AI service (assuming Flask for the API)
CMD ["python", "ai_service.py"]
