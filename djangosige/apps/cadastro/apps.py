from __future__ import unicode_literals

from django.apps import AppConfig


class CadastroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # opcional, mas recomendado em versões novas
    name = 'djangosige.apps.cadastro'  # <<< use o caminho completo do pacote
    label = 'cadastro'  # opcional; mantém o rótulo curto no banco/admin  

