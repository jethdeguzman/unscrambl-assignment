from services.db import PRODUCTS


def get_product(id):
    return PRODUCTS.get(id)
