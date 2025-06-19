import streamlit as st
from ui_components.watchlist_view import render_watchlist
from state.star_state import get_watchlist

def render_watchlist_page():
    st.title("⭐ Your Watchlist")

    watchlist = get_watchlist()
    render_watchlist(watchlist)
