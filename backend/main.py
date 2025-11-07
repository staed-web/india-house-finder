from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from scrapers.magicbricks import scrape_magicbricks
from scrapers.nobroker import scrape_nobroker
import logging

app = FastAPI(title="India House Finder API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/listings")
async def get_listings(
    city: str = "bangalore",
    min_price: int = 0,
    max_price: int = 50000000,
    bedrooms: int = None,
    property_type: str = "all"
):
    try:
        listings = []
        listings.extend(scrape_magicbricks(city, min_price, max_price, bedrooms))
        listings.extend(scrape_nobroker(city, min_price, max_price, bedrooms))
        # Apply filters
        filtered = [l for l in listings 
                   if (property_type == "all" or l["type"] == property_type)]
        return {"listings": filtered[:100]}  # Cap at 100 for performance
    except Exception as e:
        logging.error(f"Scraping failed: {e}")
        raise HTTPException(status_code=500, detail="Aggregation temporarily unavailable")
