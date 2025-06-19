token_details.py (Fallback-Integrated)

import requests from utils.fallback_request import try_sources

def get_token_details(token_id): urls = [ f"https://api.coingecko.com/api/v3/coins/{token_id}", # Add more fallback endpoints here if needed ]

response = try_sources(urls, method="GET")

if response and response.status_code == 200:
    data = response.json()
    market_data = data.get("market_data", {})
    return {
        "name": data.get("name"),
        "symbol": data.get("symbol"),
        "price": market_data.get("current_price", {}).get("usd"),
        "market_cap": market_data.get("market_cap", {}).get("usd"),
        "volume": market_data.get("total_volume", {}).get("usd"),
        "circulating": market_data.get("circulating_supply"),
        "total": market_data.get("total_supply"),
        "id": data.get("id"),
    }
return None

