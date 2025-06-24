import requests

API_BASE = "https://api.example.com/coins"

def fetch_market_movers():
    resp = requests.get(f"{API_BASE}/market_movers")
    resp.raise_for_status()
    return resp.json()

def get_all_tokens():
    resp = requests.get(f"{API_BASE}/all_tokens")
    resp.raise_for_status()
    return resp.json()
