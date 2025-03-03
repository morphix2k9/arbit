
import requests
import json

def get_ebay_sold_prices(query):
    url = f"https://api.ebay.com/buy/browse/v1/item_summary/search?q={query}&filter=buyingOptions:FIXED_PRICE"
    headers = {"Authorization": "Bearer YOUR_EBAY_API_KEY"}
    response = requests.get(url, headers=headers)
    
    data = response.json()
    sold_prices = [float(item["price"]["value"]) for item in data.get("itemSummaries", [])]
    
    return sum(sold_prices) / len(sold_prices) if sold_prices else 0

product_name = "Cloud Couch"
ebay_price = get_ebay_sold_prices(product_name)
print(f"Average eBay sold price for {product_name}: ${ebay_price}")
