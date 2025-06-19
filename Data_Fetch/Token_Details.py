import requests
from utils.fallback_request import try_sources

def get_token_details(token_id):
    """
    Retrieves detailed information for a given token from CoinGecko.
    Falls back to alternative sources if needed.
    """
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{token_id}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Extracted core details
        return {
            "name": data.get("name"),
            "symbol": data.get("symbol"),
            "price": data.get("market_data", {}).get("current_price", {}).get("usd"),
            "market_cap": data.get("market_data", {}).get("market_cap", {}).get("usd"),
            "volume": data.get("market_data", {}).get("total_volume", {}).get("usd"),
            "change_24h": data.get("market_data", {}).get("price_change_percentage_24h"),
            "homepage": data.get("links", {}).get("homepage", [None])[0],
            "image": data.get("image", {}).get("large"),
            "description": data.get("description", {}).get("en", "")[:500]  # Trimmed for UI readability
        }
    except Exception:
        # Fallback if primary fetch fails
        return try_sources(token_id, fallback=True)
