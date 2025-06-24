import streamlit as st
from ui_components.render_helpers import render_token_row
from utils.watchlist import load_watchlist
from data_fetch.token_details import get_token_details

def render_watchlist_view():
    st.header("★ Watchlist")

    watchlist = load_watchlist()
    if not watchlist:
        st.info("Your watchlist is empty.")
        return

    for token_id in watchlist:
        try:
            details = get_token_details(token_id)
            if details:
                render_token_row(details)
        except Exception as e:
            st.error(f"Error loading {token_id}: {str(e)}")
