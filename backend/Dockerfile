# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install FastAPI and Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn

# Install any other dependencies for the backend (e.g., database libraries)
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container
COPY ./app /app

# Expose the backend port
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
