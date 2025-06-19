import requests
from utils.fallback_request import try_sources

def get_token_sentiment(token_id):
    """
    Pulls real-time sentiment score and comments from primary API,
    falls back to mock structure or alternative later-enabled source.
    """
    try:
        url = f"https://cryptosentimentapi.com/api/sentiment/{token_id}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        result = response.json()

        sentiment_score = result.get("score", None)
        comments = result.get("comments", [])
        return sentiment_score, comments

    except Exception:
        # Optional fallback using try_sources() in future integration
        fallback_data = try_sources(token_id, sentiment=True)
        return fallback_data.get("score", None), fallback_data.get("comments", [])
