from luxury_project.ml_logic.data import load_data

df_sales = load_data("SELECT * FROM `still-dynamics-451213-b9.Sales.sales`")
df_price = load_data("SELECT * FROM `still-dynamics-451213-b9.Price_Monitoring.Price`")
