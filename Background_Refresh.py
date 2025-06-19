background_refresh.py — Live Data Auto-Updater

import threading import time from data_fetch.coins import fetch_top_tokens

Global cache

cached_data = [] last_updated = None refresh_interval = 60  # seconds (adjust as needed)

def background_updater(): global cached_data, last_updated while True: try: new_data = fetch_top_tokens() if not new_data.empty: cached_data = new_data.copy() last_updated = time.strftime("%Y-%m-%d %H:%M:%S") print(f"[Refresh] Data updated at {last_updated}") except Exception as e: print(f"[Refresh Error] {e}") time.sleep(refresh_interval)

def start_background_thread(): thread = threading.Thread(target=background_updater, daemon=True) thread.start()

def get_cached_tokens(): return cached_data.copy(), last_updated

