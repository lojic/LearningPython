import re
import pandas as pd

def solve():
    customers   = pd.read_csv('noahs-customers.csv')
    order_items = pd.read_csv('noahs-orders_items.csv')
    orders      = pd.read_csv('noahs-orders.csv')
    products    = pd.read_csv('noahs-products.csv')

    collectibles = products[products['sku'].str.startswith('COL')]
    items        = order_items.merge(collectibles).merge(orders)
    grouped      = items[['customerid','sku']].drop_duplicates().groupby('customerid').count()
    customer_id  = grouped[grouped['sku'] == grouped['sku'].max()].reset_index().iloc[0]['customerid']

    return customers[customers['customerid'] == customer_id].iloc[0]['phone']

# ---------------------------------------------------------------------------------------------

assert solve() == '212-547-3518'
