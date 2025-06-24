import json
import os

WATCHLIST_FILE = "assets/watchlist.json"

def get_watchlist_tokens():
    if os.path.exists(WATCHLIST_FILE):
        with open(WATCHLIST_FILE) as f:
            return json.load(f)
    return []
