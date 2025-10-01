from django.utils import timezone
from ..choices import OSStatus

def pode_concluir(os):
    return os.status in {OSStatus.ABERTA, OSStatus.EM_EXEC} and os.itens.exists() and os.total > 0

def concluir_os(os):
    if not pode_concluir(os):
        raise ValueError("OS não pode ser concluída. Verifique itens e status.")
    os.status = OSStatus.CONCLUIDA
    os.data_conclusao = timezone.now()
    os.save()

def faturar_os(os):
    if os.status != OSStatus.CONCLUIDA:
        raise ValueError("Somente OS concluída pode ser faturada.")
    os.status = OSStatus.FATURADA
    os.locked = True
    os.save()
