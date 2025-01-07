import pandas as pd

order_items = pd.merge(pd.read_csv('noahs-orders.csv'),
                       pd.merge(pd.read_csv('noahs-orders_items.csv'),
                                pd.read_csv('noahs-products.csv')))

sale_items  = order_items[order_items['unit_price'] < order_items['wholesale_cost']]
grouped     = sale_items[['customerid','unit_price']].groupby('customerid').count()
customer_id = grouped[grouped['unit_price'] == grouped['unit_price'].max()].reset_index().iloc[0]['customerid']
customers   = pd.read_csv('noahs-customers.csv')

assert customers[customers['customerid'] == customer_id].iloc[0]['phone'] == '585-838-9161'
