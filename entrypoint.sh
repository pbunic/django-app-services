#!/bin/sh

echo "Waiting for PostgreSQL..."
while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done
echo "PostgreSQL accepts connections..."

echo "Running migrations..."
python manage.py migrate --no-input

SU_TRUE=$(echo "import sys; from django.contrib.auth.models import User; \
\nif User.objects.filter(is_superuser=True).exists(): \
sys.stdout.write('true')" | python manage.py shell)

if [ "$SU_TRUE" = "true" ]; then
    echo "Superuser exists."
else
    echo "from django.contrib.auth.models import User; User.objects.create_superuser(""'""$USER_NAME""', ""'""$USER_EMAIL""', ""'""$USER_PASSWORD""')" | python manage.py shell
    echo "\nSuperuser created: $USER_NAME\n$(date)"
fi

if [ "$DJANGO_SETTINGS_MODULE" = "config.settings.production" ]; then
    echo "Collecting static files..."
    python manage.py collectstatic --no-input
fi

exec "$@"

