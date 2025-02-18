from google.cloud import bigquery
import pandas as pd
import os
from luxury_project.params import GOOGLE_CREDENTIALS, PROJECT_ID, DATASET_ID

def save_data(df, table_name):
    table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}" 
    df.to_gbq(table_id, project_id=PROJECT_ID, if_exists="replace") 
    print(f"Data saved to {table_id}")
