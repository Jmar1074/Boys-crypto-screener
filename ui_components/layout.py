import streamlit as st

def render_header():
    st.markdown(
        "<h1 style='text-align: center; margin-bottom: 0;'>📊 The Boys Crypto Screener</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size: 1.1em; margin-top: 0;'>Market movers • Volume trends • Real-time insights</p>",
        unsafe_allow_html=True
    )

def render_section_title(title: str):
    st.markdown(f"<h3 style='margin-top: 2em;'>{title}</h3>", unsafe_allow_html=True)

def render_divider():
    st.markdown("<hr style='margin: 1.5em 0;'>", unsafe_allow_html=True)

def render_subtext(text: str):
    st.markdown(f"<p style='font-size: 0.9em; color: gray;'>{text}</p>", unsafe_allow_html=True)
