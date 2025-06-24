import streamlit as st
import json
import os
from utils.render_helpers import render_token_row

WATCHLIST_FILE = "assets/watchlist.json"

def load_watchlist():
    if not os.path.exists(WATCHLIST_FILE):
        return []
    with open(WATCHLIST_FILE, "r") as f:
        return json.load(f)

def save_watchlist(watchlist):
    with open(WATCHLIST_FILE, "w") as f:
        json.dump(watchlist, f)

def render_watchlist():
    st.header("⭐ Your Watchlist")
    watchlist = load_watchlist()
    if not watchlist:
        st.info("You haven't added any tokens to your watchlist yet.")
        return

    for token in watchlist:
        render_token_row(token, is_watchlist=True)
