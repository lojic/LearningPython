import pandas as pd

def solve():
    products    = pd.read_csv('noahs-products.csv')
    cleaner_sku = products['sku'][products['desc'].str.contains('cleaner', case=False)].iloc[0]
    coffee_sku  = products['sku'][products['desc'].str.contains('coffee', case=False)].iloc[0]

    order_items           = pd.read_csv('noahs-orders_items.csv')
    orderids_with_cleaner = set(order_items['orderid'][order_items['sku'] == cleaner_sku].tolist())
    orderids_with_coffee  = set(order_items['orderid'][order_items['sku'] == coffee_sku].tolist())
    common_orders         = orderids_with_coffee & orderids_with_cleaner

    orders      = pd.read_csv('noahs-orders.csv')
    customer_id = orders['customerid'][orders['orderid'] == common_orders.pop()].iloc[0]

    customers = pd.read_csv('noahs-customers.csv')

    return customers['phone'][customers['customerid'] == customer_id].iloc[0]

# ---------------------------------------------------------------------------------------------

assert solve() == '332-274-4185'
