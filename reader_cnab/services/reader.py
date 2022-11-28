import ipdb


def read_archive(data):
    transactions = data.read().decode("utf-8").split("\n")
    list_transactions = []
    for transaction in transactions:
        list_transactions += [{"tipo": transaction[0],
                               "data": transaction[1:8],
                               "valor": transaction[10:20],
                               "CPF":transaction[20:31],
                               "cartao":transaction[31:42],
                               "hora":transaction[42:48],
                               "nome_representante":transaction[48:62],
                               "nome_fantasia":transaction[62:83]}]
    return list_transactions
