import json
import threading
from api import transactions, products, summary
from flask import Flask, abort
from services.db import tx_loader, products_loader

FIVE_MINUTES_TO_SECONDS = 300


def load_data():
    products_loader()
    tx_loader()
    threading.Timer(FIVE_MINUTES_TO_SECONDS, load_data).start()


load_data()

app = Flask(__name__)


@app.route('/assignment/transaction/<id>')
def get_transaction(id):
    tx = transactions.get_transaction(id)

    if tx:
        product = products.get_product(tx.product_id)

        return {
            "transactionId": tx.id,
            "productName": product.name,
            "transactionAmount": tx.amount,
            "transactionDatetime": tx.date
        }
    else:
        abort(404)


@app.route('/assignment/transactionSummaryByProducts/<days>')
def tx_by_product(days):
    response = summary.tx_by_product(days)
    return json.dumps(response)


@app.route('/assignment/transactionSummaryByCity/<days>')
def tx_by_city(days):
    response = summary.tx_by_city(days)
    return json.dumps(response)
