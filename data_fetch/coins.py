import requests

API_BASE_URL = "https://api.coingecko.com/api/v3"

def fetch_market_movers():
    url = f"{API_BASE_URL}/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "volume_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_top_movers():
    data = fetch_market_movers()
    return sorted(data, key=lambda x: x["price_change_percentage_24h"] or 0, reverse=True)[:10]

def get_token_by_id(token_id):
    url = f"{API_BASE_URL}/coins/{token_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
