import pandas as pd

def solve():
    customers   = pd.read_csv('noahs-customers.csv')
    orders      = pd.read_csv('noahs-orders.csv')
    order_items = pd.read_csv('noahs-orders_items.csv')
    products    = pd.read_csv('noahs-products.csv')
    data        = customers.merge(orders).merge(order_items).merge(products)

    senior = data['desc'].str.contains('Senior Cat Food')
    qty    = data['qty'] == 10

    return data[senior & qty]['phone'].drop_duplicates().iloc[0]

# ---------------------------------------------------------------------------------------------

assert solve() == '631-507-6048'
