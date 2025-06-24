import streamlit as st
from ui_components.watchlist import render_watchlist_section
from ui_components.watchlist_view import render_watchlist_view

def render_main_layout(tokens, starred_tokens, on_star_toggle):
    st.set_page_config(layout="wide")
    st.title("📈 Boys Crypto Screener")

    st.markdown("---")

    col1, col2 = st.columns([4, 1], gap="large")

    with col1:
        for token in tokens:
            row = st.container()
            with row:
                token_symbol = token.get("symbol", "").upper()
                token_name = token.get("name", "Unknown")
                token_price = token.get("price", 0)
                token_volume = token.get("volume", 0)

                st.markdown(
                    f"<div style='display:flex; justify-content:space-between; align-items:center;'>"
                    f"<span style='font-weight:bold;'>{token_symbol} — {token_name}</span>"
                    f"<span>${token_price:,.4f}</span>"
                    f"<span>Vol: {token_volume:,}</span>"
                    f"<span style='cursor:pointer;'>{'⭐' if token.get('starred') else '☆'}</span>"
                    f"</div>",
                    unsafe_allow_html=True
                )

                star_button_key = f"star_{token_symbol}"
                if st.button("★" if token.get("starred") else "☆", key=star_button_key):
                    on_star_toggle(token)

                st.markdown("<hr>", unsafe_allow_html=True)

    with col2:
        render_watchlist_section(starred_tokens, on_star_toggle)
        render_watchlist_view(starred_tokens)
