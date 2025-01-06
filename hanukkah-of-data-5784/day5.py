import pandas as pd

def solve():
    customers               = pd.read_csv('noahs-customers.csv')
    staten_island_customers = customers[customers['citystatezip'].str.startswith('Staten Island, NY')][['customerid','phone']]

    products     = pd.read_csv('noahs-products.csv')
    cat_products = products[products['desc'].str.contains('Senior Cat Food')]

    cat_order_items = pd.merge(pd.read_csv('noahs-orders_items.csv'), cat_products)
    cat_order_items = cat_order_items[cat_order_items['qty'] >= 10]

    cat_orders = pd.merge(pd.read_csv('noahs-orders.csv'), cat_order_items)

    candidates = pd.merge(staten_island_customers, cat_orders['customerid'].drop_duplicates())

    return candidates.iloc[0]['phone']

# ---------------------------------------------------------------------------------------------

assert solve() == '631-507-6048'
