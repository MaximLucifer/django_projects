from django.apps import AppConfig


class AppfordbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appfordb'

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import appfordb.signals