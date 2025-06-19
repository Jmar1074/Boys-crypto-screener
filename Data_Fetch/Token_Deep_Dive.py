from data_fetch.token_details import get_token_details
from data_fetch.sentiment import get_token_sentiment
from utils.fallback_request import try_sources

def deep_dive_data(token_id):
    """
    Provides a consolidated token profile including market data and sentiment insights.
    Tries multiple sources in fallback order for maximum resilience.
    """
    data_sources = [
        lambda: get_token_details(token_id),
        lambda: try_sources(token_id, fallback=True)
    ]

    token_data = None
    for fetch in data_sources:
        try:
            token_data = fetch()
            if token_data:
                break
        except Exception:
            continue

    if not token_data:
        return {
            "details": None,
            "sentiment_score": None,
            "sample_comments": []
        }

    sentiment_score, comments = get_token_sentiment(token_id)

    return {
        "details": token_data,
        "sentiment_score": sentiment_score,
        "sample_comments": comments or []
    }
