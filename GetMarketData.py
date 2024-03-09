import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
tickerSymbol = '^GSPC'


# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2024-1-1')  # Example: Get data from 2010 to 2023
tickerDf.to_csv('spxMarketData.csv', index=False)
# See your data
print(tickerDf)
plt.plot(tickerDf)
plt.show()