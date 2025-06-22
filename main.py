import streamlit as st
from ui_components.layout import render_main_layout
from data_fetch.coins import fetch_market_movers
from state.star_state import load_starred_tokens, toggle_star
from utils.ticker_refresh import background_token_refresher

background_token_refresher()

st.set_page_config(page_title="The Boys Crypto Screener", layout="wide")

st.markdown(
    "<h1 style='text-align: center; font-size: 40px;'>The Boys Crypto Screener</h1>",
    unsafe_allow_html=True
)

starred_tokens = load_starred_tokens()
market_movers = fetch_market_movers()

render_main_layout(market_movers, starred_tokens, toggle_star)
