# Use the official Python base image (Python 3.11)
FROM python:3.11.2

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt file from root to /app directory
COPY ./requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . /app

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
