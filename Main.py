import streamlit as st
from ui_components.layout import render_market_movers
from ui_components.watchlist_view import render_watchlist
from state.star_state import get_watchlist

# App configuration
st.set_page_config(page_title="The Boys Crypto Screener", layout="wide")

# Sidebar navigation
navigation = st.sidebar.radio("Navigate", ["Market Movers", "Watchlist"])

# Page title
st.title("🚀 The Boys Crypto Screener")

# Load and display based on navigation
if navigation == "Market Movers":
    render_market_movers()
elif navigation == "Watchlist":
    watchlist = get_watchlist()
    render_watchlist(watchlist)
