# -*- coding: utf-8 -*-

from django.db import models
from ..choices import NFSeStatus
from .servicos import OrdemServico

class NFSeConfiguracao(models.Model):
    # multi-município: cada empresa pode ter 1+ configs
    empresa = models.ForeignKey("cadastro.Empresa", on_delete=models.PROTECT)
    municipio_codigo_ibge = models.CharField(max_length=7)
    provedor = models.CharField(max_length=50)  # "ginfes", "betha", "abrasf_v203", "nfse_nacional", etc.
    # credenciais/tokens/certificados conforme provedor
    usuario = models.CharField(max_length=100, blank=True)
    senha = models.CharField(max_length=200, blank=True)
    token = models.CharField(max_length=500, blank=True)
    certificado_pfx = models.FileField(upload_to="os/certs/", blank=True, null=True)
    certificado_senha = models.CharField(max_length=200, blank=True)
    ambiente = models.CharField(max_length=10, default="homolog")  # "homolog" ou "prod"

    ativo = models.BooleanField(default=True)

class NFSe(models.Model):
    os = models.OneToOneField(OrdemServico, on_delete=models.PROTECT, related_name="nfse")
    status = models.CharField(max_length=20, choices=NFSeStatus.choices, default=NFSeStatus.PENDENTE)
    numero_nfse = models.CharField(max_length=30, blank=True)
    numero_rps = models.CharField(max_length=30, blank=True)
    serie_rps = models.CharField(max_length=10, blank=True)
    data_emissao = models.DateTimeField(null=True, blank=True)
    xml_autorizado = models.FileField(upload_to="nfse/xml/%Y/%m/", blank=True, null=True)
    protocolo = models.CharField(max_length=60, blank=True)
    mensagem_retorno = models.TextField(blank=True)
