import requests
import csv
from io import StringIO
from MarketDataDumper import TickerDataBase

api_key = "EKZRGALCGSWPSD61"
"EKZRGALCGSWPSD61"
url = "https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=daily&maturity=3M&apikey=" + api_key
#dumper = TickerDataBase().RequestAndDumpData("Real GDP", url)
# def get_tickers(api_key):
#     economicData = TickerDataBase().EconomicIndicators["Treasury Yield"]
#     url = "https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=daily&maturity=3M&apikey=" + api_key
#     response = requests.get(url)
#     csvfile = StringIO(response.text)
#     reader = csv.reader(csvfile)
#     tickers = [row for row in reader]  # Adjust based on the CSV structure
#     with open('tickers.csv', 'w') as file:
#         file.write(response.text)
#     return tickers

# tickers = get_tickers(api_key)
# print(tickers)
import pandas as pd
import json
df = pd.read_csv("Real GDP.csv")
print(type(df.iloc[0][0]))