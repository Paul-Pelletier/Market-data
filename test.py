import requests
import csv
from io import StringIO
import pandas as pd
import json
from MarketDataDumper import MarketDataRequestAndDump

api_key = "EKZRGALCGSWPSD61"
"EKZRGALCGSWPSD61"

a = MarketDataRequestAndDump(api_key)
b = a.GetEconomicIndicatorsData()