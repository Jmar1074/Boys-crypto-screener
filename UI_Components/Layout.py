import streamlit as st
from data_fetch.coins import get_token_list
from state.star_state import is_starred, toggle_star

def show_market_movers():
    tokens = get_token_list()

    if not tokens:
        st.warning("⚠️ No market data available.")
        return

    for token in tokens:
        name = token.get('name', '')
        symbol = token.get('symbol', '')
        price = token.get('price', 0)
        volume = token.get('volume', 0)

        is_favorited = is_starred(symbol)
        star_icon = "★" if is_favorited else "☆"

        cols = st.columns([0.1, 0.4, 0.25, 0.2, 0.05])
        cols[0].markdown("🔄")  # Placeholder for future logo/symbol
        cols[1].markdown(f"**{symbol}** — {name}")
        cols[2].markdown(f"${price:,.4f}")
        cols[3].markdown(f"Vol: {volume:,.2f}")
        if cols[4].button(star_icon, key=f"star-{symbol}"):
            toggle_star(symbol)
            st.experimental_rerun()
