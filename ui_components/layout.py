import streamlit as st
from ui_components.market_movers_view import render_market_movers_view
from ui_components.watchlist_view import render_watchlist_view
from utils.render_helpers import render_section_title, render_divider

def render_main_layout(market_movers, starred_tokens, toggle_star_fn):
    st.set_page_config(layout="wide")

    # Market movers section
    render_section_title("🚀 Market Movers")
    col1, col2 = st.columns([2, 1])
    with col1:
        render_market_movers_view(market_movers, starred_tokens, toggle_star_fn)

    # Watchlist section
    with col2:
        render_divider()
        render_section_title("📌 Watchlist")
        render_watchlist_view(starred_tokens, toggle_star_fn)
