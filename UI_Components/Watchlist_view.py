import streamlit as st
from data_fetch.coins import get_token_list
from state.star_state import get_starred_tokens

def show_watchlist():
    tokens = get_token_list()
    watchlist = get_starred_tokens()

    if not watchlist:
        st.info("⭐ Your watchlist is currently empty.")
        return

    st.markdown("<h3 style='margin-bottom: 10px;'>📌 Watchlist</h3>", unsafe_allow_html=True)

    for token in tokens:
        symbol = token.get("symbol", "")
        if symbol not in watchlist:
            continue

        name = token.get("name", "")
        price = token.get("price", 0)
        volume = token.get("volume", 0)

        cols = st.columns([0.4, 0.3, 0.3])
        cols[0].markdown(f"<div style='font-weight:600; font-size:17px;'>{symbol} — {name}</div>", unsafe_allow_html=True)
        cols[1].markdown(f"<div style='font-size:16px;'>${price:,.4f}</div>", unsafe_allow_html=True)
        cols[2].markdown(f"<div style='font-size:16px;'>Vol: {volume:,.2f}</div>", unsafe_allow_html=True)
