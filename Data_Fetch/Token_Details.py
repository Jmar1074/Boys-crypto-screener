import requests

def get_token_details(token_id):
    """
    Fetches token metadata from primary provider (CoinGecko by default).
    """
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{token_id}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        return {
            "name": data.get("name", ""),
            "symbol": data.get("symbol", "").upper(),
            "description": data.get("description", {}).get("en", ""),
            "market_cap": data.get("market_data", {}).get("market_cap", {}).get("usd", 0),
            "circulating_supply": data.get("market_data", {}).get("circulating_supply", 0),
            "total_supply": data.get("market_data", {}).get("total_supply", 0),
            "max_supply": data.get("market_data", {}).get("max_supply", 0),
            "ath": data.get("market_data", {}).get("ath", {}).get("usd", 0),
            "atl": data.get("market_data", {}).get("atl", {}).get("usd", 0),
            "homepage": data.get("links", {}).get("homepage", [""])[0],
            "categories": data.get("categories", []),
            "image": data.get("image", {}).get("thumb", ""),
        }

    except Exception:
        return {
            "name": token_id.capitalize(),
            "symbol": token_id.upper(),
            "description": "No description available.",
            "market_cap": None,
            "circulating_supply": None,
            "total_supply": None,
            "max_supply": None,
            "ath": None,
            "atl": None,
            "homepage": "",
            "categories": [],
            "image": "",
        }
