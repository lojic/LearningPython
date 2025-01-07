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

    lunch_hour = lambda ts: '11' <= ts[11:13] <= '12'

    # Loop over the Bargain Hunter's orders
    for desc, ordered in bargain_orders:
        # Strip off the color portion of the product descriptions, so we can compare
        desc = re.sub(r' \([a-z]+\)', '', desc)

        # Date plus hour of checkout e.g. "2024-04-01 12"
        ts = ordered[:13]

        if lunch_hour(ts):
            # Get order items for similar products e.g. "Noah's Poster"
            prods = products[products['desc'].str.startswith(desc)].merge(order_items).merge(orders)

            # Get order items in the same hour as the Bargain Hunter's
            others = prods[prods['ordered'].str.startswith(ts)][['customerid','ordered']].values.tolist()

            # Restrict to "lunch hour"
            other_ids = [ custid for custid, ordered in others if lunch_hour(ordered) ]

            # If we have only two, then one is the Bargain Hunter, and the other is our person
            if len(other_ids) == 2:
                custid = [custid for custid in other_ids if custid != bargain_hunter_id][0]
                return customers[customers['customerid'] == custid].iloc[0]['phone']

# ---------------------------------------------------------------------------------------------

assert solve() == '838-335-7157'
