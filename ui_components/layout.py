import streamlit as st
from ui_components.watchlist_view import render_watchlist_section
from ui_components.token_overview import render_token_overview
from ui_components.sentiment_section import render_sentiment_section
from state.star_state import get_watchlist_tokens

def render_main_layout():
    tabs = st.tabs(["🔥 Market Movers", "⭐ Watchlist", "📈 Sentiment Analysis"])

    with tabs[0]:
        render_token_overview()

    with tabs[1]:
        watchlist = get_watchlist_tokens()
        if not watchlist:
            st.info("No tokens in your watchlist yet. Click the star ⭐ to add some.")
        else:
            render_watchlist_section(watchlist)

    with tabs[2]:
        render_sentiment_section()
