import requests

def scrape_nobroker(city, min_price, max_price, bedrooms):
    # NoBroker PUBLIC API (no auth needed for basic data)
    url = f"https://www.nobroker.in/api/v1/pg/search?city={city}&rentMin={min_price}&rentMax={max_price}"
    if bedrooms: url += f"&bedrooms={bedrooms}"
    try:
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = res.json()
        return [{
            "id": item["id"],
            "platform": "NoBroker",
            "title": item["title"],
            "price": item["rent"],
            "bedrooms": item.get("bhk", 0),
            "area_sqft": item.get("propertyArea", 0),
            "location": item["locality"],
            "url": f"https://www.nobroker.in/property/{item['id']}",
            "image_thumbnail": item.get("imageUrls", [""])[0],
            "type": "rent" if "rent" in url else "buy"
        } for item in data.get("data", [])]
    except:
        return []
