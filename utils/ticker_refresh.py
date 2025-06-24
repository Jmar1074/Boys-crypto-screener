import threading, time
from data_fetch.coins import fetch_market_movers

def _refresh_loop(interval, callback):
    while True:
        time.sleep(interval)
        callback()

def background_token_refresher(interval=60):
    t = threading.Thread(
        target=_refresh_loop,
        args=(interval, fetch_market_movers),
        daemon=True
    )
    t.start()
