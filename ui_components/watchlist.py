from state.star_state import is_starred

def get_watchlist(tokens):
    return [token for token in tokens if is_starred(token['id'])]
