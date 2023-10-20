#!/bin/sh

echo "Waiting for PostgreSQL..."
while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done
echo "PostgreSQL accepts connections..."

echo "Running migrations..."
python manage.py migrate --no-input

if ! [ -f /_ ]; then
    echo "from django.contrib.auth.models import User; User.objects.create_superuser(""'""$USER_NAME""', ""'""$USER_EMAIL""', ""'""$USER_PASSWORD""')" | python manage.py shell
    echo "Superuser created:\n$(date)" > /_
fi

if [ "$DJANGO_SETTINGS_MODULE" = "config.settings.production" ]; then
    echo "Collecting static files..."
    python manage.py collectstatic --no-input
fi

exec "$@"
