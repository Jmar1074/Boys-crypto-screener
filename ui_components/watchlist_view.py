import streamlit as st
from render_helpers import render_token_row
from data_fetch.token_details import get_token_details
from data_fetch.sentiment import get_token_sentiment

def render_watchlist_section(watchlist):
    st.subheader("Your Watchlist")

    for token_id in watchlist:
        token_details = get_token_details(token_id)
        sentiment_score, _ = get_token_sentiment(token_id)

        if token_details:
            render_token_row(
                token=token_details,
                is_starred=True,
                sentiment_score=sentiment_score
            )
