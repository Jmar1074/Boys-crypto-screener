import requests, time

def fallback_request(url, method="get", retries=3, backoff=1, **kwargs):
    for attempt in range(1, retries + 1):
        try:
            resp = getattr(requests, method.lower())(url, **kwargs)
            resp.raise_for_status()
            return resp
        except Exception:
            if attempt == retries:
                raise
            time.sleep(backoff * attempt)
