
import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_amazon_best_sellers():
    url = "https://www.amazon.com/Best-Sellers/zgbs"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    products = []
    for item in soup.select(".p13n-sc-truncate"):
        products.append(item.get_text(strip=True))
    
    return products[:10]

amazon_trending = get_amazon_best_sellers()
df = pd.DataFrame(amazon_trending, columns=["Trending Products"])
df.to_csv("trending_products.csv", index=False)
print("Top trending products saved!")
