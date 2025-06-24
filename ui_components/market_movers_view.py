import streamlit as st
from state.star_state import is_starred, toggle_star

def render_market_movers_view(market_movers, starred_tokens, toggle_star):
    st.subheader("📈 Market Movers")
    for token in market_movers:
        symbol = token.get("symbol", "").upper()
        name = token.get("name", "")
        price = token.get("price", 0)
        volume_ratio = token.get("volume_ratio", 0)

        is_favorite = is_starred(symbol, starred_tokens)
        star_icon = "⭐" if is_favorite else "☆"

        cols = st.columns([1, 2, 2, 2, 1])
        cols[0].markdown(f"**{symbol}**")
        cols[1].markdown(f"**{name}**")
        cols[2].markdown(f"${price:,.2f}")
        cols[3].markdown(f"{volume_ratio:.2f}x")
        if cols[4].button(star_icon, key=f"star-{symbol}"):
            toggle_star(symbol)
        st.markdown("---")
