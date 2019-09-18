import csv
from pathlib import Path

TRANSACTIONS = {}
PRODUCTS = {}
DATA_PATH = Path.cwd() / 'data'


class Transaction:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.product_id = kwargs.get('product_id')
        self.amount = float(kwargs.get('amount', 0))
        self.date = kwargs.get('date')


class Product:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.city = kwargs.get('city')


def tx_loader():
    path = Path.joinpath(DATA_PATH, 'transactions.csv')

    with open(path, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            primary_key = row[0]
            TRANSACTIONS[primary_key] = map_tx_row(row)


def products_loader():
    path = Path.joinpath(DATA_PATH, 'products.csv')

    with open(path, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            primary_key = row[0]
            PRODUCTS[primary_key] = map_product_row(row)


def map_tx_row(row):
    attrs = {
        'id': row[0],
        'product_id': row[1],
        'amount': row[2],
        'date': row[3]
    }

    return Transaction(**attrs)


def map_product_row(row):
    attrs = {
        'id': row[0],
        'name': row[1],
        'city': row[2]
    }

    return Product(**attrs)
