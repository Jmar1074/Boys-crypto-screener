import json
import os

STARRED_FILE = "assets/starred.json"

def load_starred_tokens():
    if os.path.exists(STARRED_FILE):
        with open(STARRED_FILE) as f:
            return json.load(f)
    return []

def save_starred_tokens(tokens):
    with open(STARRED_FILE, "w") as f:
        json.dump(tokens, f)

def toggle_star(symbol):
    tokens = load_starred_tokens()
    if symbol in tokens:
        tokens.remove(symbol)
    else:
        tokens.append(symbol)
    save_starred_tokens(tokens)
