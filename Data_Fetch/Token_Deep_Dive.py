import streamlit as st
from data_fetch.token_details import get_token_details, get_token_chart
from data_fetch.sentiment import get_token_sentiment
import plotly.graph_objects as go

def render_token_deep_dive(token_id):
    token = get_token_details(token_id)
    if not token:
        st.warning("Failed to load token details.")
        return

    st.markdown(f"## {token['name']} ({token['symbol'].upper()})")

    market = token.get("market_data", {})
    if market:
        st.write(f"💵 **Price:** ${market['current_price']['usd']:,.4f}")
        st.write(f"🏦 **Market Cap:** ${market['market_cap']['usd']:,.0f}")
        st.write(f"🔄 **24h Volume:** ${market['total_volume']['usd']:,.0f}")
        st.write(f"📦 **Circulating Supply:** {market['circulating_supply']:,}")
        if market['total_supply']:
            st.write(f"📦 **Total Supply:** {market['total_supply']:,}")

    # Sentiment analysis from Reddit
    sentiment_score, top_comments = get_token_sentiment(token["name"])
    st.write(f"💬 **Reddit Sentiment Score:** {sentiment_score}")
    for comment in top_comments:
        st.caption(f"🗣️ {comment[:120]}...")

    # Chart
    chart_df = get_token_chart(token_id)
    if not chart_df.empty:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=chart_df['time'], y=chart_df['price'], mode='lines+markers', name='Price'))
        fig.update_layout(
            title='7-Day Price Trend',
            xaxis_title='Date',
            yaxis_title='USD',
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No chart data available.")
