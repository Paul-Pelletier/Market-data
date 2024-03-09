import requests
import csv
from io import StringIO
from MarketDataDumper import TickerDataBase

api_key = "EKZRGALCGSWPSD61"
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
with open('Real GDP.json') as f:
    json_data = json.load(f)
df = pd.DataFrame(json_data["data"])
df['date'] = pd.to_datetime(df["date"])
df['value'] = pd.to_numeric(df['value'], errors = "coerce")
dataFrame = TickerDataBase().TransformJsonToPandasDataFrame("Real GDP")
dataFrame.to_csv("Real GDP.csv", sep = ";", index = False, header = True)
print(df['value'][1]+df['value'][2])