reinstall_package:
	@pip uninstall -y luxury || :
	@pip install -e .

# Run data_loading() alone and print the returned tuple.
data_loading:
	python -c "from luxury_project.interface.main import data_loading; print(data_loading())"

# Run scraping() alone and print the result.
scraping:
	python -c "from luxury_project.interface.main import scraping; print(scraping())"

# Run preprocess(): first load data and scrape, then clean and save.
preprocess:
	python -c "from luxury_project.interface.main import data_loading, scraping, preprocess; \
	df_sales, df_price, df_stock = data_loading(); \
	df_scraped = scraping(); \
	preprocess(df_sales, df_price, df_scraped, df_stock)"

# Run eur_conversion(): load data then perform EUR conversion.
eur_conversion:
	python -c "from luxury_project.interface.main import data_loading, eur_conversion; \
	df_sales, df_price, _ = data_loading(); \
	eur_conversion(df_sales, df_price)"

# Run the recommender (streamlit function).
streamlit:
	python -c "from luxury_project.interface.main import streamlit; streamlit()"

# Run the ARIMA forecast test.
train_test:
	python -c "from luxury_project.interface.main import train_test; train_test()"

# Run the full pipeline using main()
pipeline:
	python -c "from luxury_project.interface.main import main; main()"

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr **/__pycache__ **/*.pyc
	@rm -fr **/build **/dist
	@rm -fr proj-*.dist-info
	@rm -fr proj.egg-info
	@rm -f **/.DS_Store
	@rm -f **/*Zone.Identifier
	@rm -f **/.ipynb_checkpoints

