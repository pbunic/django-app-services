## platform (work in progress)
[![Django CI](https://github.com/noctdruid/blog/actions/workflows/django-ci.yml/badge.svg)](https://github.com/noctdruid/blog/actions/workflows/django-ci.yml)

Private stack project, it's just for presentation purposes.

For now work includes:
- Django web app project skeleton
- Nginx web server for serving public/private content
- Prometheus metrics collecting
- Grafana dashboards visualization
- PostgreSQL web user interface
- Redis web user interface

Future work will include:
- Full-featured blogging options
- Procreative automation scripts
- Configuration files for Linux host
- SFTP server for files upload/backup
- VPN proxy for administration
- E2E encryption email service

---

Try stack locally:
1. Install docker-engine and plugins (cli, buildx, compose)  
`https://docs.docker.com/engine/install/`

2. Create .env file, here is one provided for faster run-up  
```
DEBUG=False
SECRET_KEY='secret'
DJANGO_SETTINGS_MODULE=config.settings.production
ALLOWED_HOSTS='*'
NGINX_PORT=80

# postgres database
DB_NAME=blog
DB_USER=postgres
DB_PASSWORD=admin
DB_HOST=pgmaster
DB_PORT=5432

# django admin configurations
USER_NAME=admin
USER_EMAIL=admin@example.com
USER_PASSWORD=admin123

# email config
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='email'
EMAIL_HOST_PASSWORD='emailpass'
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False

# celery, redis
CELERY_BROKER_URL=redis://:redispass@redis:6379/0
REDIS_BACKEND=redis://:redispass@redis:6379/0
REDIS_HOSTS=redis
REDIS_HOST=redis
REDIS_PORT=redis:6379
REDIS_PASSWORD=redispass
HTTP_USER=root
HTTP_PASSWORD=root
URL_PREFIX=/redis

# alert
ALERT_EMAIL='admin@example.com'
```

3. Verify that you added user in docker group and run docker compose  
`docker compose -f docker-compose.prod.yml up -d`