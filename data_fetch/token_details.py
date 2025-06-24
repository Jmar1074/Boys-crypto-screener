import requests
from utils.fallback_request import try_sources

def get_token_details(token_id):
    url = f"https://api.coingecko.com/api/v3/coins/{token_id}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception:
        pass

    # If primary fails, fallback
    return try_sources(token_id, fallback=True)
