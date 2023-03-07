#!/bin/sh

echo "Waiting for postgres..."

while [ ! nc -z $DB_HOSTNAME $DB_PORT ]; do
    sleep 0.1
done

echo "PostgreSQL started"

echo "Running migrations..."
python3 ./my_blog/manage.py migrate

# echo "Collecting static files..."
# python3 ./my_blog/manage.py collectstatic --no-input

echo "Creating superuser..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser(""'""$DJANGO_ADMIN_USERNAME""', ""'""$DJANGO_ADMIN_EMAIL""', ""'""$DJANGO_ADMIN_PASSWORD""')" | python3 ./my_blog/manage.py shell

echo "ADMIN PANEL: localhost:8000/admin"
echo "USERNAME: $DJANGO_ADMIN_USERNAME"
echo "PASSWORD: $DJANGO_ADMIN_PASSWORD"

exec "$@"
