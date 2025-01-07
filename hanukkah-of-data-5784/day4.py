from advent import Counter
import pandas as pd

def solve():
    customers   = pd.read_csv('noahs-customers.csv')
    orders      = pd.read_csv('noahs-orders.csv', parse_dates=['shipped'])
    order_items = pd.read_csv('noahs-orders_items.csv')
    data        = orders.merge(order_items)
    
    bakery_orders = (data[data['sku'].str.startswith('BKY')][['orderid','customerid','ordered','shipped']].
                     drop_duplicates().
                     sort_values('shipped'))

    prev_date      = None
    first_customer = Counter()

    for index, row in bakery_orders.iterrows():
        shipped_date = row['shipped'].date()
        
        if shipped_date != prev_date:
            first_customer[row['customerid']] += 1
            prev_date = shipped_date

    return customers[customers['customerid'] == first_customer.most_common()[0][0]].iloc[0]['phone']

# ---------------------------------------------------------------------------------------------

assert solve() == '607-231-3605'
