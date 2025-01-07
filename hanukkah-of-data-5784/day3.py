import pandas as pd

def solve():
    rabbit_years = (1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023)

    customers          = pd.read_csv('noahs-customers.csv', parse_dates=['birthdate'])
    contractor_address = customers[customers['phone'] == '332-274-4185'].iloc[0]['citystatezip']

    bd          = customers['birthdate']
    birth_month = bd.dt.month
    birth_day   = bd.dt.day
    birth_year  = bd.dt.year

    is_cancer       = ((birth_month == 6) & (birth_day >= 21)) | ((birth_month == 7) & (birth_day <= 22))
    is_rabbit_year  = birth_year.isin(rabbit_years)
    is_neighborhood = customers['citystatezip'] == contractor_address

    return customers[is_cancer & is_rabbit_year & is_neighborhood].iloc[0]['phone']

# -------------------------------------------------------------------------------------

assert solve() == '917-288-9635'
