import json
import os

WATCHLIST_FILE = os.path.join("data", "watchlist.json")

def is_starred(token_id):
    try:
        with open(WATCHLIST_FILE, "r") as f:
            watchlist = json.load(f)
        return token_id in watchlist
    except Exception:
        return False
