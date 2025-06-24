import streamlit as st
from ui_components.market_movers_view import render_market_movers_view
from ui_components.watchlist_view import render_watchlist_view
from data_fetch.token_details import get_token_details

def render_main_layout(market_movers, starred_tokens, toggle_star):
    col1, col2 = st.columns([2, 1])

    token_details = {}
    for token in market_movers:
        token_id = token.get("id")
        if token_id:
            details = get_token_details(token_id)
            if details:
                token_details[token_id] = details

    with col1:
        render_market_movers_view(market_movers, token_details, toggle_star)

    with col2:
        render_watchlist_view(starred_tokens, toggle_star)
