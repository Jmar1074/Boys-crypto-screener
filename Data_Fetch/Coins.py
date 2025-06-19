coins.py (Fallback-Integrated)

import pandas as pd import requests from utils.fallback_request import try_sources

Minimum Market Cap threshold for filtering

MIN_MARKET_CAP = 500_000

--- Fetch Top Coins with Fallback Support ---

def get_top_coins(): urls = [ "https://api.coingecko.com/api/v3/coins/markets", # Add more fallback URLs as needed ] params = { "vs_currency": "usd", "order": "market_cap_desc", "per_page": 100, "page": 1, "sparkline": False }

response = try_sources(urls, method="GET", params=params)
if response is not None and response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df = df[df["market_cap"] >= MIN_MARKET_CAP]
    df["volume_ratio"] = df["total_volume"] / (df["market_cap"] / 100)
    df = df.sort_values("market_cap", ascending=False)
    return df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "volume_ratio"]]
else:
    return pd.DataFrame(columns=["id", "symbol", "name", "current_price", "market_cap", "total_volume", "volume_ratio"])

