# Base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Environment variables
ENV PYTHONUNBUFFERED=1

# Collect static files
RUN python manage.py collectstatic --noinput

# Start the application - Use Google Run provided PORT
CMD exec gunicorn myproject.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2

