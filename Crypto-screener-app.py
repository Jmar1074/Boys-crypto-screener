import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="AI Crypto Screener", layout="wide")
st.title("📈 AI-Powered Crypto Screener")

# --- SESSION STATE FOR STARS ---
if "starred" not in st.session_state:
    st.session_state.starred = []

# --- SETTINGS ---
MIN_VOLUME_RATIO = 2.0
MIN_MARKET_CAP = 1_000_000
MAX_MARKET_CAP = 500_000_000

# --- API CALL ---
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

# --- SCREENING FUNCTION ---
def screen_coins(df):
    df = df[(df["market_cap"] >= MIN_MARKET_CAP) & (df["market_cap"] <= MAX_MARKET_CAP)]
    df["volume_ratio"] = df["total_volume"] / (df["market_cap"] / 100)
    df = df[df["volume_ratio"] >= MIN_VOLUME_RATIO]
    df = df.sort_values("volume_ratio", ascending=False)
    return df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "volume_ratio"]]

# --- MAIN ---
df_coins = get_top_coins()
st.write("🔍 Raw CoinGecko Data (first 5 rows):")
st.write(df_coins.head())  # Debug: verify data loading

filtered_df = screen_coins(df_coins)
st.write("✅ Filtered Results (first 5 rows):")
st.write(filtered_df.head())  # Debug: check filtering

# --- STAR FEATURE ---
st.subheader("⭐ Starred Tokens")
if st.session_state.starred:
    starred_df = filtered_df[filtered_df["id"].isin(st.session_state.starred)]
    st.dataframe(starred_df, use_container_width=True)
else:
    st.write("You have not starred any tokens yet.")

# --- ALL TOKENS TABLE ---
st.subheader("📊 Top Ranked Coins (Filtered by Market Cap & Volume Ratio)")
for _, row in filtered_df.iterrows():
    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
    with col1:
        st.write(f"**{row['name']} ({row['symbol'].upper()})**")
    with col2:
        st.write(f"Price: ${row['current_price']:.4f}")
    with col3:
        st.write(f"Volume Ratio: {row['volume_ratio']:.2f}")
    with col4:
        if row['id'] in st.session_state.starred:
            if st.button(f"⭐ Unstar {row['symbol']}", key=row['id']+"_unstar"):
                st.session_state.starred.remove(row['id'])
        else:
            if st.button(f"☆ Star {row['symbol']}", key=row['id']+"_star"):
                st.session_state.starred.append(row['id'])

# --- DETAILED VIEW ---
with st.expander("🔍 Token Deep Dive"):
    token_choice = st.selectbox("Choose a token to analyze:", filtered_df["id"])
    if token_choice:
        info_url = f"https://api.coingecko.com/api/v3/coins/{token_choice}"
        info_data = requests.get(info_url).json()

        st.markdown(f"### {info_data['name']} ({info_data['symbol'].upper()})")
        st.write("**Current Price:** $", info_data['market_data']['current_price']['usd'])
        st.write("**Market Cap:** $", info_data['market_data']['market_cap']['usd'])
        st.write("**24h Volume:** $", info_data['market_data']['total_volume']['usd'])
        st.write("**Circulating Supply:**", info_data['market_data']['circulating_supply'])
        st.write("**Total Supply:**", info_data['market_data']['total_supply'])

        st.write("**Description:**")
        st.markdown(info_data['description']['en'][:600] + "...")

