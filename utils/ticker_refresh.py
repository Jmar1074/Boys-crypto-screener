import threading
import time
from data_fetch.coins import fetch_market_movers
from state.star_state import load_starred_tokens

def background_token_refresher(interval=300):
    def refresh_loop():
        while True:
            try:
                fetch_market_movers()
                load_starred_tokens()
            except Exception as e:
                print(f"[Background Refresh Error]: {e}")
            time.sleep(interval)

    thread = threading.Thread(target=refresh_loop, daemon=True)
    thread.start()
