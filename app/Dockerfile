FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app/

# Run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
