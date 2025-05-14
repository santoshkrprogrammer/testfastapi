# Use the official Python base image
FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1
# Set the working directory inside the container
WORKDIR /app



# Install necessary build tools and dependencies
# Install dependencies, including FreeTDS for pymssql
RUN apt-get update && apt-get install -y \
    build-essential \
    freetds-dev \
    libkrb5-dev \
    libssl-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*



# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8000

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]