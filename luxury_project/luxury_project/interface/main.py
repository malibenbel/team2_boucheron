from luxury_project.ml_logic.data import load_data
from luxury_project.ml_logic.currencyconversion import convert_to_eur
from luxury_project.ml_logic.registry import save_data
from luxury_project.ml_logic.clean import clean_df
from luxury_project.ml_logic.scraper import web_scraper
from luxury_project.ml_logic.stock import get_stock_data
from luxury_project.ml_logic.boucheron_recommender import boucheron_recommender
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd


def data_loading():
    # Load the data
    df_sales = load_data(
        "SELECT * FROM `still-dynamics-451213-b9.Price_Monitoring.Sales`"
    )
    df_price = load_data(
        "SELECT * FROM `still-dynamics-451213-b9.Price_Monitoring.Price`"
    )
    df_price["price"] = pd.to_numeric(df_price["price"], errors="coerce")
    df_stock = get_stock_data()
    return df_sales, df_price, df_stock


def scraping():
    df_scraped = web_scraper()
    return df_scraped


def preprocess(df_sales, df_price, df_scraped, df_stock):
    """
    Clean the data and save the processed versions.
    """
    # Clean the data
    df_price = clean_df(df_price)
    df_sales = clean_df(df_sales)
    df_scraped = clean_df(df_scraped)
    df_stock = clean_df(df_stock)

    # Save processed data
    save_data(df_sales, "SalesEUR")
    save_data(df_price, "PriceEUR")
    save_data(df_scraped, "Scraped")
    save_data(df_stock, "Stock")

    print("Preprocessing complete.")
    return df_sales, df_price, df_scraped, df_stock


def eur_conversion(df_sales, df_price):
    # Convert currency values to EUR
    df_sales["total_sales_EUR"] = convert_to_eur(
        df_sales["currency"], df_sales["total_sales"]
    )
    df_price["prices_EUR"] = convert_to_eur(df_price["currency"], df_price["price"])
    print("EUR conversion complete.")
    return df_sales, df_price


def streamlit():
    """
    Run the Boucheron recommender.
    """
    print("Starting recommender (training step)...")
    boucheron_recommender()
    return None


def train_test():
    """
    Train an ARIMA model on stock data and print a 10-day forecast.
    """
    print("Testing ARIMA model forecast...")
    df = get_stock_data("KER.PA")
    ts = df["Close"].dropna()
    ts = ts.asfreq("B").fillna(method="ffill")

    model = ARIMA(ts, order=(1, 1, 1))
    model_fit = model.fit()
    print(model_fit.summary())

    forecast_steps = 10
    forecast = model_fit.forecast(steps=forecast_steps)

    # Create a proper DatetimeIndex if needed
    if not isinstance(forecast.index, pd.DatetimeIndex):
        last_date = ts.index[-1]
        forecast_index = pd.date_range(
            start=last_date + pd.Timedelta(days=1), periods=forecast_steps, freq="B"
        )
        forecast = pd.Series(forecast, index=forecast_index)

    print("\nForecast for the next 10 trading days:")
    print(forecast)
    print("Testing complete.")


def main():
    """
    Run all steps in sequence.
    """
    df_sales, df_price, df_stock = data_loading()
    df_scraped = scraping()
    df_sales, df_price, df_scraped, df_stock = preprocess(
        df_sales, df_price, df_scraped, df_stock
    )
    df_sales, df_price = eur_conversion(df_sales, df_price)
    streamlit()
    train_test()


if __name__ == "__main__":
    main()
