# Business Data Management: Team 2 Project

## Project Overview

Our luxury consulting engineering team stores historical product data in a massive BigQuery table: `edhec-business-manageme.luxurydata2502.price-monitoring-2022`, which contains over 2 million rows (limited from 5+ million for cost control). This data, extracted from a 2023 company study, was used to perform a strategic business analysis. In our case, we analyzed the evolution of the luxury brand Boucheron, exploring pricing trends, exchange rates, market dynamics, and other useful information.


## Functions Overview

- **data_loading()**: Loads sales, price, and stock data from BigQuery and Yahoo Finance.
- **scraping()**: Runs the web scraper to fetch extra product data.
- **preprocess()**: Cleans and saves all datasets.
- **eur_conversion()**: Converts sales and price currencies to EUR.
- **train_test()**: Fits an ARIMA model on KER.PA stock data and forecasts the next 10 trading days.
- **main()**: Runs the full pipeline in order.

## Makefile commands

To execute any of these commands, open your terminal in the project root and run:

- `make reinstall_package` to reinstall the package.
- `make data_loading` to run data_loading() and print its output.
- `make scraping` to run scraping() and print its result.
- `make preprocess` to load, clean, and save your data.
- `make eur_conversion` to convert currencies to EUR.
- `make streamlit` to launch the Streamlit recommender.
- `make train_test` to run the ARIMA forecast test.
- `make pipeline` to run the full pipeline via main().
- `make clean` to remove temporary and build files.

Simply type the desired command in your terminal and press Enter.
 
## Installation
1. Clone the repository.
2. Create and activate your Python environment (e.g., using pyenv or virtualenv).
3. Install required packages:
   ```bash
   pip install -r requirements.txt

