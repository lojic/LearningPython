import pandas as pd

def solve():
    customers   = pd.read_csv('noahs-customers.csv')
    orders      = pd.read_csv('noahs-orders.csv')
    order_items = pd.read_csv('noahs-orders_items.csv')
    products    = pd.read_csv('noahs-products.csv')
    data        = customers.merge(orders).merge(order_items).merge(products)

    cleaner_order_ids = set(data[data['desc'].str.contains('cleaner', case=False)]['orderid'].drop_duplicates())
    coffee_order_ids  = set(data[data['desc'].str.contains('coffee', case=False)]['orderid'].drop_duplicates())
    common_orders     = coffee_order_ids & cleaner_order_ids

    return data[data['orderid'] == common_orders.pop()].iloc[0]['phone']

# ---------------------------------------------------------------------------------------------

assert solve() == '332-274-4185'
