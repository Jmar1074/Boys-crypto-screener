import streamlit as st
import pandas as pd

def render_watchlist(filtered_df):
    st.subheader("👁️‍🗨️ Watchlist")

    watchlist_df = filtered_df[filtered_df["id"].isin(st.session_state.starred)]

    if watchlist_df.empty:
        st.info("Your watchlist is empty. Go star some tokens on the Market Movers tab!")
        return

    styled_df = watchlist_df[["symbol", "name", "current_price", "total_volume", "volume_ratio"]].copy()
    styled_df.columns = ["Symbol", "Name", "Price (USD)", "24h Volume", "Volume Ratio"]

    # Format values
    styled_df["Price (USD)"] = styled_df["Price (USD)"].apply(lambda x: f"${x:,.4f}")
    styled_df["24h Volume"] = styled_df["24h Volume"].apply(lambda x: f"${x:,.0f}")
    styled_df["Volume Ratio"] = styled_df["Volume Ratio"].apply(lambda x: f"{x:.2f}")

    # Display table with larger font and no visible borders
    st.markdown(
        styled_df.style
        .set_properties(**{
            "font-size": "16px",
            "font-weight": "bold",
            "border": "none",
            "text-align": "left"
        })
        .hide(axis="index")
        .to_html(), unsafe_allow_html=True
    )
