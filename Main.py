import streamlit as st
import threading

from ui_components.layout import show_market_movers
from ui_components.watchlist_view import show_watchlist
from utils.background_refresh import start_refresh_loop
from state.star_state import init_star_state

if 'page' not in st.session_state:
    st.session_state.page = 'Market Movers'
init_star_state()

st.sidebar.title("📊 The Boys Crypto Screener")
page_choice = st.sidebar.radio("Navigate to:", ["Market Movers", "Watchlist"])
st.session_state.page = page_choice

if 'refresh_thread_started' not in st.session_state:
    threading.Thread(target=start_refresh_loop, daemon=True).start()
    st.session_state.refresh_thread_started = True

if st.session_state.page == 'Market Movers':
    show_market_movers()
elif st.session_state.page == 'Watchlist':
    show_watchlist()
