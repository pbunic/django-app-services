from decouple import config

settings_env = config('DJANGO_SETTINGS_MODULE')
production = bool(settings_env == 'production')

if production:
    try:
        from .celery import app as celery_app
        __all__ = ('celery_app',)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import celery. Something is improperly configured."
        ) from exc
