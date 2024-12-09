#!/bin/bash
set -e

# Run database migrations
python manage.py migrate

# Create a default superuser if it doesn't exist
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
import os

User = get_user_model()
if not User.objects.filter(username=os.getenv('DJANGO_SUPERUSER_USERNAME')).exists():
    User.objects.create_superuser(
        username=os.getenv('DJANGO_SUPERUSER_USERNAME'),
        email=os.getenv('DJANGO_SUPERUSER_EMAIL'),
        password=os.getenv('DJANGO_SUPERUSER_PASSWORD')
    )
EOF

# Start the server
exec "$@"
