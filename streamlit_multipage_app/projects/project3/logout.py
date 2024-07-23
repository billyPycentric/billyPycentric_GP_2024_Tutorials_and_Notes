import streamlit as st

def render():
    if st.button("LogOut"):
        st.session_state.login = False
        st.rerun()
        
render()
    