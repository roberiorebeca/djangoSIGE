from __future__ import unicode_literals

from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # opcional, mas recomendado em versões novas
    name = 'djangosige.apps.base'  # <<< use o caminho completo do pacote
    label = 'base'  # opcional; mantém o rótulo curto no banco/admin
