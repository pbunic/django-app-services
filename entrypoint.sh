#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done

echo "PostgreSQL started"
echo "Running migrations..."
python3 manage.py migrate --no-input

if [ "$DJANGO_SETTINGS_MODULE" = "config.settings.production" ]; then
    echo "Collecting static files..."
    python3 manage.py collectstatic --no-input
fi

exec "$@"
