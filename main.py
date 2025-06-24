import streamlit as st

from ui_components.layout import render_main_layout
from utils.ticker_refresh import refresh_token_data

st.set_page_config(
    page_title="Crypto Screener",
    page_icon="💹",
    layout="wide"
)

if "refresh_state" not in st.session_state:
    st.session_state.refresh_state = False

st.title("📊 Crypto Screener Dashboard")

with st.sidebar:
    refresh = st.button("🔄 Refresh Tokens")
    if refresh:
        st.session_state.refresh_state = True
        refresh_token_data()
        st.success("Token data refreshed.")

# Render the main layout (UI)
render_main_layout()
