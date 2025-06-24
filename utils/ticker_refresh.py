import requests
import time

_cache = {}

def get_token_ticker(token_id, force_refresh=False):
    current_time = time.time()
    cache_expiry = 120  # seconds

    if (
        not force_refresh and
        token_id in _cache and
        current_time - _cache[token_id]["timestamp"] < cache_expiry
    ):
        return _cache[token_id]["data"]

    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies=usd&include_24hr_vol=true"
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()

        if token_id in json_data:
            price = json_data[token_id].get("usd", 0.0)
            volume = json_data[token_id].get("usd_24h_vol", 0.0)
        else:
            price = 0.0
            volume = 0.0

        data = {
            "price": price,
            "volume": volume
        }

        _cache[token_id] = {
            "data": data,
            "timestamp": current_time
        }

        return data

    except Exception:
        return {
            "price": 0.0,
            "volume": 0.0
        }
