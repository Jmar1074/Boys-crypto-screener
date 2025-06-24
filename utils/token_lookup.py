from data_fetch.coins import get_all_tokens

def get_token_by_id(token_id):
    for t in get_all_tokens():
        if t.get("id") == token_id:
            return t
    return None
