watchlist_view.py — Clean and Modern Watchlist View

import streamlit as st import pandas as pd from state.star_state import get_starred_tokens from data_fetch.coins import fetch_top_tokens

def display_watchlist(): st.subheader("⭐ Watchlist")

starred_ids = get_starred_tokens()
if not starred_ids:
    st.info("Your watchlist is empty. Star tokens to add them here.")
    return

all_data = fetch_top_tokens()
watchlist_df = all_data[all_data['id'].isin(starred_ids)]

if watchlist_df.empty:
    st.warning("No matching data for your starred tokens.")
    return

st.markdown("<style> .watch-row { padding: 6px 0; font-size: 17px; font-weight: 600; } .watch-col { display: inline-block; width: 22%; } .watch-header { border-bottom: 1px solid #444; margin-bottom: 10px; font-weight: bold; font-size: 18px; } </style>", unsafe_allow_html=True)

st.markdown("""
<div class='watch-header'>
    <span class='watch-col'>Symbol</span>
    <span class='watch-col'>Name</span>
    <span class='watch-col'>Price</span>
    <span class='watch-col'>Volume Ratio</span>
</div>
""", unsafe_allow_html=True)

for _, row in watchlist_df.iterrows():
    symbol = row['symbol'].upper()
    name = row['name']
    price = f"${row['current_price']:,.4f}"
    volume = f"{row['volume_ratio']:.2f}x"

    st.markdown(f"""
    <div class='watch-row'>
        <span class='watch-col'>{symbol}</span>
        <span class='watch-col'>{name}</span>
        <span class='watch-col'>{price}</span>
        <span class='watch-col'>{volume}</span>
    </div>
    """, unsafe_allow_html=True)

