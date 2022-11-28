from datetime import time


def read_archive(data):
    transactions = data.read().decode("utf-8").split("\n")
    list_transactions = []
    for transaction in transactions:
        list_transactions += [{"tipo": int(transaction[0]),
                               "data": transaction[1:9],
                               "valor": int(transaction[10:20]) / 100,
                               "cpf":transaction[20:31],
                               "cartao":transaction[31:42],
                               "hora":time(int(transaction[42:44]), int(transaction[44:46]), int(transaction[46:48])).strftime("%H:%M:%S"),
                               "nome_representante":transaction[48:62],
                               "nome_fantasia":transaction[62:83]}]
    return list_transactions
