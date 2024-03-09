import requests
import csv
from io import StringIO

api_key = "HF8YN14QRF5L1GGQ"

def get_tickers(api_key):
    url = "https://www.alphavantage.co/query?function=UNEMPLOYMENT&interval=weekly&apikey=" + api_key
    response = requests.get(url)
    csvfile = StringIO(response.text)
    reader = csv.reader(csvfile)
    tickers = [row for row in reader]  # Adjust based on the CSV structure
    with open('tickers.csv', 'w') as file:
        file.write(response.text)
    return tickers

tickers = get_tickers(api_key)
print(tickers)