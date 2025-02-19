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

ts = df_sales["number_of_items_sold"]

# --- Fit a Simple ARIMA Model ---
# The order (1,1,1) is just a starting point; further tuning may be required.
model = ARIMA(ts, order=(1, 1, 1))
model_fit = model.fit()

# Print the model summary
print(model_fit.summary())

# --- Forecast Future Quantity ---
# Forecast the next 12 time periods (e.g., months, days, depending on your frequency)
forecast_steps = 12
forecast = model_fit.forecast(steps=forecast_steps)
print("Forecast for the next", forecast_steps, "periods:")
print(forecast)
