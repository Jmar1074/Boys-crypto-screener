import streamlit as st

def render_watchlist_section(starred_tokens, on_star_toggle):
    st.subheader("⭐ Your Watchlist")
    if not starred_tokens:
        st.info("No tokens starred yet. Use the ★ icon to add.")
        return

    for token in starred_tokens:
        col1, col2 = st.columns([8, 1])
        with col1:
            st.write(f"{token['name']} ({token['symbol']}) - ${token['price']:,.2f}")
        with col2:
            star = "★"
            if st.button(star, key=f"remove_star_{token['id']}"):
                on_star_toggle(token['id'])
