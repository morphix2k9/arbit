import os 
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Function to scrape Amazon Best Sellers using Selenium
def get_amazon_best_sellers():
    url = "https://www.amazon.com/Best-Sellers/zgbs"

    # Set up Selenium WebDriver with options to avoid detection
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Use headless mode
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Disable GPU/WebGL and enforce software rendering
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-webgl")
    chrome_options.add_argument("--disable-3d-apis")
    chrome_options.add_argument("--disable-features=VizDisplayCompositor")
    chrome_options.add_argument("--use-gl=swiftshader")
    chrome_options.add_argument("--disable-angle-features")
    
    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get(url)
        time.sleep(5)  # Allow JavaScript to load

        # Get page source and parse with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        products = []
        for item in soup.select("div.p13n-sc-truncate-desktop-type2, div.zg-text-center-align a div"):
            products.append(item.get_text(strip=True))

        return products[:10] if products else ["No products found!"]
    
    finally:
        driver.quit()  # Close the browser

# Fetch Amazon best sellers
amazon_trending = get_amazon_best_sellers()

# Use raw string (r"") to avoid invalid escape sequence error
output_dir = output_dir = "C:\\Wrkspace\\ai-arbitrage"
os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

output_file = os.path.join(output_dir, "trending_products.csv")

# Save results to CSV
df = pd.DataFrame(amazon_trending, columns=["Trending Products"])
df.to_csv(output_file, index=False)

print(f"Top trending products saved to {output_file}")
