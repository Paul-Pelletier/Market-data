import requests
import csv
from io import StringIO
import json
import pandas as pd

class MarketDataRequestAndDump:
    #Gets data from AlphaVantage
    def __init__(self : object, apiKey : str) -> None:
        self.apiKey = apiKey
        self.StockMarket = None
        self.CommoditiesMarket = None
        self.CryptoMarket = None
        self.EconomicIndicator = None
        self.EconomicIndicators = {
                                    "Real GDP": {"function": "REAL_GDP", "interval": "quarterly"},
                                    "Real GDP per Capita": {"function": "REAL_GDP_PER_CAPITA"},
                                    "Treasury Yield_3month": {"function": "TREASURY_YIELD", "interval": "daily", "maturity": "3month"},
                                    "Treasury Yield_2year": {"function": "TREASURY_YIELD", "interval": "daily", "maturity": "2year"},
                                    "Treasury Yield_5year": {"function": "TREASURY_YIELD", "interval": "daily", "maturity": "5year"},
                                    "Treasury Yield_7year": {"function": "TREASURY_YIELD", "interval": "daily", "maturity": "7year"},
                                    "Treasury Yield_10year": {"function": "TREASURY_YIELD", "interval": "daily", "maturity": "10year"},
                                    "Treasury Yield_30year": {"function": "TREASURY_YIELD", "interval": "daily", "maturity": "30year"},
                                    "Federal Funds Rate": {"function": "FEDERAL_FUNDS_RATE", "interval": "daily"},
                                    "CPI": {"function": "CPI", "interval": "monthly"},
                                    "Inflation": {"function": "INFLATION", "interval": "monthly"},
                                    "Retail Sales": {"function": "RETAIL_SALES", "interval": "monthly"},
                                    "Durable Goods Orders": {"function": "DURABLES", "interval": "monthly"},
                                    "Unemployment Rate": {"function": "UNEMPLOYMENT", "interval": "monthly"},
                                    "Nonfarm Payroll": {"function": "NONFARM_PAYROLL", "interval": "monthly"}}
    
    def RequestAndDumpEconomicIndicatorData(self : object, EconomicIndicator : str, url : str, maturity : str)->str:
        response = requests.get(url)
        data = json.loads(response.text)
        if EconomicIndicator == "TREASURY_YIELD":
            EconomicIndicator = EconomicIndicator + f"_{maturity}"
        with open(f"./EconomicIndicatorsData/{EconomicIndicator}.json", 'w') as json_file:
            json.dump(data, json_file, indent=4)
        dataFrame = self.TransformJsonToPandasDataFrame(EconomicIndicator)
        dataFrame.to_csv(f"./EconomicIndicatorsData/{EconomicIndicator}.csv", sep = ";", index = False, header = True)
        print(f"{EconomicIndicator} done")
    
    def TransformJsonToPandasDataFrame(self : object, EconomicIndicator : str) -> pd.DataFrame:
        with open(f'./EconomicIndicatorsData/{EconomicIndicator}.json') as file:
            json_data = json.load(file)
        dataFrame = pd.DataFrame(json_data["data"])
        dataFrame["date"] = pd.to_datetime(dataFrame["date"])
        dataFrame["value"] = pd.to_numeric(dataFrame["value"], errors = "coerce")
        return dataFrame
    
    def GetEconomicIndicatorsData(self : object) -> str:
        for key in self.EconomicIndicators.keys():
            economicIndicator = self.EconomicIndicators[key]["function"]
            maturity = ""
            if key[0:14] == "Treasury Yield":
                maturity = self.EconomicIndicators[key]["maturity"]
                url = f"https://www.alphavantage.co/query?function={economicIndicator}&interval={"daily"}&maturity={maturity}&apikey=" + self.apiKey
            else:
                url = f"https://www.alphavantage.co/query?function={economicIndicator}&interval={"daily"}&apikey=" + self.apiKey
            self.RequestAndDumpEconomicIndicatorData(economicIndicator, url, maturity)


    def GetListingStatus(self : object) -> csv:
        url = "https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=" + self.apiKey
        response = requests.get(url)
        csvfile = StringIO(response.text)
        reader = csv.reader(csvfile)
        tickers = [row for row in reader]  # Adjust based on the CSV structure
        with open("./StockMarketData/StockTickers.csv", 'w', newline='') as file:
            writer = csv.writer(file, delimiter = ";")
            for row in tickers:
                writer.writerow(row)
        return tickers
        
