from advent import Counter
import pandas as pd

order_items = pd.merge(pd.read_csv('noahs-orders.csv'),
                       pd.merge(pd.read_csv('noahs-orders_items.csv'),
                                pd.read_csv('noahs-products.csv')))

sale_items = order_items[order_items['unit_price'] < order_items['wholesale_cost']]
customers = pd.read_csv('noahs-customers.csv')

c = Counter()

for index, row in sale_items.iterrows():
    c[row['customerid']] += 1

assert customers[customers['customerid'] == c.most_common()[0][0]].iloc[0]['phone'] == '585-838-9161'
