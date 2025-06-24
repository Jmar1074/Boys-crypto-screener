import requests

def try_sources(token_id, fallback=False):
    try:
        response = requests.get(f"https://api.coingecko.com/api/v3/coins/{token_id}")
        response.raise_for_status()
        data = response.json()
    except Exception:
        if not fallback:
            return None
        try:
            response = requests.get(f"https://api.coinpaprika.com/v1/coins/{token_id}")
            response.raise_for_status()
            data = response.json()
        except Exception:
            return None

    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "symbol": data.get("symbol"),
        "market_cap": data.get("market_cap", None),
        "current_price": (
            data.get("market_data", {}).get("current_price", {}).get("usd")
            if "market_data" in data
            else data.get("quotes", {}).get("USD", {}).get("price")
        ),
        "volume": (
            data.get("market_data", {}).get("total_volume", {}).get("usd")
            if "market_data" in data
            else data.get("quotes", {}).get("USD", {}).get("volume_24h")
        ),
        "price_change_percentage_24h": (
            data.get("market_data", {}).get("price_change_percentage_24h")
            if "market_data" in data
            else data.get("quotes", {}).get("USD", {}).get("percent_change_24h")
        ),
    }
