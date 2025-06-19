token_deep_dive.py — Refactored with Fallback Support

from utils.fallback_request import try_sources

def fetch_token_deep_dive(token_id): """ Pull detailed token metrics (supply, all-time high, ROI stats). """ url_sources = [ f"https://api.coingecko.com/api/v3/coins/{token_id}", f"https://coins.llama.fi/prices/current/coingecko:{token_id}" ]

data = try_sources(url_sources)
if not data:
    return None

if 'market_data' in data:
    market = data['market_data']
    return {
        "price": market['current_price']['usd'],
        "market_cap": market['market_cap']['usd'],
        "volume_24h": market['total_volume']['usd'],
        "circulating_supply": market['circulating_supply'],
        "total_supply": market['total_supply'],
        "ath": market['ath']['usd'],
        "ath_date": market['ath_date']['usd'],
    }

elif 'coins' in data and f"coingecko:{token_id}" in data['coins']:
    token_data = data['coins'][f"coingecko:{token_id}"]
    return {
        "price": token_data.get("price"),
        "market_cap": token_data.get("marketCap"),
        "volume_24h": token_data.get("volume"),
        "circulating_supply": token_data.get("circulatingSupply"),
        "total_supply": token_data.get("totalSupply"),
        "ath": token_data.get("ath"),
        "ath_date": token_data.get("athDate"),
    }

return None

