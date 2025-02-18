import requests
import pandas as pd
from luxury_project.params import CURRENCY_API

BASE_CURRENCY = "EUR"


# Function to get exchange rates
def get_exchange_rates():
    url = f"https://v6.exchangerate-api.com/v6/{CURRENCY_API}/latest/{BASE_CURRENCY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["conversion_rates"]
    else:
        print("Error fetching exchange rates:", response.status_code)
        return None


# Fetch exchange rates
exchange_rates = get_exchange_rates()


# Function to convert prices
def convert_to_eur(df):
    converted = []
    for row in df.iterrows():
        currency = row["currency"]
        price = row["price"]

        if currency in exchange_rates:
            converted.append(price / exchange_rates[currency])
    df["price_eur"] = converted
