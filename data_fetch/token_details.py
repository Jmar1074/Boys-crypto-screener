from utils.fallback_request import try_sources

def get_token_details(token_id):
    try:
        return try_sources(token_id, fallback=True)
    except Exception:
        return {}
