# Login Page

import streamlit as st

def render():
    if st.button("Login"):
        st.session_state.login = True
        
        st.rerun()

render()