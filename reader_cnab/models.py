from django.db import models
import uuid
# Create your models here.
# migrations.RunSQL("INSERT INTO reader_cnab_typetransaction VALUES(1, 'DEBITO', 'ENTRADA'),(2, 'BOLETO', 'SAIDA'),(3, 'FINANCIAMENTE', 'SAIDA'),(4, 'CREDITO', 'ENTRADA'),(5, 'RECEBIMENTO_EMPRESTIMO', 'ENTRADA'),(6, 'VENDAS', 'ENTRADA'),(7, 'RECEBIMENTO_TED', 'ENTRADA'),(8, 'RECEBIMENTO_DOC', 'ENTRADA'),(9,'ALUGUEL','SAIDA')"),


class OperationsChoices(models.TextChoices):
    DEBITO = "DEBITO"
    BOLETO = "BOLETO"
    FINANCIAMENTO = "FINANCIAMENTE"
    CREDITO = "CREDITO"
    RECEBIMENTO_EMPRESTIMO = "RECEBIMENTO_EMPRESTIMO"
    VENDAS = "VENDAS"
    RECEBIMENTO_TED = "RECEBIMENTO_TED"
    RECEBIMENTO_DOC = "RECEBIMENTO_DOC"
    OTHER = "OTHER"


class TypeTransaction(models.Model):
    id = models.IntegerField(primary_key=True)
    operacao = models.CharField(
        max_length=24, choices=OperationsChoices.choices, default=OperationsChoices.OTHER)
    natureza = models.CharField(max_length=24)


class DataCnab(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False)
    tipo = models.ForeignKey(
        "TypeTransaction", on_delete=models.CASCADE, related_name='tipo_id')
    data = models.CharField(max_length=12)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.CharField(max_length=12)
    nome_representante = models.CharField(max_length=14)
    nome_fantasia = models.CharField(max_length=19)
