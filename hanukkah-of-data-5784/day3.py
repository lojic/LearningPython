import pandas as pd

# https://en.wikipedia.org/wiki/Rabbit_(zodiac)
rabbit_years = [ ('1903-01-29', '1904-02-15'), ('1915-02-14', '1916-02-03'),
                 ('1927-02-02', '1928-01-22'), ('1939-02-19', '1940-02-07'),
                 ('1951-02-06', '1952-01-26'), ('1963-01-25', '1964-02-12'),
                 ('1975-02-11', '1976-01-30'), ('1987-01-29', '1988-02-16'),
                 ('1999-02-16', '2000-02-04'), ('2011-02-03', '2012-01-22'),
                 ('2023-01-22', '2024-02-09') ]

customers          = pd.read_csv('noahs-customers.csv')
contractor_address = customers[customers['phone'] == '332-274-4185'].iloc[0]['citystatezip']

is_rabbit   = lambda row: any(d1 <= row['birthdate'] <= d2 for d1, d2 in rabbit_years)
is_cancer   = lambda row: '06-21' <= row['birthdate'][5:] <= '07-22'
is_neighbor = lambda row: contractor_address == row['citystatezip']
predicate   = lambda row: is_rabbit(row) and is_cancer(row) and is_neighbor(row)

def solve():
    return customers[customers.apply(predicate, axis=1)].iloc[0]['phone']

# -------------------------------------------------------------------------------------

assert solve() == '917-288-9635'
