import streamlit as st
from utils.render_helpers import render_star_icon


def render_watchlist(watchlist_data):
    st.subheader("📌 Your Watchlist")

    if not watchlist_data:
        st.info("Your watchlist is currently empty.")
        return

    for token in watchlist_data:
        col1, col2 = st.columns([9, 1])
        with col1:
            st.write(f"**{token['name']}** — ${token['price']:,}")
        with col2:
            render_star_icon(token['symbol'], active=True)
