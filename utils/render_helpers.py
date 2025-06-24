import streamlit as st

def render_section_title(title: str):
    st.markdown(f"<h2 style='color: #F39C12;'>{title}</h2>", unsafe_allow_html=True)

def render_divider():
    st.markdown("---")

def render_loading_message(message="Loading..."):
    st.markdown(f"<p style='color: #888;'>{message}</p>", unsafe_allow_html=True)
