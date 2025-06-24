import streamlit as st
from state.star_state import is_starred
from data_fetch.token_deep_dive import deep_dive_data
from ui_components.layout import render_divider, render_section_title

def render_watchlist(watchlist):
    if not watchlist:
        render_section_title("📁 Watchlist")
        st.info("Your watchlist is empty. Star some tokens to track them here.")
        return

    render_section_title("⭐ Watchlist")
    render_divider()

    for token in watchlist:
        if not is_starred(token['id']):
            continue

        details = deep_dive_data(token['id'])

        if details is None:
            st.warning(f"Failed to load data for {token['name']}")
            continue

        col1, col2 = st.columns([3, 2])

        with col1:
            st.markdown(
                f"<div style='padding: 0.5em 0; font-weight: bold; font-size: 1.2em;'>{token['name']} ({token['symbol'].upper()})</div>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<div style='font-size: 0.95em;'>Price: ${float(token['current_price']):,.5f}</div>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<div style='font-size: 0.95em;'>Volume: ${float(token['total_volume']):,.0f}</div>",
                unsafe_allow_html=True
            )

        with col2:
            st.metric(label="Sentiment Score", value=f"{details['sentiment_score']:.2f}")
            if details['sample_comments']:
                st.markdown("<div style='font-size: 0.85em; margin-top: 0.3em;'><b>Sample:</b> " +
                            details['sample_comments'][0] + "</div>", unsafe_allow_html=True)

        render_divider()
