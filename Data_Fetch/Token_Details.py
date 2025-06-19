import requests
import pandas as pd

def get_token_details(token_id):
    url = f"https://api.coingecko.com/api/v3/coins/{token_id}"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"Error fetching details for {token_id}: {e}")
        return {}

def get_token_chart(token_id, days=7):
    url = f"https://api.coingecko.com/api/v3/coins/{token_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        prices = r.json().get("prices", [])
        df = pd.DataFrame(prices, columns=["time", "price"])
        df["time"] = pd.to_datetime(df["time"], unit="ms")
        return df
    except Exception as e:
        print(f"Error fetching chart for {token_id}: {e}")
        return pd.DataFrame()
