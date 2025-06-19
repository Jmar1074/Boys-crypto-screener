# sentiment.py (Fallback-Integrated)

import requests
from textblob import TextBlob
from utils.fallback_request import try_sources

def get_token_sentiment(token_name):
    query = token_name.lower()
    urls = [
        f"https://api.pushshift.io/reddit/search/comment/?q={query}&size=20",
        # Add future fallback URLs here
    ]
    response = try_sources(urls, method="GET")

    if response and response.status_code == 200:
        data = response.json().get("data", [])
        comments = [i.get("body", "") for i in data]
        sentiments = [TextBlob(text).sentiment.polarity for text in comments if text]
        average = round(sum(sentiments) / len(sentiments), 3) if sentiments else 0
        return average, comments[:3]

    return 0, []
