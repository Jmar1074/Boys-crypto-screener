utils/fallback_request.py

import requests

def try_sources(sources, params=None, headers=None, timeout=5): """ Attempt to fetch data from multiple sources in order. Returns the first valid JSON response.

Args:
    sources (list): List of full URLs (strings).
    params (dict): Optional URL parameters.
    headers (dict): Optional headers.
    timeout (int): Timeout in seconds for each request.

Returns:
    dict or None: Parsed JSON if any request is successful, else None.
"""
for url in sources:
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        if response.ok:
            return response.json()
    except Exception as e:
        continue
return None

Example usage in another script:

from utils.fallback_request import try_sources

data = try_sources([

"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd",

"https://api.coinpaprika.com/v1/tickers"

])

