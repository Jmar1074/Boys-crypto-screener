import requests
from textblob import TextBlob

def get_token_sentiment(token_name):
    try:
        url = f"https://api.pushshift.io/reddit/search/comment/?q={token_name}&size=20"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json().get("data", [])
            comments = [item["body"] for item in data if "body" in item]
            scores = [TextBlob(comment).sentiment.polarity for comment in comments]
            avg_score = round(sum(scores) / len(scores), 3) if scores else 0
            return avg_score, comments[:3]
    except Exception as e:
        print("Sentiment fetch error:", e)
    return 0.0, []
