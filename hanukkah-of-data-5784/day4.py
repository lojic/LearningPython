from advent import Counter
import pandas as pd

def solve():
    order_items   = pd.read_csv('noahs-orders_items.csv')
    bakery_items  = order_items[order_items['sku'].str.startswith('BKY')]['orderid']

    orders        = pd.read_csv('noahs-orders.csv')
    bakery_orders = pd.merge(orders, bakery_items)[['orderid','customerid','ordered','shipped']].sort_values('shipped')

    prev_date      = None
    first_customer = Counter()

    for index, row in bakery_orders.iterrows():
        shipped_date = str.split(row['shipped'])[0]

        if shipped_date != prev_date:
            first_customer[row['customerid']] += 1
            prev_date = shipped_date

    frequent_first_customer_id = first_customer.most_common()[0][0]
    customers                  = pd.read_csv('noahs-customers.csv')

    return customers[customers['customerid'] == frequent_first_customer_id].iloc[0]['phone']

# ---------------------------------------------------------------------------------------------

assert solve() == '607-231-3605'
