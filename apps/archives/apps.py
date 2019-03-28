from django.apps import AppConfig


class ArchivesConfig(AppConfig):
    name = 'archives'

    def ready(self):
        import archives.signals

