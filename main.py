import streamlit as st
from ui_components.layout import render_main_layout
from data_fetch.coins import fetch_market_movers
from state.star_state import load_starred_tokens, toggle_star
from utils.ticker_refresh import background_token_refresher

# Kick off periodic data refresh (every 60s)
background_token_refresher(interval=60)

st.set_page_config(page_title="Crypto Screener", layout="wide")

starred = load_starred_tokens()
movers = fetch_market_movers()

render_main_layout(movers, starred, toggle_star)
