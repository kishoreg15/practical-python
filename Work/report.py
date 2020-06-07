import csv

def read_portfolio(filename):
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        
        #skip header
        next(rows)

        portfolio = []

        for row in rows:
            holding = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
            portfolio.append(holding)

    return portfolio

def read_prices(filename):
    with open(filename,'rt') as f:
        rows = csv.reader(f)

        prices = {}

        for row in rows:
            if(row):
                prices[row[0]] = float(row[1])

    return prices

def portfolio_value(portfolio,prices):
    original_value = 0.0
    current_value = 0.0
    for item in portfolio:
        original_value += item['shares']*item['price']
        if item['name'] in prices:
            current_value += item['shares'] * prices[item['name']]
        else:
            current_value += item['shares']*item['price']
    
    print('Original value:', original_value)
    print('Current value:', current_value)
    print('Gain/Loss:', current_value - original_value)
    return current_value - original_value
