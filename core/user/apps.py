from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.user'
    label = 'core_user'     # ADD THIS AT THE END OF THE CMD IN RUNNING python manage.py migrate
                            # OR python manage.py makemigrations
