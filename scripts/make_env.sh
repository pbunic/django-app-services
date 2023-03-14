#!/bin/bash
# Set env variables for testing purpose.

env_var="../.env"

echo "DEBUG=True" >> $env_var
echo "SECRET_KEY=secret" >> $env_var
echo "DJANGO_SETTINGS_MODULE=config.settings.development" >> $env_var
echo "ALLOWED_HOSTS=localhost, 0.0.0.0" >> $env_var
echo "DB_NAME=blog" >> $env_var
echo "DB_USER=postgres" >> $env_var
echo "DB_PASSWORD=admin" >> $env_var
echo "DB_HOST=localhost" >> $env_var
echo "DB_PORT=5432" >> $env_var
echo "EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend" >> $env_var