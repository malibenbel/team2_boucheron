import yfinance as yf
import pandas as pd


def get_stock_data(ticker_symbol="KER.PA"):
    data = yf.download(ticker_symbol, period="5d", interval="1d")
    data = pd.DataFrame(data)
    return data
