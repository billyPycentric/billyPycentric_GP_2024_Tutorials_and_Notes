import streamlit as st


pg  = st.navigation([st.Page("home.py",title="Billys Home Page"),st.Page("about.py"),st.Page("contact.py")])
st.set_page_config(page_title="Pycentric")

pg.run()
