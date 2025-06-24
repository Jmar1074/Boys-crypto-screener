import requests

API_BASE = "https://api.example.com/coins"

def get_token_details(token_id):
    resp = requests.get(f"{API_BASE}/{token_id}")
    resp.raise_for_status()
    return resp.json()
