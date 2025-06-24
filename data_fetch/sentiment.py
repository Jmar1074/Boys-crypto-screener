from utils.fallback_request import try_sources

def get_token_sentiment(token_id):
    try:
        sentiment_data = try_sources(token_id, sentiment=True)
        if sentiment_data:
            score = sentiment_data.get("sentiment_score", 0)
            comments = sentiment_data.get("sample_comments", [])
            return score, comments
    except Exception:
        pass

    return 0, []
