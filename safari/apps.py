from django.apps import AppConfig


class SafariConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'safari'

def ready(self):
    import safari.signals


