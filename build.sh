#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Build complete!"

# Set environment variable for gunicorn timeout
export GUNICORN_CMD_ARGS="--timeout 120 --workers 2"
