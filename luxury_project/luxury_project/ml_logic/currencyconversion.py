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


"""
# Function to convert prices
def convert_to_eur(currency_col, price_col):
    exchange_rates = get_exchange_rates()
    return price_col.where(
        currency_col == "EUR", price_col / currency_col.map(exchange_rates)
    )
"""


def convert_to_eur(currency_col, price_col):
    # Convert price_col to float to allow float arithmetic
    price_col = price_col.astype(float)
    exchange_rates = get_exchange_rates()
    return price_col.where(
        currency_col == "EUR", price_col / currency_col.map(exchange_rates)
    )
