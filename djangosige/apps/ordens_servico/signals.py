from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models.servicos import OrdemServico, OSItem

def _recalcular_totais(os):
    subtotal = sum(i.total for i in os.itens.all())
    os.subtotal = subtotal
    os.total = max(subtotal - (os.desconto or 0), 0)
    os.save(update_fields=["subtotal","total"])

@receiver([post_save, post_delete], sender=OSItem)
def os_item_changed(sender, instance, **kwargs):
    _recalcular_totais(instance.os)
