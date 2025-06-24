import requests
import streamlit as st

@st.cache_data(ttl=300)
def fetch_market_movers():
    try:
        url = "https://api.coingecko.com/api/v3/search/trending"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("coins", [])
    except Exception as e:
        st.error(f"Error fetching market movers: {e}")
        return []

@st.cache_data(ttl=300)
def get_top_movers():
    return fetch_market_movers()

@st.cache_data(ttl=300)
def get_token_by_id(token_id):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{token_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None

@st.cache_data(ttl=600)
def get_all_tokens():
    try:
        url = "https://api.coingecko.com/api/v3/coins/list"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()  # list of token dictionaries with id, name, symbol
    except Exception as e:
        st.error(f"Error fetching all tokens: {e}")
        return []
