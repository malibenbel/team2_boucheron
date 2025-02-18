import os
from dotenv import load_dotenv

load_dotenv()
# Load environment variables load_dotenv()
GOOGLE_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")
CURRENCY_API = os.getenv("CURRENCY_API_KEY")
MODEL_TARGET = os.environ.get("MODEL_TARGET")
