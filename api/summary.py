from datetime import datetime, timedelta
from services.db import TRANSACTIONS, PRODUCTS
from .products import get_product


def tx_by_product(days):
    summary = {}
    txs = filter_txs_by_days(days)

    for tx in txs:
        product = get_product(tx.product_id)
        product_summary = summary.get(tx.product_id)

        if product_summary:
            total_amount = product_summary['totalAmount'] + tx.amount
            summary[tx.product_id]['totalAmount'] = total_amount
        else:
            summary[tx.product_id] = {
                'productName': product.name,
                'totalAmount': tx.amount
            }

    return list(summary.values())


def tx_by_city(days):
    summary = {}
    txs = filter_txs_by_days(days)

    for tx in txs:
        product = get_product(tx.product_id)
        city_summary = summary.get(product.city)

        if city_summary:
            total_amount = city_summary['totalAmount'] + tx.amount
            summary[product.city]['totalAmount'] = total_amount
        else:
            summary[product.city] = {
                'cityName': product.city,
                'totalAmount': tx.amount
            }

    return list(summary.values())


def filter_txs_by_days(days):
    filtered_txs = []
    today = datetime.now()
    filter_date = today - timedelta(days=int(days))

    for tx in TRANSACTIONS.values():
        tx_date = datetime.strptime(tx.date, '%Y-%m-%d %H:%M:%S')

        if tx_date >= filter_date:
            filtered_txs.append(tx)

    return filtered_txs
