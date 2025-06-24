import streamlit as st
from ui_components.watchlist_view import render_watchlist_view
from ui_components.render_helpers import render_divider, render_section_title
from data_fetch.coins import get_top_movers
from state.star_state import toggle_star, is_starred


def render_market_movers():
    render_section_title("📈 Market Movers")

    movers = get_top_movers()
    for token in movers:
        with st.container():
            cols = st.columns([2, 5, 3, 2, 1])
            cols[0].write(token.get("symbol", "").upper())
            cols[1].markdown(f"**{token.get('name', 'N/A')}**")
            cols[2].write(f"${token.get('price', 0):,.4f}")
            cols[3].write(f"{token.get('volume_ratio', 0):.2f}x")

            starred = is_starred(token["id"])
            star_button = "★" if starred else "☆"
            if cols[4].button(star_button, key=f"star_{token['id']}"):
                toggle_star(token["id"])

    render_divider()


def render_main_layout():
    st.set_page_config(page_title="Crypto Screener", layout="wide")
    st.title("🚀 Boys Crypto Screener")

    render_market_movers()
    render_watchlist_view()
