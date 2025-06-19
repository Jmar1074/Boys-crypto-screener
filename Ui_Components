import streamlit as st

def render_market_movers(filtered_df):
    st.subheader("📊 Ranked Market Movers")

    for _, row in filtered_df.iterrows():
        col1, col2, col3, col4 = st.columns([2, 3, 3, 1])

        with col1:
            st.markdown(f"**{row['symbol'].upper()}**  \n{row['name']}")

        with col2:
            price = f"${row['current_price']:,.4f}"
            st.markdown(f"**Price:** {price}")

        with col3:
            ratio = f"{row['volume_ratio']:.2f}"
            st.markdown(f"**Volume Ratio:** {ratio}")

        with col4:
            is_starred = row['id'] in st.session_state.starred
            icon = "★" if is_starred else "☆"
            btn_label = f"{icon}"
            if st.button(btn_label, key=f"star-{row['id']}"):
                if is_starred:
                    st.session_state.starred.remove(row['id'])
                else:
                    st.session_state.starred.append(row['id'])
