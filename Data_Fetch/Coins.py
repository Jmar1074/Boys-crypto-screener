coins.py — Refactored with Fallback Support

import pandas as pd from utils.fallback_request import try_sources

def fetch_top_coins(limit=100): """ Fetch top coins by market cap using multiple fallback APIs. """ url_sources = [ "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false", "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit=100&convert=USD" ]

data = try_sources(url_sources)
if not data:
    return pd.DataFrame()

# Handle CoinGecko format
if isinstance(data, list) and 'id' in data[0]:
    df = pd.DataFrame(data)
    df["volume_ratio"] = df["total_volume"] / (df["market_cap"] / 100)
    return df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "volume_ratio"]]

# Handle CoinMarketCap format
elif isinstance(data, dict) and 'data' in data:
    parsed = []
    for token in data['data']:
        parsed.append({
            "id": token["slug"],
            "symbol": token["symbol"].lower(),
            "name": token["name"],
            "current_price": token["quote"]["USD"]["price"],
            "market_cap": token["quote"]["USD"]["market_cap"],
            "total_volume": token["quote"]["USD"]["volume_24h"],
        })
    df = pd.DataFrame(parsed)
    df["volume_ratio"] = df["total_volume"] / (df["market_cap"] / 100)
    return df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "volume_ratio"]]

return pd.DataFrame()

