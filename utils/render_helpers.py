import streamlit as st

def render_section_header(title):
    st.markdown(f"## {title}", unsafe_allow_html=True)

def render_metric(label, value, delta=None):
    if delta is not None:
        st.metric(label=label, value=value, delta=delta)
    else:
        st.metric(label=label, value=value)

def render_data_table(data_dict):
    if not data_dict:
        st.warning("No data available.")
        return
    for key, value in data_dict.items():
        st.write(f"**{key.capitalize()}**: {value}")
