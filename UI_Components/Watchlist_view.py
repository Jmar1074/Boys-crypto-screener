import streamlit as st
from data_fetch.coins import get_market_movers
from state.star_state import toggle_watchlist, is_starred

def render_watchlist(watchlist):
    st.subheader("📌 Watchlist")

    all_coins = get_market_movers()
    tracked = [coin for coin in all_coins if coin.get("symbol", "").upper() in watchlist]

    if not tracked:
        st.info("Your watchlist is empty.")
        return

    for coin in tracked:
        symbol = coin.get("symbol", "").upper()
        name = coin.get("name", "")
        price = coin.get("price", 0)
        volume_ratio = coin.get("volume_change_ratio", "N/A")

        is_saved = is_starred(symbol)
        star = "⭐" if is_saved else "☆"

        cols = st.columns([2, 5, 3, 2, 1])
        cols[0].markdown(f"**{symbol}**")
        cols[1].markdown(name)
        cols[2].markdown(f"${price:,.4f}")
        cols[3].markdown(f"Vol Ratio: {volume_ratio}")

        if cols[4].button(star, key=f"watch_star_{symbol}"):
            toggle_watchlist(symbol)
            st.experimental_rerun()
