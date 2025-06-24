import json
import os

WATCHLIST_FILE = "watchlist.json"

def load_watchlist():
    if not os.path.exists(WATCHLIST_FILE):
        return []
    with open(WATCHLIST_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_watchlist(watchlist):
    with open(WATCHLIST_FILE, "w") as f:
        json.dump(watchlist, f, indent=2)

def toggle_watchlist(token_id):
    watchlist = load_watchlist()
    if token_id in watchlist:
        watchlist.remove(token_id)
    else:
        watchlist.append(token_id)
    save_watchlist(watchlist)
