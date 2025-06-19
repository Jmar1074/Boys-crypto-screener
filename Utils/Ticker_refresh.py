import time
import threading

# Global toggle for refresh loop
refresh_loop_running = False

def start_refresh_loop(callback, interval=60):
    """
    Starts a background thread that triggers the provided callback at a set interval.
    Use this to refresh data, graphs, etc.
    """
    global refresh_loop_running
    refresh_loop_running = True

    def loop():
        while refresh_loop_running:
            try:
                callback()
            except Exception:
                pass
            time.sleep(interval)

    threading.Thread(target=loop, daemon=True).start()


def stop_refresh_loop():
    """
    Stops the background refresh loop.
    Useful for freeing up resources or manually triggering state changes.
    """
    global refresh_loop_running
    refresh_loop_running = False
