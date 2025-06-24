import streamlit as st
from ui_components.watchlist import get_watchlist_tokens
from data_fetch.token_details import get_token_details
from utils.render_helpers import render_token_row

def render_watchlist_view(starred_tokens, toggle_star_fn):
    token_ids = get_watchlist_tokens()
    if not token_ids:
        st.info("Your watchlist is empty.")
        return

    for tid in token_ids:
        details = get_token_details(tid)
        render_token_row(details, tid in starred_tokens, toggle_star_fn)
