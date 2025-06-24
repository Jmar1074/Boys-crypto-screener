import streamlit as st
from ui_components.watchlist_view import render_watchlist_view

def render_main_layout(market_movers, starred_tokens, toggle_star):
    st.set_page_config(page_title="Crypto Screener", layout="wide")

    st.title("📈 Crypto Market Screener")
    
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Top Market Movers")
        for token in market_movers:
            name = token.get("name", "N/A")
            symbol = token.get("symbol", "N/A")
            price = token.get("price", "N/A")
            volume_ratio = token.get("volume_ratio", "N/A")

            row = f"**{symbol}** {name} — ${price:,} | VR: {volume_ratio:.2f}"
            is_starred = symbol in starred_tokens
            star_label = "★" if is_starred else "☆"

            col_star, col_data = st.columns([0.1, 0.9])
            if col_star.button(star_label, key=symbol):
                toggle_star(symbol)
            col_data.markdown(row)

    with col2:
        st.subheader("⭐ Watchlist")
        render_watchlist_view(starred_tokens)
