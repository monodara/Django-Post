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
ENV PORT=8080

# Collect static files
RUN python manage.py collectstatic --noinput

# Start the application - Use Google Run provided PORT
CMD gunicorn mysite.wsgi:application \
  --bind 0.0.0.0:$PORT \
  --workers 1 \
  --threads 4 \
  --timeout 0 \
  --log-level debug \
  --error-logfile - \
  --access-logfile -


