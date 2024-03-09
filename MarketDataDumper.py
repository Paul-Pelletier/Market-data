import requests
import csv
from io import StringIO
import json
import pandas as pd

class TickerDataBase:
    def __init__(self) -> None:
        self.apiKey = "EKZRGALCGSWPSD61"
        self.StockMarket = None
        self.CommoditiesMarket = None
        self.CryptoMarket = None
        self.EconomicIndicators = {
                                    "Real GDP": {"function": "REAL_GDP", "interval": "quarterly"},
                                    "Real GDP per Capita": {"function": "GDP_PER_CAPITA"},
                                    "Treasury Yield": {"function": "TREASURY_YIELD", "interval": "daily", "maturity": ["3month", "2year", "5year", "7year", "10year", "30year"]},
                                    "Federal Funds Rate": {"function": "FEDERAL_FUNDS_RATE", "interval": "daily"},
                                    "CPI": {"function": "CPI", "interval": "monthly"},
                                    "Inflation": {"function": "INFLATION", "interval": "monthly"},
                                    "Retail Sales": {"function": "RETAIL_SALES", "interval": "monthly"},
                                    "Durable Goods Orders": {"function": "DURABLES", "interval": "monthly"},
                                    "Unemployment Rate": {"function": "UNEMPLOYMENT", "interval": "monthly"},
                                    "Nonfarm Payroll": {"function": "NONFARM_PAYROLL", "interval": "monthly"}}
    
    def RequestAndDumpData(self : object, EconomicIndicator : str, url : str)->str:
        response = requests.get(url)
        data = json.loads(response.text)
        with open(f"{EconomicIndicator}.json", 'w') as json_file:
            json.dump(data, json_file, indent=4)
        dataFrame = self.TransformJsonToPandasDataFrame(EconomicIndicator)
        dataFrame.to_csv(f"{EconomicIndicator}.csv", sep = ";", index = False, header = True)
        print("Done")
        return "Done"
    
    def TransformJsonToPandasDataFrame(self : object, EconomicIndicator : str) -> pd.DataFrame:
        with open(f'{EconomicIndicator}.json') as file:
            json_data = json.load(file)
        dataFrame = pd.DataFrame(json_data["data"])
        dataFrame['date'] = pd.to_datetime(dataFrame["date"])
        dataFrame['value'] = pd.to_numeric(dataFrame['value'], errors = "coerce")
        return dataFrame
    
    def GetEconomicIndicatorsData(self) -> str:
        for key in self.EconomicIndicators.keys():
            economicIndicator = self.EconomicIndicators[key]
            if key == "Treasury Yield":
                for maturity in self.self.EconomicIndicators[key]["maturity"]:
                    url = f"https://www.alphavantage.co/query?function={key}&interval={"daily"}&maturity={maturity}&apikey=" + self.apiKey
            else:
                url = f"https://www.alphavantage.co/query?function={key}&interval={"daily"}&&apikey=" + self.apiKey
            self.RequestAndDumpData(economicIndicator, url)

            
