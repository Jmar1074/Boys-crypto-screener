from data_fetch.token_details import get_token_details
from data_fetch.sentiment import get_token_sentiment
from utils.fallback_request import try_sources

def token_deep_dive(token_id):
    detail_sources = [
        lambda: get_token_details(token_id),
        lambda: try_sources(token_id, fallback=True)
    ]

    for fetch in detail_sources:
        try:
            data = fetch()
            if data:
                break
        except Exception:
            continue
    else:
        return None

    sentiment_score, comments = get_token_sentiment(token_id)

    return {
        "details": data,
        "sentiment_score": sentiment_score,
        "sample_comments": comments
    }
