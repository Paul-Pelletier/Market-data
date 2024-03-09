"""Launcher for fetching market data from AlphaVantage"""
from MarketDataDumper import MarketDataRequestAndDump

ApiKey = "IWGY89WST51M75RS"
MarketDataRequestAndDump(ApiKey).GetEconomicIndicatorsData()
