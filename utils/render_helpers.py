import streamlit as st

def render_token_row(token):
    st.markdown(
        f"""
        <div style="display: flex; justify-content: space-between; padding: 0.5rem; border-bottom: 1px solid #444;">
            <div><strong>{token.get("symbol", "N/A")}</strong> — {token.get("name", "Unnamed")}</div>
            <div>${token.get("price", "0.00")}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
