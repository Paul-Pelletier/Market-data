import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

AlphaVantageAPIKey = "HF8YN14QRF5L1GGQ"

class TickerDataBase:
    def __init__(self) -> None:
        self.StockMarket = None
        self.CommoditiesMarket = None
        self.CryptoMarket = None
        self.EconomicIndicators = None
