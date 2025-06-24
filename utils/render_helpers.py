import streamlit as st

def render_section_title(title):
    st.markdown(f"## {title}")

def render_divider():
    st.markdown("---")

def render_star_icon(symbol, active, toggle_fn):
    label = "★" if active else "☆"
    if st.button(label, key=f"star_{symbol}"):
        toggle_fn(symbol)

def render_token_row(token, starred, toggle_fn):
    symbol = token.get("symbol", "")
    name   = token.get("name", "")
    price  = token.get("price", 0)

    cols = st.columns([1, 4, 2])
    with cols[0]:
        render_star_icon(symbol, starred, toggle_fn)
    with cols[1]:
        st.write(f"{name} ({symbol})")
    with cols[2]:
        st.write(f"${price:,.2f}")
