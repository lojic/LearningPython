import pandas as pd
import re
from datetime import datetime, timedelta

def solve():
    customers   = pd.read_csv('noahs-customers.csv')
    orders      = pd.read_csv('noahs-orders.csv', parse_dates=['ordered'])
    order_items = pd.read_csv('noahs-orders_items.csv')
    products    = pd.read_csv('noahs-products.csv')
    data        = customers.merge(orders).merge(order_items).merge(products)

    is_bargain_hunter = data['phone'] == '585-838-9161'
    has_color         = data['sku'].str.startswith('COL')
    is_in_stock       = data['ordered'] == data['shipped']

    bargain_orders = data[has_color & is_bargain_hunter & is_in_stock][['desc','ordered']]

    # Loop over the Bargain Hunter's orders
    for _, row in bargain_orders.iterrows():
        desc    = row['desc']
        ordered = row['ordered']

        # Strip off the color portion of the product descriptions, so we can compare w/o color
        desc_prefix = re.sub(r' \([a-z]+\)', '', desc)

        # Restrict to w/in 10 minutes of Bargain Hunter's purchase
        delta        = timedelta(minutes=10)
        similar_time = (data['ordered'] >= (ordered - delta)) & (data['ordered'] <= (ordered + delta))

        # Restrict to order items for similar products e.g. "Noah's Poster"
        similar_item = data['desc'].str.startswith(desc_prefix)

        items = data[similar_time & similar_item][['customerid','desc']].values.tolist()

        # Restrict to different colored products
        custids = [ custid for custid, other_desc in items if other_desc != desc ]

        # If we have only one, then we've found our person
        if len(custids) == 1:
            return customers[customers['customerid'] == custids[0]].iloc[0]['phone']

# ---------------------------------------------------------------------------------------------

assert solve() == '838-335-7157'
