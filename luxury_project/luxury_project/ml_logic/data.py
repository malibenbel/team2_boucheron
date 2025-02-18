from google.cloud import bigquery
import pandas as pd
import os
from luxury_project.params import GOOGLE_CREDENTIALS


# Authenticate & initialize BigQuery client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_CREDENTIALS
client = bigquery.Client()


def load_data(query):
    df = client.query(query).to_dataframe()
    print(f"Loaded {df.shape[0]} rows.")
    return df
