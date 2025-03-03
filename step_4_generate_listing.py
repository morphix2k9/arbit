
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_listing(title, condition, price, features):
    prompt = f"Create a high-converting eBay listing for a {title}. Condition: {condition}. Price: ${price}. Features: {features}."
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

listing_description = generate_listing("Cloud Couch Dupe", "Like New", 1200, "Soft fabric, deep seating, modern design")
print("Generated Listing:\n", listing_description)
