import time
import random
from bs4 import BeautifulSoup
import requests

def scrape_magicbricks(city, min_price, max_price, bedrooms):
    city_slug = city.replace(" ", "-").lower()
    url = f"https://www.magicbricks.com/property-for-rent/residential-real-estate/{city_slug}"
    params = {"bedroom": bedrooms or "", "budgetMin": min_price, "budgetMax": max_price}
    
    try:
        time.sleep(random.uniform(5, 8))  # Ethical delay
        res = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, 'html.parser')
        listings = []
        for prop in soup.select("div.mb-srp__list"):
            price = prop.select_one(".mb-srp__c__l-price")
            if not price: continue
            listings.append({
                "id": prop.get("id", ""),
                "platform": "MagicBricks",
                "title": prop.select_one(".mb-srp__c__l-title")?.get_text(strip=True),
                "price": int(price.get_text().replace("₹", "").replace(",", "").split()[0]) * 100000,
                "bedrooms": bedrooms or 0,
                "area_sqft": 0,  # MagicBricks hides this—skip or estimate
                "location": prop.select_one(".mb-srp__c__l-location")?.get_text(strip=True),
                "url": "https://www.magicbricks.com" + prop.select_one("a")["href"],
                "image_thumbnail": "",
                "type": "rent"
            })
        return listings
    except:
        return []
