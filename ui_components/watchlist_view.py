import streamlit as st
from data_fetch.coins import get_token_by_id
from state.star_state import get_starred_tokens
from ui_components.render_helpers import render_divider, render_section_title
from utils.token_lookup import get_token_by_id


def render_watchlist_view():
    watchlist = get_starred_tokens()
    if not watchlist:
        return

    render_divider()
    render_section_title("⭐ Watchlist")

    for token_id in watchlist:
        token = get_token_by_id(token_id)
        if token:
            cols = st.columns([2, 5, 3, 2])
            cols[0].write(token.get("symbol", "").upper())
            cols[1].markdown(f"**{token.get('name', 'N/A')}**")
            cols[2].write(f"${token.get('price', 0):,.4f}")
            cols[3].write(f"{token.get('volume_ratio', 0):.2f}x")
