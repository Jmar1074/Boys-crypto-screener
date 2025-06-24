from data_fetch.token_details import get_token_details
from data_fetch.sentiment import get_token_sentiment
from utils.fallback_request import try_sources

def deep_dive_data(token_id):
    data_sources = [
        lambda: get_token_details(token_id),
        lambda: try_sources(token_id, fallback=True)
    ]

    data = None
    for fetcher in data_sources:
        try:
            result = fetcher()
            if result:
                data = result
                break
        except Exception:
            continue

    if not data:
        return None

    sentiment_score, comments = get_token_sentiment(token_id)

    return {
        "details": data,
        "sentiment_score": sentiment_score,
        "sample_comments": comments
    }
