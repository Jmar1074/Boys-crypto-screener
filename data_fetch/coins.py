import requests

def fetch_market_movers():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "volume_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return sorted(data, key=lambda x: x["total_volume"], reverse=True)
    except Exception:
        return []
