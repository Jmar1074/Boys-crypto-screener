
import requests
from utils.fallback_request import try_sources

def get_token_sentiment(token_id):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{token_id}"
        response = requests.get(url)
        data = response.json()

        sentiment_score = data.get("sentiment_votes_up_percentage", 0)
        comments = data.get("description", {}).get("en", "").split(". ")[:3]

        return sentiment_score, comments

    except Exception:
        return 0, ["Sentiment data unavailable."]
