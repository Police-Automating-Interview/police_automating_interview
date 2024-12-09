#!/bin/bash
set -e

# Run database migrations
python manage.py migrate

# Create a default superuser if it doesn't exist
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
EOF

# Start the server
exec "$@"
