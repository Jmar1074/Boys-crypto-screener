import streamlit as st
from utils.is_starred import is_starred
from utils.render_helpers import render_star_icon

def render_market_movers_view(movers, starred_tokens, toggle_star_fn):
    # Header row
    headers = ["★", "Symbol", "Name", "Price", "VR"]
    cols = st.columns([1, 2, 2, 2, 1])
    for col, h in zip(cols, headers):
        with col:
            st.write(f"**{h}**")

    # Data rows
    for token in movers:
        symbol = token["symbol"]
        name = token.get("name", "")
        price = token.get("price", 0)
        vr = token.get("volume_ratio", 0)

        cols = st.columns([1, 2, 2, 2, 1])
        with cols[0]:
            render_star_icon(symbol, is_starred(symbol, starred_tokens), toggle_star_fn)
        with cols[1]:
            st.write(symbol)
        with cols[2]:
            st.write(name)
        with cols[3]:
            st.write(f"${price:,.2f}")
        with cols[4]:
            st.write(f"{vr:.2f}")
