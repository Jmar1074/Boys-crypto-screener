import streamlit as st
from state.star_state import get_starred_tokens
from data_fetch.coins import get_top_coins

def render_watchlist():
    st.markdown("## ⭐ Watchlist")

    starred = get_starred_tokens()
    if not starred:
        st.info("You haven't added any tokens to your Watchlist yet.")
        return

    # Fetch latest data
    df = get_top_coins()
    df = df[df["id"].isin(starred)]

    if df.empty:
        st.warning("No matching tokens found. Try refreshing or starring some again.")
        return

    # Format and display
    for _, row in df.iterrows():
        st.markdown(
            f"""
            <div style="display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid #333;">
                <span><b>{row['name']} ({row['symbol'].upper()})</b></span>
                <span>💲 {row['current_price']:,.4f}</span>
                <span>📈 Vol: {row['total_volume']:,.0f}</span>
