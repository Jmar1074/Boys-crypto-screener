import requests
import random
import time

def try_sources(token_id, fallback=False):
    """
    Attempts multiple sources to retrieve token data.
    Used when main API fails or for cross-verification.
    """
    sources = [
        lambda: fetch_coingecko_data(token_id),
        lambda: fetch_mock_data(token_id),  # Used only if fallback=True
    ]

    for fetch in sources:
        try:
            result = fetch()
            if result:
                return result
        except Exception:
            continue
    return None


def fetch_coingecko_data(token_id):
    url = f"https://api.coingecko.com/api/v3/coins/{token_id}"
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data.get("name"),
            "symbol": data.get("symbol"),
            "price": data.get("market_data", {}).get("current_price", {}).get("usd"),
            "market_cap": data.get("market_data", {}).get("market_cap", {}).get("usd"),
            "volume": data.get("market_data", {}).get("total_volume", {}).get("usd"),
            "rank": data.get("market_cap_rank"),
        }
    return None


def fetch_mock_data(token_id):
    """
    Returns a mock dataset (used as last fallback).
    """
    return {
        "name": f"{token_id.capitalize()} (Offline)",
        "symbol": token_id[:4].upper(),
        "price": round(random.uniform(0.01, 100), 2),
        "market_cap": random.randint(1_000_000, 50_000_000),
        "volume": random.randint(100_000, 5_000_000),
        "rank": random.randint(100, 1000),
    }
