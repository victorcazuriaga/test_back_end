from reader_cnab.models import DataCnab, TypeTransaction


def create_transactions(transactions):
    for transaction in transactions:
        type = transaction.pop("tipo")
        type_data = TypeTransaction.objects.get(id=type)
        cnab_data = DataCnab.objects.create(
            **transaction, tipo_id=type_data.id)
        cnab_data.save()
