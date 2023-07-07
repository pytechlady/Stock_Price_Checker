import requests
import os
import csv
import matplotlib.pyplot as plt
import numpy as np


api_token = os.environ.get('API_KEY')


url_path = 'https://finnhub.io//api/v1/quote?symbol={symbol}'

# company code for all FAANG company
companies = ['AAPL', 'GOOGL', 'AMZN', 'NFLX', 'META']
stock_prices = []

# Query the url using GET request to get all the stock information
for company in companies:
    url = url_path.format(symbol=company)
    response = requests.get(url, headers={'X-Finnhub-Token': '{key}'.format(key=api_token)})
    data = response.json()
    data_list = [value for (key, value) in data.items()]
    stock_prices.append(data_list[0])

    
# Enter the stock information displayed in a bar chart
x = np.array(companies)
y = np.array(stock_prices)

plt.bar(x,y)
# plt.pie(y, labels = x)
plt.show()

# Write the stock information with the highest price to a csv file
with open('volatile.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Company", "Stock Price"])
    writer.writerow([x[np.argmax(y)], np.max(y)])

