import streamlit as st
from data_fetch.coins import get_market_data
from state.star_state import is_starred

def render_main_layout(toggle_star, get_starred_tokens):
    tokens = get_market_data()
    if not tokens:
        st.warning("No token data found.")
        return

    st.markdown("### Top Market Movers")
    for token in tokens:
        token_id = token.get("id", "")
        name = token.get("name", "N/A")
        symbol = token.get("symbol", "N/A").upper()
        price = token.get("current_price", 0.0)
        volume = token.get("total_volume", 0)

        # Format values
        formatted_price = f"${price:,.4f}"
        formatted_volume = f"{volume:,}"

        # Compact row layout
        cols = st.columns([1.2, 2.5, 2, 2.5, 0.5])
        with cols[0]:
            st.write(symbol)
        with cols[1]:
            st.markdown(f"**{name}**")
        with cols[2]:
            st.write(formatted_price)
        with cols[3]:
            st.write(f"Vol: {formatted_volume}")
        with cols[4]:
            starred = is_starred(token_id)
            star_label = "★" if starred else "☆"
            if st.button(star_label, key=f"star-{token_id}"):
                toggle_star(token_id)
                st.rerun()
