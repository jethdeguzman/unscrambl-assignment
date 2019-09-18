from services.db import TRANSACTIONS


def get_transaction(id):
    return TRANSACTIONS.get(id)
