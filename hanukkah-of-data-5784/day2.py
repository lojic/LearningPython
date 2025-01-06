import pandas as pd

def solve():
    products    = pd.read_csv('noahs-products.csv')
    cleaner_sku = products[products['desc'].str.contains('cleaner', case=False)].iloc[0]['sku']
    coffee_sku  = products[products['desc'].str.contains('coffee', case=False)].iloc[0]['sku']

    order_items           = pd.read_csv('noahs-orders_items.csv')
    orderids_with_cleaner = set(order_items[order_items['sku'] == cleaner_sku]['orderid'].tolist())
    orderids_with_coffee  = set(order_items[order_items['sku'] == coffee_sku]['orderid'].tolist())
    common_orders         = orderids_with_coffee & orderids_with_cleaner

    orders      = pd.read_csv('noahs-orders.csv')
    customer_id = orders[orders['orderid'] == common_orders.pop()].iloc[0]['customerid']

    customers = pd.read_csv('noahs-customers.csv')

    return customers[customers['customerid'] == customer_id].iloc[0]['phone']

# ---------------------------------------------------------------------------------------------

assert solve() == '332-274-4185'
