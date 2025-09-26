from __future__ import unicode_literals

from django.apps import AppConfig


class FinanceiroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # opcional, mas recomendado em versões novas
    name = 'djangosige.apps.financeiro'  # <<< use o caminho completo do pacote
    label = 'financeiro'  # opcional; mantém o rótulo curto no banco/admin  
