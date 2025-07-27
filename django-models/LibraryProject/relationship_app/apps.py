from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'


class DjangoModelsConfig(AppConfig):
    name = 'django-models'

    def ready(self):
        import django_models.signals  # Make sure to import signals

