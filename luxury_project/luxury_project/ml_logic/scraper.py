from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in background
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("start-maximized")

# Set up WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)

# Store extracted data
all_watches = []
def web_scraper():
    # Start scraping from page 1 and continue
    page = 1
    while True:
        if page == 1:
            url = "https://www.boucheron.com/fr_fr/horlogerie/toute-l-horlogerie.html"  # First page URL
        else:
            url = f"https://www.boucheron.com/fr_fr/horlogerie/toute-l-horlogerie.html?p={page}"  # Next pages

        print(f"🔄 Scraping Page {page}... [{url}]")
        driver.get(url)
        time.sleep(5)  # Wait for JavaScript to load

        # Find all product containers
        products = driver.find_elements(By.CLASS_NAME, "product-item")

        if not products:  # If no products are found, stop the loop
            print(f"No more products found on page {page}. Stopping.")
            break

        for product in products:
            try:
                # Extract reference code
                ref_code = (
                    product.find_element(By.XPATH, ".//span[contains(text(), 'ref')]")
                    .text.replace("ref • ", "")
                    .strip()
                )
            except:
                ref_code = "N/A"

            try:
                # Extract price
                price = product.find_element(By.CLASS_NAME, "price").text.strip()
            except:
                price = "N/A"

            # Store in list
            all_watches.append({"Reference Code": ref_code, "Price": price})

        print(f"Page {page} scraped successfully.")
        page += 1  # Move to the next page

    df_scraped = pd.DataFrame(all_watches)
    driver.quit()
    return df_scraped
