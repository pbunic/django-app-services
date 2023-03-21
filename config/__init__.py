from decouple import config


is_production = bool(config('DJANGO_SETTINGS_MODULE') == 'config.settings.production')

if is_production:
    try:
        from .celery import app as celery_app
        __all__ = ('celery_app',)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import celery. Something is improperly configured. "
            "Checkout out if celery is installed and other requirements and/or"
            "check if your virtual environment is activated."
        ) from exc
