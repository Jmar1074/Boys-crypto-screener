import requests import json

def fetch_top_tokens(limit=100): url = f"https://api.coingecko.com/api/v3/coins/markets" params = { 'vs_currency': 'usd', 'order': 'volume_desc', 'per_page': limit, 'page': 1, 'sparkline': False } try: response = requests.get(url, params=params) response.raise_for_status() return response.json() except Exception as e: print(f"[ERROR] Failed to fetch top tokens: {e}") return []

def format_token_data(token): return { 'id': token.get('id'), 'symbol': token.get('symbol').upper(), 'name': token.get('name'), 'price': f"${token.get('current_price'):,.4f}", 'volume': token.get('total_volume'), 'image': token.get('image') }

def get_tokens(limit=100): raw_tokens = fetch_top_tokens(limit) return [format_token_data(t) for t in raw_tokens if t.get('id') and t.get('symbol') and t.get('name')]

