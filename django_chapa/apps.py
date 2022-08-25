from django.apps import AppConfig


class ChapaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chapa'

    def ready(self):
        pass
