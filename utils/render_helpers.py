import streamlit as st

def render_section_header(title, icon="📊"):
    st.markdown(f"### {icon} {title}", unsafe_allow_html=True)

def render_divider():
    st.markdown("---")

def render_error_message(message):
    st.error(message)

def render_info_message(message):
    st.info(message)

def render_success_message(message):
    st.success(message)

def render_warning_message(message):
    st.warning(message)

def render_chip(text, color="#1f77b4"):
    st.markdown(
        f"<span style='background-color:{color}; color:white; padding:4px 8px; border-radius:12px; font-size:0.9em;'>{text}</span>",
        unsafe_allow_html=True,
    )

def render_badge(label, value, color="#10b981"):
    st.markdown(
        f"<span style='display:inline-block; padding:4px 10px; background:{color}; color:white; border-radius:8px; margin:2px; font-size:0.8em;'>"
        f"<strong>{label}:</strong> {value}</span>",
        unsafe_allow_html=True,
    )
