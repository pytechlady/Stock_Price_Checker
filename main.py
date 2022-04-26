import requests
import csv


api_token = 'c9j4j7iad3iblk5allq0'
most_percentage_points_arr = []

# Endpoints for all FAANG company
apple_url = 'https://finnhub.io//api/v1/quote?symbol=AAPL'
google_url = 'https://finnhub.io//api/v1/quote?symbol=GOOGL'
amazon_url = 'https://finnhub.io//api/v1/quote?symbol=AMZN'
netflix_url = 'https://finnhub.io//api/v1/quote?symbol=NFLX'
facebook_url = 'https://finnhub.io//api/v1/quote?symbol=META'

# Query the url using GET request to get all the stock information
apple_response = requests.get(apple_url, headers={'X-Finnhub-Token': '{key}'.format(key=api_token)})
google_response = requests.get(google_url, headers={'X-Finnhub-Token': '{key}'.format(key=api_token)})
amazon_response = requests.get(amazon_url, headers={'X-Finnhub-Token': '{key}'.format(key=api_token)})
netflix_response = requests.get(netflix_url, headers={'X-Finnhub-Token': '{key}'.format(key=api_token)})
facebook_response = requests.get(facebook_url, headers={'X-Finnhub-Token': '{key}'.format(key=api_token)})

# Convert to JSON object for accessibility
apple_data = apple_response.json()
google_data = google_response.json()
amazon_data = amazon_response.json()
netflix_data = netflix_response.json()
facebook_data = facebook_response.json()

# Loop through each object to get a specific data
apple_list = [value for (key, value) in apple_data.items()]
google_list = [val for (k, val) in google_data.items()]
amazon_list = [v for (x, v) in amazon_data.items()]
netflix_list = [a for (b, a) in netflix_data.items()]
facebook_list = [i for (y, i) in facebook_data.items()]

# Print the Latest stock price for all the companies
print('Latest Apple stock = ' + str(apple_list[0]))
print('Latest Google stock = ' + str(google_list[0]))
print('Latest Amazon stock = ' + str(amazon_list[0]))
print('Latest Netflix stock = ' + str(netflix_list[0]))
print('Latest Facebook stock = ' + str(facebook_list[0]))


# Find the company that has the the stock that moved the most percentage points from yesterday.
apple_difference = apple_list[2]
most_percentage_points_arr.append(apple_difference)

google_difference = google_list[2]
most_percentage_points_arr.append(google_difference)

amazon_difference = amazon_list[2]
most_percentage_points_arr.append(amazon_difference)

netflix_difference = netflix_list[2]
most_percentage_points_arr.append(netflix_difference)

facebook_difference = facebook_list[2]
most_percentage_points_arr.append(facebook_difference)

print(most_percentage_points_arr)
most_volatile_stock = max(most_percentage_points_arr)
print(most_volatile_stock)

# Write the most_volatile_stock details in CSV file
header = ["stock_symbol", "percentage_change", "current_price", "last_close_price"]

with open('volatile.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(header)
    thewriter.writerow(['META', facebook_difference, facebook_list[0], facebook_list[6]])
