from django.db.models import TextChoices

class OSStatus(TextChoices):
    RASCUNHO = "rascunho", "Rascunho"
    ABERTA   = "aberta", "Aberta"
    EM_EXEC  = "em_exec", "Em execução"
    CONCLUIDA= "concluida", "Concluída"
    FATURADA = "faturada", "Faturada"
    CANCELADA= "cancelada", "Cancelada"

class NFSeStatus(TextChoices):
    PENDENTE   = "pendente", "Pendente"
    AUTORIZADA = "autorizada", "Autorizada"
    REJEITADA  = "rejeitada", "Rejeitada"
    CANCELADA  = "cancelada", "Cancelada"

class TipoDescontoOS_Escolhas(TextChoices):
    VALOR       = "valor", "Valor"
    PERCENTUAL  =  "percentual", "Percentual"