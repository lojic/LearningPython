import re
import pandas as pd

def solve():
    customers   = pd.read_csv('noahs-customers.csv')
    orders      = pd.read_csv('noahs-orders.csv')
    order_items = pd.read_csv('noahs-orders_items.csv')
    products    = pd.read_csv('noahs-products.csv')
    data        = customers.merge(orders).merge(order_items).merge(products)

    is_collectible = data['sku'].str.startswith('COL')

    grouped = (data[is_collectible][['customerid','sku','phone']].
               drop_duplicates().
               groupby(['customerid','phone']).
               count())

    return (grouped[grouped['sku'] == grouped['sku'].max()].
            reset_index().
            iloc[0]['phone'])

# ---------------------------------------------------------------------------------------------

assert solve() == '212-547-3518'
