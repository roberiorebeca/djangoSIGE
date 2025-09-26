from __future__ import unicode_literals

from django.apps import AppConfig


class EstoqueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # opcional, mas recomendado em versões novas
    name = 'djangosige.apps.estoque'  # <<< use o caminho completo do pacote
    label = 'estoque'  # opcional; mantém o rótulo curto no banco/admin  
