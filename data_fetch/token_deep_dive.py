from data_fetch.token_details import get_token_details
from data_fetch.sentiment import get_token_sentiment

def deep_dive_data(token_id):
    try:
        details = get_token_details(token_id)
    except Exception:
        details = {}

    try:
        sentiment_score, comments = get_token_sentiment(token_id)
    except Exception:
        sentiment_score, comments = None, []

    return {
        "details": details,
        "sentiment_score": sentiment_score,
        "sample_comments": comments
    }
