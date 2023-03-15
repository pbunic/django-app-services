echo "Creating superuser..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser(""'""$DJANGO_ADMIN_USERNAME""', ""'""$DJANGO_ADMIN_EMAIL""', ""'""$DJANGO_ADMIN_PASSWORD""')" | python3 ../manage.py shell
