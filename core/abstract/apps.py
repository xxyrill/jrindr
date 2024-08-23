from django.apps import AppConfig


class AbstractConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.abstract'
    label = 'core_abstract'

