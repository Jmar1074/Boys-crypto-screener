import streamlit as st
from data_fetch.coins import get_market_data
from state.star_state import is_starred
from utils.ticker_refresh import get_symbol_logo

def render_watchlist(toggle_star):
    st.markdown("## 🔖 Your Watchlist")

    tokens = get_market_data()
    watchlist = [t for t in tokens if is_starred(t.get("id", ""))]

    if not watchlist:
        st.info("Your Watchlist is currently empty.")
        return

    for token in watchlist:
        token_id = token.get("id", "")
        name = token.get("name", "N/A")
        symbol = token.get("symbol", "N/A").upper()
        price = token.get("current_price", 0.0)
        volume = token.get("total_volume", 0)

        formatted_price = f"${price:,.4f}"
        formatted_volume = f"{volume:,}"

        cols = st.columns([1.2, 2.5, 2, 2.5, 0.5])
        with cols[0]:
            logo = get_symbol_logo(symbol)
            st.image(logo, width=20) if logo else st.write(symbol)
        with cols[1]:
            st.markdown(f"**{name}**")
        with cols[2]:
            st.markdown(f"**{formatted_price}**")
        with cols[3]:
            st.markdown(f"Vol: {formatted_volume}")
        with cols[4]:
            if st.button("★", key=f"unstar-{token_id}"):
                toggle_star(token_id)
                st.rerun()
