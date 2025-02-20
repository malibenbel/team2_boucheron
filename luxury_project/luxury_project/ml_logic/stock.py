import yfinance as yf
import pandas as pd


def get_stock_data(ticker_symbol="KER.PA"):
    data = yf.download(ticker_symbol, period="5y", interval="1d")
    data = pd.DataFrame(data)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)
    data.reset_index(inplace=True)
    data.set_index("Date", inplace=True)
    data.index = pd.to_datetime(data.index)
    return data
