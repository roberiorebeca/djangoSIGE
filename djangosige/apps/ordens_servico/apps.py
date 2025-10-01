from __future__ import unicode_literals

from django.apps import AppConfig


class OrdensServicoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ordens_servico'
    label = 'OS'

    def ready(self):
        from . import signals  # noqa