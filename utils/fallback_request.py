import requests

def try_sources(token_id, fallback=False):
    sources = [
        f"https://api.coingecko.com/api/v3/coins/{token_id}",
        f"https://api.coinpaprika.com/v1/coins/{token_id}"
    ]

    for source in sources:
        try:
            response = requests.get(source)
            if response.status_code == 200:
                return response.json()
        except Exception:
            continue

    if fallback:
        return {"message": "All fallback sources failed."}
    return None
