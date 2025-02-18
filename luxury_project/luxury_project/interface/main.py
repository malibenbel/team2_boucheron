from luxury_project.ml_logic.data import load_data
from luxury_project.ml_logic.currencyconversion import convert_to_eur
from luxury_project.ml_logic.registry import save_data
import pandas as pd

df_sales = load_data("SELECT * FROM `still-dynamics-451213-b9.Price_Monitoring.Sales`")
df_price = load_data("SELECT * FROM `still-dynamics-451213-b9.Price_Monitoring.Price`")

<<<<<<< HEAD
df_sales['total_sales_EUR'] = convert_to_eur(df_sale['currency'], df_sale['total_sales'])
df_sales['prices_EUR'] = convert_to_eur(df_sale['currency'], df_sale['price'])

save_data(df_sales, "Sales_EUR")
save_data(df_price, "Price_EUR")
=======
df_price["price"] = pd.to_numeric(df_price["price"], errors="coerce")

df_sales["total_sales_EUR"] = convert_to_eur(
    df_sales["currency"], df_sales["total_sales"]
)
df_price["prices_EUR"] = convert_to_eur(df_price["currency"], df_price["price"])

save_data(df_sales, "SalesEUR")
save_data(df_price, "PriceEUR")
>>>>>>> 452e924 (Works)
print("Data saved successfully")
