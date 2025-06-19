import streamlit as st
from ui_components.layout import render_main_layout
from ui_components.watchlist_view import render_watchlist
from state.star_state import toggle_star, get_starred_tokens
from data_fetch.token_deep_dive import deep_dive_data
from assets.ticker_refresh import refresh_ticker_data

# Optional future fallback hooks (disabled but reserved)
from utils.fallback_request import try_sources

# --- App Configuration ---
st.set_page_config(
    page_title="The Boys Crypto Screener",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Top Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Market Screener", "Watchlist"])

# --- Background Ticker Refresh (auto-run later) ---
refresh_ticker_data()

# --- Market Screener View ---
if page == "Market Screener":
    st.title("📊 Market Movers")
    render_main_layout(toggle_star, get_starred_tokens)

# --- Watchlist View ---
elif page == "Watchlist":
    st.title("⭐ Your Watchlist")
    starred_tokens = get_starred_tokens()
    if starred_tokens:
        render_watchlist(starred_tokens, deep_dive_data)
    else:
        st.info("Your watchlist is currently empty.")

# --- Optional Hooks (Future Feature: Auto News + Twitter Sentiment Feed) ---
if False:
    try_sources("bitcoin", fallback=True)
