import pandas as pd

def solve():
    # https://en.wikipedia.org/wiki/Rabbit_(zodiac)
    rabbit_years = [ ('1903-01-29', '1904-02-15'), ('1915-02-14', '1916-02-03'),
                     ('1927-02-02', '1928-01-22'), ('1939-02-19', '1940-02-07'),
                     ('1951-02-06', '1952-01-26'), ('1963-01-25', '1964-02-12'),
                     ('1975-02-11', '1976-01-30'), ('1987-01-29', '1988-02-16'),
                     ('1999-02-16', '2000-02-04'), ('2011-02-03', '2012-01-22'),
                     ('2023-01-22', '2024-02-09') ]

    is_rabbit = lambda birthdate: any(d1 <= birthdate <= d2 for d1, d2 in rabbit_years)
    is_cancer = lambda birthdate: '06-21' <= birthdate[5:] <= '07-22'

    customers          = pd.read_csv('noahs-customers.csv')
    contractor_address = customers['citystatezip'][customers['phone'] == '332-274-4185'].iloc[0]

    for index, row in customers[['phone','birthdate','citystatezip']].iterrows():
        birthdate = row['birthdate']
        address   = row['citystatezip']
        if is_rabbit(birthdate) and is_cancer(birthdate) and contractor_address == address:
            return row['phone']

# -------------------------------------------------------------------------------------

assert solve() == '917-288-9635'
