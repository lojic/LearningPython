import pandas as pd
import re

def solve():
    customers   = pd.read_csv('noahs-customers.csv')
    order_items = pd.read_csv('noahs-orders_items.csv')
    orders      = pd.read_csv('noahs-orders.csv')
    products    = pd.read_csv('noahs-products.csv')

    # Get the Bargain Hunter information from the previous day
    bargain_hunter = customers[customers['phone'] == '585-838-9161']
    bargain_hunter_id = bargain_hunter.iloc[0]['customerid']

    # Get products that have a color
    col_products = products[products['sku'].str.startswith('COL')]

    # Get orders for the Bargain Hunter where:
    # 1. SKU indicates color
    # 2. ordered and shipped timestamps are equal i.e. in stock and in person
    bargain_orders = pd.merge(col_products, order_items). \
        merge(orders). \
        merge(bargain_hunter).query('ordered == shipped')[['desc','ordered']].values.tolist()

    # Loop over the Bargain Hunter's orders
    for orig_desc, ordered in bargain_orders:
        # Strip off the color portion of the product descriptions, so we can compare
        desc = re.sub(r' \([a-z]+\)', '', orig_desc)

        # Date plus hour of checkout e.g. "2024-04-01 12"
        ts = ordered[:13]

        # Get order items for similar products e.g. "Noah's Poster"
        prods = products[products['desc'].str.startswith(desc)].merge(order_items).merge(orders)

        # Get order items in the same hour as the Bargain Hunter's
        # NOTE: this wouldn't work if the two times were very close to the hours!
        items = prods[prods['ordered'].str.startswith(ts)][['customerid','desc']].values.tolist()

        # Restrict to different colored products
        custids = [ custid for custid, other_desc in items if other_desc != orig_desc ]

        # If we have only one, then we've found our person
        if len(custids) == 1:
            return customers[customers['customerid'] == custids[0]].iloc[0]['phone']

# ---------------------------------------------------------------------------------------------

assert solve() == '838-335-7157'
