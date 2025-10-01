# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import inlineformset_factory

from djangosige.apps.ordens_servico.models import OSItem, OrdemServico, ServicoCatalogo, OSStatus

class ServicoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServicoForm, self).__init__(*args, **kwargs)

        self.fields['desconto'].localize = True
        self.fields['desconto'].initial = '0.00'
    
    class Meta:
         fields = ('numero','cliente','responsavel','tecnico_exec',
                   'observacoes','tipo_desconto','desconto')
         
         widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'responsavel': forms.Select(attrs={'class': 'form-control'}),
            'tecnico_exec': forms.Select(attrs={'class': 'form-control'}),
            'observacoes': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_desconto': forms.Select(attrs={'class': 'form-control'}),
            'desconto': forms.TextInput(attrs={'class': 'form-control decimal-mask-four'}),
         }
         labels = {
            'numero': _('Número OS'),
            'cliente': _('Cliente'),
            'responsavel': _('Técnico Responsável'),
            'tecnico_exec': _('Técnico Executor'),
            'observacoes': _('Observações'),
            'tipo_desconto': _('Tipo de desconto'),
            'desconto': _('Desconto (% ou R$)'),
         }

class OrdemServicoForm(ServicoForm):

    class Meta(ServicoForm.Meta):
        model = OrdemServico
        fields = ServicoForm.Meta.fields
        widgets = ServicoForm.Meta.widgets
        labels = ServicoForm.Meta.labels