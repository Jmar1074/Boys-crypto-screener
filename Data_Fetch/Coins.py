import requests
import pandas as pd

MIN_MARKET_CAP = 500_000  # You can change this threshold as needed

def get_top_coins():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        coins = response.json()
        df = pd.DataFrame(coins)
        return df
    except Exception as e:
        print("Error fetching top coins:", e)
        return pd.DataFrame()

def screen_coins(df):
    if df.empty:
        return pd.DataFrame()

    df = df[df["market_cap"] >= MIN_MARKET_CAP].copy()
    df["volume_ratio"] = df["total_volume"] / (df["market_cap"] / 100)
    df = df.sort_values("market_cap", ascending=False)
    return df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "volume_ratio"]]
