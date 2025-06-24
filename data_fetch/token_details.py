import requests

def get_token_details(token_id):
    if not token_id:
        return None

    url = f"https://api.coingecko.com/api/v3/coins/{token_id}"
    params = {
        "localization": "false",
        "tickers": "false",
        "market_data": "true",
        "community_data": "true",
        "developer_data": "false",
        "sparkline": "false"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        return {
            "name": data.get("name"),
            "symbol": data.get("symbol"),
            "price": data.get("market_data", {}).get("current_price", {}).get("usd"),
            "market_cap": data.get("market_data", {}).get("market_cap", {}).get("usd"),
            "volume_24h": data.get("market_data", {}).get("total_volume", {}).get("usd"),
            "price_change_percentage_24h": data.get("market_data", {}).get("price_change_percentage_24h"),
            "sentiment_votes_up_percentage": data.get("sentiment_votes_up_percentage"),
            "sentiment_votes_down_percentage": data.get("sentiment_votes_down_percentage"),
            "description": data.get("description", {}).get("en", "").split(". ")[0]  # First sentence
        }

    except Exception:
        return None
