import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="The Boys Crypto Screener", layout="wide")

if "starred" not in st.session_state:
    st.session_state.starred = []

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

def screen_coins(df):
    df = df[df["market_cap"] >= 500_000]
    df["volume_ratio"] = df["total_volume"] / (df["market_cap"] / 100)
    df = df.sort_values("market_cap", ascending=False)
    return df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "volume_ratio"]]

df_coins = get_top_coins()
filtered_df = screen_coins(df_coins)

# Update starred list live based on toggle state
for _, row in filtered_df.iterrows():
    star_key = f"star_{row['id']}"
    if star_key not in st.session_state:
        st.session_state[star_key] = row['id'] in st.session_state.starred
    elif st.session_state[star_key] and row['id'] not in st.session_state.starred:
        st.session_state.starred.append(row['id'])
    elif not st.session_state[star_key] and row['id'] in st.session_state.starred:
        st.session_state.starred.remove(row['id'])

# UI tabs
tab = st.selectbox("Navigate", ["Market Movers", "Watchlist"])

# ---- MARKET MOVERS VIEW ----
if tab == "Market Movers":
    st.markdown("## Market Movers")
    for _, row in filtered_df.iterrows():
        col1, col2, col3, col4, col5 = st.columns([1, 3, 2, 2, 1])
        with col1:
            st.text(row['symbol'].upper())
        with col2:
            st.markdown(f"**{row['name']}**")
        with col3:
            st.text(f"${row['current_price']:,.4f}")
        with col4:
            st.text(f"VR: {row['volume_ratio']:.2f}")
        with col5:
            star_key = f"star_{row['id']}"
            star_symbol = "★" if st.session_state[star_key] else "☆"
            button_color = "color: gold;" if st.session_state[star_key] else "color: white;"
            if st.button(f"{star_symbol}", key=star_key + "_btn"):
                st.session_state[star_key] = not st.session_state[star_key]

# ---- WATCHLIST VIEW ----
elif tab == "Watchlist":
    st.markdown("## Watchlist")
    starred_df = filtered_df[filtered_df["id"].isin(st.session_state.starred)]
    if not starred_df.empty:
        for _, row in starred_df.iterrows():
            st.markdown(f"""
<div style='padding:6px 12px;margin-bottom:8px;background:#111;border-radius:6px'>
    <strong style='font-size:18px'>{row['name']} ({row['symbol'].upper()})</strong><br>
    Price: ${row['current_price']:,.4f} | Volume Ratio: {row['volume_ratio']:.2f}
</div>
""", unsafe_allow_html=True)
    else:
        st.info("Your watchlist is empty.")