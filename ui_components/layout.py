import streamlit as st
from ui_components.watchlist_view import render_watchlist_view
from ui_components.market_movers_view import render_market_movers_view

def render_main_layout(market_movers, starred_tokens, toggle_star):
    st.set_page_config(layout="wide")
    st.title("📈 Boys Crypto Screener")

    col1, col2 = st.columns([2, 1])
    with col1:
        render_market_movers_view(market_movers, toggle_star)
    with col2:
        render_watchlist_view(starred_tokens, toggle_star)
