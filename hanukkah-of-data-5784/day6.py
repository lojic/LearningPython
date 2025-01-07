import pandas as pd

customers   = pd.read_csv('noahs-customers.csv')
orders      = pd.read_csv('noahs-orders.csv')
order_items = pd.read_csv('noahs-orders_items.csv')
products    = pd.read_csv('noahs-products.csv')
data        = customers.merge(orders).merge(order_items).merge(products)

below_cost = data['unit_price'] < data['wholesale_cost']
grouped    = data[below_cost][['customerid','phone','unit_price']].groupby(['customerid', 'phone']).count()

assert grouped[grouped['unit_price'] == grouped['unit_price'].max()].reset_index().iloc[0]['phone'] == '585-838-9161'
