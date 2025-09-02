#!/bin/bash
# Django migration script

echo "⚙️ Running makemigrations..."
python manage.py makemigrations

echo "⚙️ Applying migrations..."
python manage.py migrate
