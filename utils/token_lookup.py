from data_fetch.token_details import get_token_details
from utils.fallback_request import try_sources

def lookup_token(token_id):
    data = get_token_details(token_id)
    if not data:
        data = try_sources(token_id, fallback=True)
    return data
