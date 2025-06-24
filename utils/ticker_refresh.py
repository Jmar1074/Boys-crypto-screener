import time
import streamlit as st

def auto_refresh(interval_sec=60):
    """Triggers Streamlit rerun after specified interval."""
    placeholder = st.empty()
    countdown = interval_sec

    while countdown:
        placeholder.text(f"Auto-refresh in {countdown} sec...")
        time.sleep(1)
        countdown -= 1

    st.rerun()
