import streamlit as st
import pandas as pd
from state.star_state import toggle_star, is_starred
from utils.render_helpers import render_section_header


def display_watchlist(watchlist_data):
    """Render the user's starred token watchlist."""
    render_section_header("⭐ Starred Watchlist")

    if not watchlist_data:
        st.info("No tokens have been starred yet.")
        return

    # Format the data into a DataFrame
    df = pd.DataFrame(watchlist_data)

    # Display as table with watch/unwatch actions
    for _, row in df.iterrows():
        cols = st.columns([3, 2, 2, 1])
        token_name = f"**{row['name']} ({row['symbol']})**"
        price = f"${row['price']:,.4f}"
        volume_ratio = f"{row['volume_ratio']:.2f}"

        cols[0].markdown(token_name)
        cols[1].markdown(price)
        cols[2].markdown(volume_ratio)

        # Star toggle
        starred = is_starred(row["symbol"])
        if cols[3].button("★" if starred else "☆", key=f"star-{row['symbol']}"):
            toggle_star(row["symbol"])
