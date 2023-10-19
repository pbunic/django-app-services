#!/bin/bash
# Set env variables for github testing purposes.

DOTENV=".env"
arr=("DEBUG=True" \
"SECRET_KEY=secret" \
"DJANGO_SETTINGS_MODULE=config.settings.development" \
"ALLOWED_HOSTS=localhost, 0.0.0.0" \
"DB_NAME=blog" \
"DB_USER=postgres" \
"DB_PASSWORD=admin" \
"DB_HOST=localhost" \
"DB_PORT=5432" \
"EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend")

for i in "${arr[@]}"; do
    echo "$i" >> $DOTENV
done