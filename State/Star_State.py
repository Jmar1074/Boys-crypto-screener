import streamlit as st

def initialize_star_state():
    if "starred" not in st.session_state:
        st.session_state.starred = []
