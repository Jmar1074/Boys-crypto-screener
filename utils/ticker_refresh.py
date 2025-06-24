
import time
import threading

class TickerRefresher:
    def __init__(self, interval=60):
        self.interval = interval
        self._data = {}
        self._lock = threading.Lock()
        self._running = False
        self._thread = None

    def start(self, fetch_function):
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._refresh_loop, args=(fetch_function,))
            self._thread.daemon = True
            self._thread.start()

    def _refresh_loop(self, fetch_function):
        while self._running:
            try:
                data = fetch_function()
                with self._lock:
                    self._data = data
            except Exception:
                pass
            time.sleep(self.interval)

    def get_data(self):
        with self._lock:
            return self._data.copy()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join()
