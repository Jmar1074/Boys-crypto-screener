import streamlit as st

def get_starred_tokens():
    """Retrieve the current list of starred tokens."""
    return st.session_state.get("starred_tokens", set())

def toggle_star(token_id):
    """
    Adds or removes a token from the starred list.
    Immediately reflects changes in the session state.
    """
    if "starred_tokens" not in st.session_state:
        st.session_state.starred_tokens = set()

    if token_id in st.session_state.starred_tokens:
        st.session_state.starred_tokens.remove(token_id)
    else:
        st.session_state.starred_tokens.add(token_id)
