import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="The Boys Crypto Screener", layout="wide")

# Initialize starred list
if "starred" not in st.session_state:
    st.session_state.starred = []

# Load top coins from CoinGecko
@st.cache_data(ttl=60)
def get_top_coins():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False
    }
    r = requests.get(url, params=params)
    return pd.DataFrame(r.json())

# Load chart data for token
@st.cache_data(ttl=300)
def get_candle_data(symbol="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
    params = {"vs_currency": "usd", "days": 7, "interval": "daily"}
    r = requests.get(url, params=params)
    if r.status_code == 200:
        prices = r.json()['prices']
        df = pd.DataFrame(prices, columns=['time', 'price'])
        df['time'] = pd.to_datetime(df['time'], unit='ms')
        df['price'] = df['price'].astype(float)
        return df
    return pd.DataFrame()

# Screen coins by market cap and add volume ratio
def screen_coins(df):
    df = df[df["market_cap"] >= 500_000]
    df["volume_ratio"] = df["total_volume"] / (df["market_cap"] / 100)
    df = df.sort_values("market_cap", ascending=False)
    return df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "volume_ratio"]]

# Load coin data
df_coins = get_top_coins()
filtered_df = screen_coins(df_coins)

# Handle all star/unstar actions before displaying
for _, row in filtered_df.iterrows():
    star_key = row['id'] + "_star"
    unstar_key = row['id'] + "_unstar"

    if st.session_state.get(star_key):
        if row['id'] not in st.session_state.starred:
            st.session_state.starred.append(row['id'])
        st.session_state[star_key] = False

    if st.session_state.get(unstar_key):
        if row['id'] in st.session_state.starred:
            st.session_state.starred.remove(row['id'])
        st.session_state[unstar_key] = False

# Main UI Tabs
tab = st.selectbox("Navigate", ["Market Movers", "Watchlist"])

# --- Market Movers View ---
if tab == "Market Movers":
    st.markdown("## Market Movers")
    for _, row in filtered_df.iterrows():
        with st.container():
            cols = st.columns([3, 2, 2, 2])
            with cols[0]:
                st.markdown(f"**{row['name']} ({row['symbol'].upper()})**")
            with cols[1]:
                st.markdown(f"Price: **${row['current_price']:.4f}**")
            with cols[2]:
                st.markdown(f"Volume Ratio: {row['volume_ratio']:.2f}")
            with cols[3]:
                key = row['id'] + ("_unstar" if row['id'] in st.session_state.starred else "_star")
                label = "Unstar" if row['id'] in st.session_state.starred else "Star"
                st.checkbox(label, key=key)

# --- Watchlist View ---
elif tab == "Watchlist":
    st.markdown("## Watchlist")
    starred_df = filtered_df[filtered_df["id"].isin(st.session_state.starred)]

    if not starred_df.empty:
        for _, row in starred_df.iterrows():
            with st.container():
                st.markdown(f"""
                <div style="padding: 8px 12px; margin-bottom: 10px; background-color: #111111; border-radius: 6px;">
                    <div style="font-size: 20px; font-weight: bold;">{row['name']} ({row['symbol'].upper()})</div>
                    <div style="font-size: 16px;">Price: ${row['current_price']:.4f}</div>
                    <div style="font-size: 16px;">Volume Ratio: {row['volume_ratio']:.2f}</div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("Your watchlist is currently empty.")