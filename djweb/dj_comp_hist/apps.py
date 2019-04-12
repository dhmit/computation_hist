from django.apps import AppConfig


class DjCompHistConfig(AppConfig):
    name = 'dj_comp_hist'

    def ready(self):
        import dj_comp_hist.signals

