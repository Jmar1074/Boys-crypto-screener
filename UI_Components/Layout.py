layout.py — Redesigned Market Movers UI Layout

import streamlit as st import pandas as pd from state.star_state import toggle_star, is_starred

def display_market_movers(df): st.subheader("📈 Market Movers")

if df.empty:
    st.warning("No data available.")
    return

# Custom compressed ticker-style layout
for _, row in df.iterrows():
    token_id = row['id']
    symbol = row['symbol'].upper()
    name = row['name']
    price = f"${row['current_price']:,.4f}"
    volume_ratio = f"{row['volume_ratio']:.2f}x"

    cols = st.columns([1, 2.5, 2, 2, 0.7])

    with cols[0]:
        st.markdown(f"**{symbol}**", unsafe_allow_html=True)
    with cols[1]:
        st.markdown(f"<span style='font-weight:600;font-size:16px'>{name}</span>", unsafe_allow_html=True)
    with cols[2]:
        st.markdown(f"<span style='font-size:16px'>{price}</span>", unsafe_allow_html=True)
    with cols[3]:
        st.markdown(f"<span style='font-size:16px'>{volume_ratio}</span>", unsafe_allow_html=True)
    with cols[4]:
        starred = is_starred(token_id)
        if st.button("★" if starred else "☆", key=f"star_{token_id}"):
            toggle_star(token_id)
            st.experimental_rerun()

st.markdown("---")

