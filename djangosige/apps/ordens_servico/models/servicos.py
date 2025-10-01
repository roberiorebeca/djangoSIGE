# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils import timezone
from ..choices import OSStatus, TipoDescontoOS_Escolhas

class ServicoCatalogo(models.Model):
    codigo = models.CharField(max_length=30, unique=True)
    descricao = models.CharField(max_length=255)
    # ISS: código LC 116 / CNAE / código municipal (ajuste conforme município)
    codigo_servico_municipal = models.CharField(max_length=30, blank=True)
    aliquota_iss = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # % ex.: 5.00
    valor_unitario = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

class OrdemServico(models.Model):
    numero = models.CharField(max_length=30, unique=True)
    cliente = models.ForeignKey("cadastro.Cliente", on_delete=models.PROTECT)  # aproveite o app existente
    data_abertura = models.DateTimeField(default=timezone.now)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="os_responsavel")
    tecnico_exec = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="os_tecnico")
    status = models.CharField(max_length=20, choices=OSStatus.choices, default=OSStatus.RASCUNHO)
    observacoes = models.TextField(blank=True)

    # totais
    subtotal = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    tipo_desconto = models.CharField(max_length=1, choices=TipoDescontoOS_Escolhas, null=True, blank=True)
    desconto = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    total = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    # trava após faturar
    locked = models.BooleanField(default=False)

    class Meta:
        ordering = ["-data_abertura"]

    def __str__(self):
        return f"OS #{self.numero} - {self.cliente}"

class OSItem(models.Model):
    os = models.ForeignKey(OrdemServico, on_delete=models.CASCADE, related_name="itens")
    servico = models.ForeignKey(ServicoCatalogo, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=255, blank=True)  # override opcional
    quantidade = models.DecimalField(max_digits=12, decimal_places=2, default=1)
    valor_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if not self.valor_unitario:
            self.valor_unitario = self.servico.valor_unitario
        self.total = (self.quantidade or 0) * (self.valor_unitario or 0)
        super().save(*args, **kwargs)

class OSAnexo(models.Model):
    os = models.ForeignKey(OrdemServico, on_delete=models.CASCADE, related_name="anexos")
    arquivo = models.FileField(upload_to="os/anexos/%Y/%m/")
    descricao = models.CharField(max_length=255, blank=True)
