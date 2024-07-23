import streamlit as st

st.title("Welcome to the log out Page")
st.write("Do you want to log out?\n if yes the Press the Button")

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()
logout()