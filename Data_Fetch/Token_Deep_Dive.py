token_deep_dive.py — Finalized with Structured Deep Dive

from data_fetch.token_details import get_token_details from data_fetch.sentiment import get_token_sentiment from utils.fallback_request import try_sources

def deep_dive_data(token_id): """ Combines token detail retrieval and sentiment analysis. Falls back to secondary data if needed. """ data_sources = [ lambda: get_token_details(token_id), lambda: try_sources([ f"https://api.coingecko.com/api/v3/coins/{token_id}", f"https://coins.llama.fi/prices/current/coingecko:{token_id}" ]) ]

token_data = None
for fetch in data_sources:
    try:
        data = fetch()
        if data:
            token_data = data
            break
    except Exception:
        continue

if not token_data:
    return None

sentiment_score, comments = get_token_sentiment(token_id)

return {
    "details": token_data,
    "sentiment_score": sentiment_score,
    "sample_comments": comments or []
}

