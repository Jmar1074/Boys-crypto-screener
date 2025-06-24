import streamlit as st
from ui_components.watchlist_view import render_watchlist_view
from utils.render_helpers import render_section_title


def render_main_layout():
    st.set_page_config(page_title="Crypto Screener", layout="wide")
    render_section_title("📈 Market Movers & Watchlist")
    render_watchlist_view()
