# -*- coding: utf-8 -*-
from django.db import migrations
import json
import os

def load_fixture(apps, schema_editor):
    """
    Carrega o fixture 'estoque_initial_data.json' usando os modelos históricos
    (fornecidos por `apps`) sem depender de APIs privadas do Django.
    """
    # caminho padrão do fixture dentro do app: apps/estoque/fixtures/estoque_initial_data.json
    here = os.path.dirname(__file__)
    fixture_path = os.path.normpath(
        os.path.join(here, '..', 'fixtures', 'estoque_initial_data.json')
    )

    if not os.path.exists(fixture_path):
        # Se o arquivo não existir, não falhe a migração.
        return

    with open(fixture_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Espera formato padrão de fixture do Django:
    # [{"model": "app_label.ModelName", "pk": 1, "fields": {...}}, ...]
    for obj in data:
        model_label = obj.get('model')
        if not model_label:
            continue

        # model_label esperado como "app_label.ModelName"
        try:
            app_label, model_name = model_label.split('.')
        except ValueError:
            parts = model_label.split('.')
            app_label, model_name = parts[0], parts[-1]

        Model = apps.get_model(app_label, model_name)
        fields = obj.get('fields', {})
        pk = obj.get('pk')

        # Se o fixture usa natural keys ou FKs por string, garanta que os
        # nomes dos campos em `fields` estão alinhados com o schema atual
        # histórico. Se necessário, faça mapeamentos aqui.

        if pk is not None:
            # Evita duplicidade em reexecuções
            if not Model.objects.filter(pk=pk).exists():
                Model.objects.create(pk=pk, **fields)
        else:
            Model.objects.create(**fields)

def unload_fixture(apps, schema_editor):
    """
    (Opcional) Reverso: implemente deletes se necessário.
    Mantemos como NOOP para não remover dados em reversões.
    """
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
