import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

st.set_page_config(page_title="The Boys Crypto Screener", layout="wide")
st.title("🧠 The Boys Crypto Screener")

if "starred" not in st.session_state:
    st.session_state.starred = []

MIN_MARKET_CAP = 500_000

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

def screen_coins(df):
    df = df[df["market_cap"] >= MIN_MARKET_CAP]
    df["volume_ratio"] = df["total_volume"] / (df["market_cap"] / 100)
    df = df.sort_values("market_cap", ascending=False)
    return df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "volume_ratio"]]

df_coins = get_top_coins()
filtered_df = screen_coins(df_coins)

st.subheader("🚀 Watchlist: Starred Tokens")
if st.session_state.starred:
    starred_df = filtered_df[filtered_df["id"].isin(st.session_state.starred)]
    st.dataframe(starred_df, use_container_width=True)
else:
    st.info("No tokens starred yet. Scroll below and ⭐ to track them here.")

st.subheader("📊 Ranked Market Movers")
for _, row in filtered_df.iterrows():
    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
    with col1:
        st.write(f"**{row['name']} ({row['symbol'].upper()})**")
    with col2:
        st.write(f"💵 Price: ${row['current_price']:.4f}")
    with col3:
        st.write(f"📈 Volume Ratio: {row['volume_ratio']:.2f}")
    with col4:
        if row['id'] in st.session_state.starred:
            if st.button(f"Unstar {row['symbol']} ⭐", key=row['id']+"_unstar"):
                st.session_state.starred.remove(row['id'])
        else:
            if st.button(f"Star {row['symbol']} ☆", key=row['id']+"_star"):
                st.session_state.starred.append(row['id'])

with st.expander("🔎 Token Deep Dive"):
    token_choice = st.selectbox("Choose a token:", filtered_df["id"])
    if token_choice:
        info_url = f"https://api.coingecko.com/api/v3/coins/{token_choice}"
        info_data = requests.get(info_url).json()

        st.markdown(f"### {info_data['name']} ({info_data['symbol'].upper()})")
        st.write("💰 **Price:** $", info_data['market_data']['current_price']['usd'])
        st.write("🏦 **Market Cap:** $", info_data['market_data']['market_cap']['usd'])
        st.write("🔄 **24h Volume:** $", info_data['market_data']['total_volume']['usd'])
        st.write("📦 **Circulating Supply:**", info_data['market_data']['circulating_supply'])
        st.write("📦 **Total Supply:**", info_data['market_data']['total_supply'])

        chart_df = get_candle_data(token_choice)
        if not chart_df.empty:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=chart_df['time'], y=chart_df['price'], mode='lines+markers', name='Price'))
            fig.update_layout(title='📉 7-Day Price Trend', xaxis_title='Date', yaxis_title='USD')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No chart data available.")