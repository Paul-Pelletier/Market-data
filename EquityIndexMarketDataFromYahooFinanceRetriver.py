"""Module providing a database class and extracting market quotes from Yahoo Finance."""
import yfinance as yf

class TickerDataBase:
    """Class representing a major indices ticker data base"""
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

Indices = TickerDataBase().Indices
for name, ticker in Indices.items():
    marketData = yf.Ticker(ticker)
    dataFrame = marketData.history(period='1d',
                                   start='2010-1-1',
                                   end='2024-1-1')  # Example: Get data from 2010 to 2023)
    dataFrame.to_csv(f'{"./EquityIndexData/"+str(name)}.csv', sep = ";", index = False)
