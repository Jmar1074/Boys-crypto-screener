import streamlit as st

def _init_star_state():
    if "starred_tokens" not in st.session_state:
        st.session_state["starred_tokens"] = set()

def get_starred():
    _init_star_state()
    return st.session_state["starred_tokens"]

def is_starred(token_id):
    _init_star_state()
    return token_id in st.session_state["starred_tokens"]

def toggle_star(token_id):
    _init_star_state()
    if token_id in st.session_state["starred_tokens"]:
        st.session_state["starred_tokens"].remove(token_id)
    else:
        st.session_state["starred_tokens"].add(token_id)
