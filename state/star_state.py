import json
import os

STARRED_FILE = "state/starred_tokens.json"

def load_starred_tokens():
    if os.path.exists(STARRED_FILE):
        with open(STARRED_FILE, "r") as f:
            return json.load(f)
    return []

def save_starred_tokens(tokens):
    with open(STARRED_FILE, "w") as f:
        json.dump(tokens, f)

def toggle_star(token_id):
    tokens = load_starred_tokens()
    if token_id in tokens:
        tokens.remove(token_id)
    else:
        tokens.append(token_id)
    save_starred_tokens(tokens)

def is_starred(token_id):
    return token_id in load_starred_tokens()

def get_starred_tokens():
    return load_starred_tokens()
