from luxury_project.ml_logic.data import load_data
from luxury_project.ml_logic.currencyconversion import convert_to_eur
from luxury_project.ml_logic.registry import save_data
from luxury_project.ml_logic.clean import clean_df
from luxury_project.ml_logic.scraper import web_scraper
from luxury_project.ml_logic.stock import get_stock_data
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

# Load the data
df_sales = load_data("SELECT * FROM `still-dynamics-451213-b9.Price_Monitoring.Sales`")
df_price = load_data("SELECT * FROM `still-dynamics-451213-b9.Price_Monitoring.Price`")
df_price["price"] = pd.to_numeric(df_price["price"], errors="coerce")
df_scraped = web_scraper()
df_stock = get_stock_data()

# Clean the data
df_price = clean_df(df_price)
df_sales = clean_df(df_sales)
df_scraped = clean_df(df_scraped)
df_stock = clean_df(df_stock)

#### Part 1 - tables exporting

df_sales["total_sales_EUR"] = convert_to_eur(
    df_sales["currency"], df_sales["total_sales"]
)
df_price["prices_EUR"] = convert_to_eur(df_price["currency"], df_price["price"])

save_data(df_sales, "SalesEUR")
save_data(df_price, "PriceEUR")
save_data(df_scraped, "Scraped")
save_data(df_stock, "Stock")

stock_data = get_stock_data("KER.PA")

# --- Select the Adjusted Close price series ---
if "Adj Close" in stock_data.columns:
    ts = stock_data["Adj Close"]
else:
    ts = stock_data["Close"]

ts = ts.sort_index()

# --- Check the Data ---
print("Data Description:")
print(ts.describe())
print("\nFirst few rows:")
print(ts.head())
print("\nLast few rows:")
print(ts.tail())

# Drop any remaining missing values
ts = ts.dropna()

# --- Fit an ARIMA(1,1,1) Model ---
try:
    model = ARIMA(ts, order=(1, 1, 1))
    model_fit = model.fit()
    print(model_fit.summary())
except Exception as e:
    print("Error fitting ARIMA model:", e)
    raise

# --- Forecast the Next 5 Trading Days ---
forecast_steps = 5
try:
    forecast = model_fit.forecast(steps=forecast_steps)
except Exception as e:
    print("Error during forecasting:", e)
    raise

# If forecast index isn't date-based, create a new date range using business days
if not isinstance(forecast.index, pd.DatetimeIndex):
    last_date = ts.index[-1]
    forecast_index = pd.date_range(
        start=last_date + pd.Timedelta(days=1), periods=forecast_steps, freq="B"
    )
    forecast = pd.Series(forecast, index=forecast_index)

print("\nForecast for the next 5 trading days:")
print(forecast)
