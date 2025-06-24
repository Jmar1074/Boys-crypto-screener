from data_fetch.coins import get_all_tokens

def get_token_by_id(token_id):
    tokens = get_all_tokens()
    for token in tokens:
        if token.get("id") == token_id:
            return token
    return None
