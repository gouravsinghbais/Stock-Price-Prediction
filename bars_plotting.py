import plotly.plotly as py
import pandas as pd
import csv
import plotly.graph_objs as go
import plotly
import numpy as np
py.sign_in('GouravSinghBais','noa01K08GYJ3hWoowIE7')
plotly.tools.set_credentials_file(username='GouravSinghBais', api_key='noa01K08GYJ3hWoowIE7')
dates = []
prices_open = []
price_close = []
high_price = []
low_price = []
with open('aapl.csv','r') as csv_file:
    CsvFileReader = csv.reader(csv_file)
    next(CsvFileReader)
    for row in CsvFileReader:
        dates.append(row[0])
        prices_open.append(float(row[1]))
        high_price.append(float(row[2]))
        low_price.append(float(row[3]))
        price_close.append(float(row[5]))

print(dates)
print(price_close)
print(prices_open)
print(high_price)
print(low_price)

trace = go.Candlestick(x = dates,
                       open = prices_open,
                       high = high_price,
                       low = low_price,
                       close = price_close)
data = [trace]
py.plot(data)