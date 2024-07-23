import streamlit as st
from streamlit.runtime.state import session_state

if "login" not in st.session_state:
    st.session_state.login = False

if st.button("Click Me"):
    st.session_state.login = True
    st.write("You are logged in")

if st.button("UnClick Me"):
    st.session_state.login = False
    st.write("You are logged out")

st.button("Button")