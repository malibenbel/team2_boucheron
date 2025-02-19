from luxury_project.ml_logic.data import load_data
from luxury_project.ml_logic.currencyconversion import convert_to_eur
from luxury_project.ml_logic.registry import save_data
from luxury_project.ml_logic.clean import clean_df
from luxury_project.ml_logic.scraper import web_scraper
from luxury_project.ml_logic.stock import get_stock_data
from luxury_project.ml_logic.boucheron_recommender import boucheron_recommender
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Load the data
df_sales = load_data("SELECT * FROM `still-dynamics-451213-b9.Price_Monitoring.Sales`")
df_price = load_data("SELECT * FROM `still-dynamics-451213-b9.Price_Monitoring.Price`")
df_recommendations = load_data("SELECT * FROM `still-dynamics-451213-b9.Price_Monitoring.recom`")
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
# ✅ Call the function when running the script
if __name__ == "__main__":
    boucheron_recommender()

"""
#### Part 2 - model training

# 1. Check for non-numeric values in the prices_EUR column
non_numeric_prices = df_price[
    ~df_price["prices_EUR"].apply(lambda x: isinstance(x, (int, float)))
]
print("Non-numeric price values found:")
print(non_numeric_prices)

# 2. Convert prices_EUR to numeric (non-convertible values become NaN)
df_price["prices_EUR"] = pd.to_numeric(df_price["prices_EUR"], errors="coerce")

# Optional: Drop rows where prices_EUR is NaN after conversion
df_price = df_price.dropna(subset=["prices_EUR"])

# 3. Prepare features and target variable
# One-hot encode the categorical columns ("collection" and "currency")
X = pd.get_dummies(df_price[["collection", "currency"]])
y = df_price["prices_EUR"]

# 4. Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 5. Train the KNeighborsRegressor model
model = KNeighborsRegressor(n_neighbors=5)
model.fit(X_train, y_train)

# 6. Evaluate the model on the test set
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"📊 Mean Squared Error: {mse:.4f}")
print(f"📈 R-squared: {r2:.4f}")
"""
