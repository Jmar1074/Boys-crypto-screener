import requests

def try_sources(token_id, fallback=False):
    """
    Attempts to fetch token metadata from a fallback source if primary fails.
    Currently uses CoinPaprika as secondary.
    """

    if not fallback:
        return None

    try:
        url = f"https://api.coinpaprika.com/v1/coins/{token_id}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        return {
            "name": data.get("name", ""),
            "symbol": data.get("symbol", "").upper(),
            "description": data.get("description", "No description available."),
            "market_cap": None,
            "circulating_supply": None,
            "total_supply": None,
            "max_supply": None,
            "ath": None,
            "atl": None,
            "homepage": data.get("links", {}).get("website", [""])[0] if isinstance(data.get("links", {}).get("website"), list) else "",
            "categories": [],
            "image": "",  # Could be populated via scraped source
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
