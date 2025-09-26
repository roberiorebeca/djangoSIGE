from __future__ import unicode_literals

from django.apps import AppConfig


class VendasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # opcional, mas recomendado em versões novas
    name = 'djangosige.apps.vendas'  # <<< use o caminho completo do pacote
    label = 'vendas'  # opcional; mantém o rótulo curto no banco/admin 
