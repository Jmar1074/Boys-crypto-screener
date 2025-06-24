import streamlit as st
from state.star_state import load_starred_tokens
from utils.render_helpers import render_section_title


def render_watchlist_view():
    render_section_title("★ Starred Tokens")
    starred_tokens = load_starred_tokens()

    if not starred_tokens:
        st.write("No tokens starred yet.")
        return

    for token in starred_tokens:
        st.markdown(f"- **{token}**")
