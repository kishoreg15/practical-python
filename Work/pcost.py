# pcost.py
#
# Exercise 1.27
import sys
import csv

def portValue(filename):
    'Returns the total value of the portfolio'
    total = 0
    portfoliofile = filename
    #delimeter = ','

    f = open(portfoliofile,'rt')
    rows = csv.reader(f)

    #skip header
    next(rows)

    for row in rows:
        try:
            shares = int(row[1])
        except ValueError:
            print("Invalid shares value:", row[1])
            continue
        try:
            price = float(row[2])
        except ValueError:
            print("Invalid price value:", row[2])
            continue
        
        total += shares * price

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

value = portValue(filename)
print(value)