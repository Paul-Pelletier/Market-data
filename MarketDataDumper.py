import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class TickerDataBase:
    def __init__(self) -> None:
        self.Indices = {
            "S&P 500 Index": "^GSPC",
            "Dow Jones Industrial Average": "^DJI",
            "NASDAQ Composite Index": "^IXIC",
            "NYSE Composite Index": "^NYA",
            "Russell 2000 Index": "^RUT",
            "FTSE 100 Index": "^FTSE",
            "DAX Index (Germany)": "^GDAXI",
            "CAC 40 Index (France)": "^FCHI",
            "Nikkei 225 Index (Japan)": "^N225",
            "Hang Seng Index (Hong Kong)": "^HSI",
            "Shanghai Composite Index (China)": "000001.SS",
            "S&P_ASX 200 Index (Australia)": "^AXJO",
            "Bovespa Index (Brazil)": "^BVSP",
            "TSX Composite Index (Canada)": "^GSPTSE"
        }

        self.Commodities = {
            "Crude Oil (WTI)": "CL=F",
            "Crude Oil (Brent)": "BZ=F",
            "Natural Gas": "NG=F",
            "Gold": "GC=F",
            "Silver": "SI=F",
            "Copper": "HG=F",
            "Platinum": "PL=F",
            "Palladium": "PA=F",
            "Corn": "ZC=F",
            "Soybeans": "ZS=F",
            "Wheat": "ZW=F",
            "Cotton": "CT=F",
            "Sugar": "SB=F",
            "Coffee": "KC=F",
            "Cocoa": "CC=F"
        }

        self.BenchmarkGovernmentYields = {
            "United States": {
                "1-Year": "US1YT=RR",
                "2-Year": "US2YT=RR",
                "3-Year": "US3YT=RR",
                "5-Year": "US5YT=RR",
                "7-Year": "US7YT=RR",
                "10-Year": "US10YT=RR",
                "30-Year": "US30YT=RR"
            },
            "Germany": {
                "1-Year": "DE1YT=RR",
                "2-Year": "DE2YT=RR",
                "3-Year": "DE3YT=RR",
                "5-Year": "DE5YT=RR",
                "7-Year": "DE7YT=RR",
                "10-Year": "DE10YT=RR",
                "30-Year": "DE30YT=RR"
            },
            "United Kingdom": {
                "1-Year": "GB1YT=RR",
                "2-Year": "GB2YT=RR",
                "3-Year": "GB3YT=RR",
                "5-Year": "GB5YT=RR",
                "7-Year": "GB7YT=RR",
                "10-Year": "GB10YT=RR",
                "30-Year": "GB30YT=RR"
            },
            "France": {
                "1-Year": "FR1YT=RR",
                "2-Year": "FR2YT=RR",
                "3-Year": "FR3YT=RR",
                "5-Year": "FR5YT=RR",
                "7-Year": "FR7YT=RR",
                "10-Year": "FR10YT=RR",
                "30-Year": "FR30YT=RR"
            },
            "Italy": {
                "1-Year": "IT1YT=RR",
                "2-Year": "IT2YT=RR",
                "3-Year": "IT3YT=RR",
                "5-Year": "IT5YT=RR",
                "7-Year": "IT7YT=RR",
                "10-Year": "IT10YT=RR",
                "30-Year": "IT30YT=RR"
            },
            "Spain": {
                "1-Year": "ES1YT=RR",
                "2-Year": "ES2YT=RR",
                "3-Year": "ES3YT=RR",
                "5-Year": "ES5YT=RR",
                "7-Year": "ES7YT=RR",
                "10-Year": "ES10YT=RR",
                "30-Year": "ES30YT=RR"
            },
            "China": {
                "1-Year": "CN1YT=RR",
                "2-Year": "CN2YT=RR",
                "3-Year": "CN3YT=RR",
                "5-Year": "CN5YT=RR",
                "7-Year": "CN7YT=RR",
                "10-Year": "CN10YT=RR",
                "30-Year": "CN30YT=RR"
            },
            "Japan": {
                "1-Year": "JP1YT=RR",
                "2-Year": "JP2YT=RR",
                "3-Year": "JP3YT=RR",
                "5-Year": "JP5YT=RR",
                "7-Year": "JP7YT=RR",
                "10-Year": "JP10YT=RR",
                "30-Year": "JP30YT=RR"
            }
        }


Indices = TickerDataBase().Indices
for keys in Indices.keys():
    marketData = yf.Ticker(Indices[keys])
    dataFrame = marketData.history(period='1d', start='2010-1-1', end='2024-1-1')  # Example: Get data from 2010 to 2023)
    dataFrame.to_csv(f'{str(keys)}.csv', sep = ";", index = False)
