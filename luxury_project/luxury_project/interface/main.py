from luxury_project.ml_logic.data import load_data
from luxury_project.ml_logic.currencyconversion import convert_to_eur
from luxury_project.ml_logic.registry import save_data

df_sales = load_data("SELECT * FROM `still-dynamics-451213-b9.Price_Monitoring.Sales`")
df_price = load_data("SELECT * FROM `still-dynamics-451213-b9.Price_Monitoring.Price`")

df_sales['EUR'] = convert_to_eur(df_sale[''])

save_data(df_sales, "Sales_EUR")

