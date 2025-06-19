import streamlit as st
from ui_components.layout import render_market_movers
from ui_components.watchlist_view import render_watchlist
from state.star_state import sync_starred_tokens
from data_fetch.coingecko_api import get_filtered_tokens

st.set_page_config(page_title="The Boys Crypto Screener", layout="wide")

# Sync toggle logic for starred tokens
filtered_df = get_filtered_tokens()
sync_starred_tokens(filtered_df)

# Navigation
tab = st.selectbox("Navigate", ["Market Movers", "Watchlist"])

if tab == "Market Movers":
    render_market_movers(filtered_df)

elif tab == "Watchlist":
    render_watchlist(filtered_df)
