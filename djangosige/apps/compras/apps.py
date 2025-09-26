from __future__ import unicode_literals

from django.apps import AppConfig


class ComprasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # opcional, mas recomendado em versões novas
    name = 'djangosige.apps.compras'  # <<< use o caminho completo do pacote
    label = 'compras'  # opcional; mantém o rótulo curto no banco/admin  
