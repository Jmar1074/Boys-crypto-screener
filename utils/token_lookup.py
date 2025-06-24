import requests

def search_token_id(user_input):
    try:
        url = f"https://api.coingecko.com/api/v3/search?query={user_input}"
        response = requests.get(url)
        response.raise_for_status()
        results = response.json().get("coins", [])

        if not results:
            return None

        best_match = results[0]
        return best_match.get("id")

    except Exception:
        return None
