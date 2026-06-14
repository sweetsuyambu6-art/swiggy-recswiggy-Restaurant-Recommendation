import streamlit as st
# Define the pages
project_4 = st.Page("project_4.py", title="swiggy", icon="🥘")
page_2 = st.Page("page_2.py", title="order", icon="🥘")

st.sidebar.markdown("swiggy 🥘")

# Set up navigation
pg = st.navigation([project_4, page_2])
# Run the selected page
pg.run()

