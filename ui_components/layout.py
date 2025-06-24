import streamlit as st
from ui_components.watchlist_view import display_watchlist
from state.star_state import toggle_star, is_starred
from data_fetch.coins import get_top_movers
from utils.render_helpers import render_section_header


def render_market_movers():
    render_section_header("🔥 Market Movers")
    top_movers = get_top_movers()

    for token in top_movers:
        name = token.get("name", "Unknown")
        symbol = token.get("symbol", "???")
        price = token.get("price")
        volume_ratio = token.get("volume_ratio", "N/A")
        token_id = token.get("id", "")

        price_display = f"${price:,.2f}" if isinstance(price, (int, float)) else price or "N/A"

        cols = st.columns([6, 3, 3, 1])  # Ticker | Price | Volume | Star

        with cols[0]:
            st.markdown(f"**{symbol}** {name}")
        with cols[1]:
            st.markdown(price_display)
        with cols[2]:
            st.markdown(f"VR: {volume_ratio}")
        with cols[3]:
            star_status = is_starred(token_id)
            star_label = "⭐" if star_status else "☆"
            if st.button(star_label, key=f"star_{token_id}"):
                toggle_star(token_id)


def render_layout():
    st.set_page_config(page_title="Crypto Screener", layout="wide")
    st.title("📊 Crypto Screener")

    tabs = st.tabs(["Market Movers", "Watchlist"])

    with tabs[0]:
        render_market_movers()

    with tabs[1]:
        display_watchlist()
